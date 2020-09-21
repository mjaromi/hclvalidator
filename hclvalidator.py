#!/usr/local/bin/python
import hcl
import sys
import glob

ext = ('*.tf', '*.tfvars')
files = []

path = sys.argv[1] if len(sys.argv) == 2 else '.'
    
for file in ext:
    files.extend(glob.glob(path + '/' + file))

for file in files:
    with open(file, 'r') as tffile:
        try:
            hcl.load(tffile)
        except ValueError as e:
            error = str(e)
            sub = 2 if 'unexpected LEFT' in error else 1
            line = str(open(file).readlines()[int(error.split(':')[0].split(',')[0].split()[1])-sub]).strip()
            print("[{}] => [{}] => [{}]".format(file, line, error))
            sys.exit(1)
