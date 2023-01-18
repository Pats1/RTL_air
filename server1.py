#!/usr/bin/python

import subprocess x = subprocess.run(['sudo rtl_tcp -d 1 -p 2200 -a 192.168.1.35'], shell=True) print(x) print(x.args) print(x.returncode) print(x.stdout) print(x.stderr)
