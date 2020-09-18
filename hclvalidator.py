#!/usr/local/bin/python
import hcl
import glob

ext = ('*.tf', '*.tfvars')
files = []
for file in ext:
    files.extend(glob.glob(file))

for file in files:
    with open(file, 'r') as tffile:
        try:
            hcl.load(tffile)
        except ValueError as e:
            error = str(e)
            sub = 2 if 'unexpected LEFT' in error else 1
            line = str(open(file).readlines()[int(error.split(':')[0].split(',')[0].split()[1])-sub]).strip()
            print("[{}] => [{}] => [{}]".format(file, line, error))
