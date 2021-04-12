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

## Examples

```{bash}
python3 main.py -cmd "dd if=/dev/urandom of=/home/lukemartinlogan/Documents/Projects/PhD/parsers/sample/test.bin bs=1M count=500" -dir /home/lukemartinlogan/Documents/Projects/PhD/parsers/sample -t all

python3 main.py -cmd "ping www.google.com -c 5" -dir /home/lukemartinlogan/Documents/Projects/PhD/parsers/sample -t all
```
