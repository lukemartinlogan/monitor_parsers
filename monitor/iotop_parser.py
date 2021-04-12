import sys,os
from .monitor import Monitor

class IOTopParser(Monitor):
    def __init__(self, dir, refresh):
        super().__init__(dir, refresh)
        self.raw_path = os.path.join(self.dir, "iotop_raw.log")
        self.csv_path = os.path.join(self.dir, "iotop.csv")

    def mointor_cmd(self, command):
        raise Exception("Monitor using launch not implemented for iotop")

    def monitor_pid(self, pid):
        print(f"MONITORING WITH IOTOP on pid={pid}")
        self._launch(f"iotop  -d {self.refresh} -o -b -p {pid}".split(), stdout=self.raw_path)

    def parse(self):
        print(f"PARSING IOTOP")
        with open(self.csv_path, 'w') as CSVouput, open(self.raw_path, 'r') as raw_log:
            for line in raw_log.readlines():
                if line.decode().split()[0] == 'Actual':
                    #print(line.decode(), " ||| ", line.decode().split()[6])
                    print((line.decode().split()[-2]).strip())
                    CSVouput.write((line.decode().split()[-2]).strip())
                    CSVouput.write("\n")
