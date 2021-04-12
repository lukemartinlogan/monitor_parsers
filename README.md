# MonitorParsers

A simple tool for monitoring and profiling applications.

## Installation

### For Regular Users
```{bash}
cd /path/to/monitor_parsers  
sudo su
python3 -m pip install -r requirements.txt  
python3 setup.py sdist bdist_wheel  
python3 -m pip install dist/*.whl  
rm -r dist build *.egg_info MANIFEST  
```

### For Developers
```{bash}
cd /path/to/monitor_parsers  
sudo su
python3 -m pip install -r requirements.txt  
sudo python3 setup.py develop
```

### Uninstallation

```{bash}
python3 -m pip uninstall monitor
```

### Dependencies

```{bash}
sudo apt-get install valgrind nethogs sysstat
```

## Usage

monitor -dir "/path/to/outdir" -r [refresh-rate (sec)] -cmd "[COMMAND]" -t [monitor/parse/all]  
* dir: The directory to output parser data to  
* r: The refresh rate for the monitor tools (in seconds, can be fractional)  
* cmd: The command to execute and monitor. Must be in quotations!  
* t: Collect monitor data (monitor), parse logs into CSVs (parse), or both (all)

## Examples

This is an example of collecting raw monitor data:
```{bash}
sudo su
mkdir ${HOME}/sample
monitor -cmd "dd if=/dev/urandom of=${HOME}/sample/test.bin bs=1M count=500" -dir ${HOME}/sample -t monitor
```

This is an example of parsing the monitor data and producing CSVs (still use the cmd):
```{bash}
sudo su
mkdir ${HOME}/sample
monitor -cmd "dd if=/dev/urandom of=${HOME}/sample/test.bin bs=1M count=500" -dir ${HOME}/sample -t parse
```

This is an example of monitoring and parsing at the same time (may not work):
```{bash}
sudo su
mkdir ${HOME}/sample
monitor -cmd "dd if=/dev/urandom of=${HOME}/sample/test.bin bs=1M count=500" -dir ${HOME}/sample -t all
```
