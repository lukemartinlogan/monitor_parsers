# MonitorParsers

A simple tool for monitoring and profiling applications.

## Installation

```{bash}
cd /path/to/parsers  
python3 -m pip install -r requirements.txt  
python3 setup.py develop --user
```

### Uninstallation

```{bash}
python3 -m pip uninstall luxio
```

## Usage

monitor -dir "/path/to/outdir" -r [refresh-rate (sec)] -cmd "[COMMAND]" -t [monitor/parse/all]  
* dir: The directory to output parser data to  
* r: The refresh rate for the monitor tools (in seconds, can be fractional)  
* cmd: The command to execute and monitor. Must be in quotations!  
* t: Collect monitor data (monitor), parse logs into CSVs (parse), or both (all)

## Examples

```{bash}
mkdir ${HOME}/sample
monitor -cmd "dd if=/dev/urandom of=${HOME}/sample/test.bin bs=1M count=500" -dir ${HOME}/sample -t all
monitor -cmd "ping www.google.com -c 5" -dir ${HOME}/sample -t all
```
