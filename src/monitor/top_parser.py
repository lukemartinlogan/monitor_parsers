import sys,os
from .monitor import Monitor
import pandas as pd

class TopParser(Monitor):
    col_names = ['Time',
             'Duration',
             'Process State',
             'CPU User Space',
             'CPU Kernel Space',
             'Idle Time',
             'Wait Time',
             'Hardware Interrupt',
             'Software Interrupt',
             'Steal Time',
             'RAM Used',
             'Buff/Cache',
             'Swap Used',
             'Available Swap MEM',
             '%CPU',
             '%Mem',
             'Memory',
             'Total Mem',
             'Shared Memory']

    def __init__(self, dir, rank, refresh):
        super().__init__(dir, rank, refresh)
        self.raw_path = os.path.join(self.dir, f"top_raw_{self.rank}.log")
        self.csv_path = os.path.join(self.dir, f"top_{self.rank}.csv")

    def mointor_cmd(self, command):
        raise Exception("Monitor using launch not implemented for top")

    def monitor_pid(self, pid):
        print(f"MONITORING WITH TOP on pid={pid}")
        self._launch(f"top  -d {self.refresh} -b -p {pid}".split(), stdout=self.raw_path)

    @staticmethod
    def _parse_file(array, temp_array):
        #Used to record Clock Time and Runtime
        if array[0] == 'top':
            temp_array.append(array[2])
            temp_array.append(array[4]+' '+array[5][:-1])

        #Used to store Memory Data and %CPU usage of process
        elif array[1] == 'root':
            temp_array.append(array[8])
            temp_array.append(array[9])
            temp_array.append(array[4])
            temp_array.append(array[5])
            temp_array.append(array[6])

        #Gives the state of the process
        elif array[0] == 'Tasks:':
            if array[3] == '1':
                temp_array.append('R')
            elif array[5] =='1':
                temp_array.append('S')
            elif array[7] =='1':
                temp_array.append('T')
            else:
                temp_array.append('Z')

        #Collect CPU data and Interrupt information
        elif array[0] == '%Cpu(s):':
            temp_array.append(array[1])
            temp_array.append(array[3])
            temp_array.append(array[7])
            temp_array.append(array[9])
            temp_array.append(array[11])
            temp_array.append(array[13])
            temp_array.append(array[15])

        else:
            #Collects the Memory Used and Buff/Cache data
            if array[1] == 'Mem':
                temp_array.append(array[7])
                temp_array.append(array[9])

            #Collects information about memory swap used and available
            else:
                temp_array.append(array[6])
                temp_array.append(array[8])

    def parse(self):
        print(f"PARSING TOP")
        temp_array =[]
        buffer =[]
        with open(self.raw_path, 'r') as raw_log:
            temp = raw_log.readline()
            while temp != '':
                temp_array.clear()
                for x in range(9):
                    if temp  != '\n':
                        parse = temp.split()
                        #prevent errors from empty array
                        if not parse:
                            temp = raw_log.readline()
                            continue
                        #Avoids PID row
                        if parse[0] != 'PID':
                            self._parse_file(parse, temp_array)
                    temp = raw_log.readline()
                buffer.append(temp_array)
        df = pd.DataFrame(buffer, columns = TopParser.col_names)
        df.to_csv(self.csv_path, index=False)
