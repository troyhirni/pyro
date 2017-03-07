"""
Copyright 2014-2017 Troy Hirni
This file is part of the pyro project, distributed under the terms 
of the GNU Affero General Public License.

** MAIN **

python -m pyro --help
python -m pyro --clean # remove .pyc files and __pycache__ directories
python -m pyro --ipath # print the `innerpath` to pyro package
python -m pyro --test  # test loading of modules and file wrapper io
"""


import sys
from . import *


if __name__ == '__main__':
	
	app = sys.argv[0]
	cmd = sys.argv[1] if len(sys.argv) > 1 else ''
	args = sys.argv[2:]
	
	# help/how-to reminders
	if not cmd or (cmd in ['-h', '--help']):
		print (__doc__)
	
	# print the arguments received by this call
	elif cmd == '--args':
		print (str(sys.argv))
	
	# print the inner-path for python imports within the package
	elif cmd == '--ipath':
		print ("%s" % (Base.innerpath(*args)))
	
	# test loading of modules and file wrapper io
	elif cmd == '--test':
		from pyro.dev import test
		test.report()
	
	# remove *.pyc files
	elif cmd == '--clean':
		d = Base.ncreate('fs.dir.Dir', *args[1:])
		d.search('pyro', '__pycache__', fn=d.rm)
		d.search('pyro', '*.pyc', fn=d.rm)
