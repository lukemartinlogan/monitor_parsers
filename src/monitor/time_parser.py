import sys,os
from .monitor import Monitor
import time

class TimeParser(Monitor):
    def __init__(self, dir, refresh):
        super().__init__(dir, refresh)
        self.raw_path = os.path.join(self.dir, "time.log")

    def mointor_cmd(self, command):
        with open(self.raw_path, 'w') as time_log:
            time_log.write(str(time.time()))

    def monitor_pid(self, pid):
        raise Exception("Monitor using pid not implemented for time")

    def parse(self):
        return
