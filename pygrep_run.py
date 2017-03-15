#!/usr/bin/python
import sys, getopt

from pygrep import pygrep
from pygrep import dataPresenter

def main(argv):
	inputfile = ''
	pattern = ''
	message = 'pygrep_run.py -i "Logs/*" -p "PrChecker.Downs"'
	try:
		opts, args = getopt.getopt(argv,"hi:p:",["file=","pattern="])
	except getopt.GetoptError:
		print message
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print message
			sys.exit()
		elif opt in ("-i", "--file"):
			inputfile = arg
		elif opt in ("-p", "--pattern"):
			pattern = arg
	if not inputfile:
		print "no input file given"
		print message
		sys.exit()
	if not pattern:
		print "no pattern given"
		print message
		sys.exit()
	my_grep = pygrep(inputfile)
	my_grep.findInFiles(pattern)
	my_grep.writeToFile()
	
	dp = dataPresenter(my_grep.matched, my_grep.filesName)
	dp.plotData()
	


if __name__ == "__main__":
   main(sys.argv[1:])


