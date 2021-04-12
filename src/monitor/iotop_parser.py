import sys,os
from .monitor import Monitor
import pandas as pd

class IOTopParser(Monitor):
    def __init__(self, dir, refresh):
        super().__init__(dir, refresh)
        self.raw_path = os.path.join(self.dir, "iotop_raw.log")
        self.csv_path = os.path.join(self.dir, "iotop.csv")

    def mointor_cmd(self, command):
        raise Exception("Monitor using launch not implemented for iotop")

    def monitor_pid(self, pid):
        print(f"MONITORING WITH IOTOP on pid={pid}")
        self._launch(f"iotop  -d {self.refresh} -k -o -b -p {pid}".split(), stdout=self.raw_path)

    def parse(self):
        print(f"PARSING IOTOP")
        log = []
        with open(self.raw_path, 'r') as raw_log:
            for line in raw_log.readlines():
                line = line.split()
                if line[0] == 'Total':
                    row = [line[3], line[9]]
                if line[0] == 'Current':
                    row += [line[3], line[9]]
                    log.append(row)
        pd.DataFrame(log, columns=['total_read_bw', 'total_write_bw', 'current_read_bw', 'current_write_bw']).to_csv(self.csv_path, index=False)
