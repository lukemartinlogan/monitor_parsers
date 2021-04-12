import sys,os,subprocess
from abc import ABC, abstractmethod
from shutil import which

class Monitor(ABC):
    def __init__(self, dir, refresh):
        self.dir = dir
        self.pid = None
        self.pidstr = None
        self.refresh = refresh

    def _exe_path(self, exe):
        return which(exe)

    def _launch(self, command, savepid=True, wait=False, stdout=None):
        if stdout is None:
            proc = subprocess.Popen(command)
        else:
            stdout = open(stdout, 'wb')
            proc = subprocess.Popen(command, stdout=stdout)
            stdout.close()
        if savepid:
            self.pid = proc.pid
            self.pidstr = str(self.pid)
        if wait:
            proc.wait()

    @abstractmethod
    def mointor_cmd(self, command):
        return

    @abstractmethod
    def monitor_pid(self, pid):
        return

    def waitpid(self):
    	if self.pid is not None:
            os.waitpid(self.pid, 0)

    def kill(self):
        if self.pid is not None:
            subprocess.Popen(["sudo", "kill", self.pidstr])

    def getpid(self):
        return self.pid

    @abstractmethod
    def parse(self, out_path):
        return
