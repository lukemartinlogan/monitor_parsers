"""
A simple tool to collect monitoring data for running processes or processes to be launched.

USAGE: python3 main.py -cmd "[COMMAND]" -lang [c/java] -dir "/path/to/outdir"
EXAMPLE:
python3 main.py -cmd "dd if=/dev/urandom of=/home/lukemartinlogan/Documents/Projects/PhD/parsers/sample/test.bin bs=1M count=500" -dir /home/lukemartinlogan/Documents/Projects/PhD/parsers/sample -t all
python3 main.py -cmd "ping www.google.com -c 5" -dir /home/lukemartinlogan/Documents/Projects/PhD/parsers/sample -t all
"""

import sys,os
from monitor.time_parser import TimeParser
from monitor.nethogs_parser import NethogsParser
from monitor.top_parser import TopParser
from monitor.iotop_parser import IOTopParser
from monitor.callgrind_parser import CallgrindParser

import argparse, configparser
class ArgumentParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("-cmd", default=None, help="The command to launch an application")
        self.parser.add_argument("-lang", default="c", help="What language the program being launched is built in")
        self.parser.add_argument("-dir", default=str(os.getenv("HOME")), help="The directory to output monitor data")
        self.parser.add_argument("-t", default="all", help="The mode of execution (monitor/parse/all)")
        self.parser.add_argument("-r", default=.5, help="Refresh rate for monitoring (in seconds, can be a fraction)")

    def parse(self):
        args = self.parser.parse_args()
        self.cmd = args.cmd
        self.lang = args.lang
        self.log_dir = args.dir
        self.mode = args.t
        self.refresh = args.r
        return self

if __name__ == '__main__':
    args = ArgumentParser().parse()

    timer = TimeParser(args.log_dir, args.refresh)
    callgrind = CallgrindParser(args.log_dir, args.refresh, args.lang)
    nethogs = NethogsParser(args.log_dir, args.refresh, 'valgrind')
    top = TopParser(args.log_dir, args.refresh)
    iotop = IOTopParser(args.log_dir, args.refresh)

    if args.mode == 'monitor' or args.mode == 'all':
        #Start monitoring the program
        timer.mointor_cmd(args.cmd)
        callgrind.mointor_cmd(args.cmd)
        nethogs.monitor_pid(callgrind.getpid())
        top.monitor_pid(callgrind.getpid())
        iotop.monitor_pid(callgrind.getpid())

        #Wait for the program to stop
        callgrind.waitpid()

        #Kill all monitors
        nethogs.kill()
        top.kill()
        iotop.kill()

    if args.mode == 'parse' or args.mode == 'all':
        #Parse the outputs
        callgrind.parse()
        top.parse()
        iotop.parse()
        nethogs.parse()
