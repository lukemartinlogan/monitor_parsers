import sys,os
from .monitor import Monitor
import pandas as pd

class CallgrindParser(Monitor):
    def __init__(self, dir, refresh, lang):
        super().__init__(dir, refresh)
        self.lang = lang
        self.raw_path = os.path.join(self.dir, "callgrind_raw.log")
        self.pretty_path = os.path.join(self.dir, "callgrind_pretty.log")
        self.csv_path = os.path.join(self.dir, "callgrind.csv")

    def mointor_cmd(self, command):
        print(f"MONITORING WITH CALLGRIND using cmd={command}")
        self._launch(f"valgrind --tool=callgrind --dump-instr=yes --trace-jump=yes --callgrind-out-file={self.raw_path} {command}".split())

    def monitor_pid(self, pid):
        raise Exception("Cannot monitor using PID for callgrind")

    def parse(self):
        print(f"PARSING CALLGRIND")
        #Parse the raw output
        self._launch(f"callgrind_annotate --show-percs=yes {self.raw_path}".split(), savepid=False, wait=True, stdout=self.pretty_path)
        #Parse the annotated file
        pretty_log = open(self.pretty_path)
        final_csv = open(self.csv_path,'w')
        log = []
        line = pretty_log.readline()
        while line:
            #remove leading spaces
            line = line.lstrip(' ')

            #check if first character is a number
            char = line[0]
            if char.isnumeric():
                #split the line
                split1 = line.split('(')
                split2 = split1[1].split(')')

                #break it up into peices
                Ir = split1[0]
                percent = split2[0]
                description = split2[1]

                #clean up Ir
                Ir = Ir.replace(',','')
                Ir = Ir.strip(' ')

                #clean up percent
                percent = percent.strip('%')

                #clean up description
                description = description.strip('\n')
                description = description.lstrip(' ')
                description = description.replace(',','  ')

                #print to CSV file
                log.append([Ir, percent, description])

            #get next line
            line = pretty_log.readline()

        pretty_log.close()
        pd.DataFrame(log, columns=['Ir', 'Percent', 'Description']).to_csv(self.csv_path, index=False)
