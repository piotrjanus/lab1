import sys
from pygrep import fileListMaker
import logging
import os

class pywc:
	def __init__(self, listOfFilesNotValidated):
		self.fileListHelper = fileListMaker("")
		self.fileListHelper.listOfFiles = listOfFilesNotValidated
		self.fileListHelper.validateFiles()
		self.filesName = self.fileListHelper.listOfFiles
	
		self.words = {}
		self.lines = {}
		self.chars = {}
		
		fileLogName = 'pywc.log'
		if os.path.exists(fileLogName):
			os.remove(fileLogName)
		logging.basicConfig(filename=fileLogName,level=logging.INFO)


	def countInFiles(self):
		for file_name in self.filesName:
			self.countInFile(file_name)
	
	def countInFile(self, file_name):
		self.lines[file_name] = 0
		self.words[file_name] = 0
		self.chars[file_name] = 0
		with open(file_name, 'r') as in_file:
			for line in in_file:
				self.lines[file_name] += 1
				self.words[file_name] += len(line.split())
				self.chars[file_name] += len(line)

		logging.info("%d %d %d %s",self.chars[file_name], self.words[file_name], self.lines[file_name], file_name)
		


def main():
	temp_list = list(sys.argv)
	del temp_list[0]
	if(len(temp_list)==0): 
		print "no file given"
	else:
		my_pywc = pywc(temp_list)
		my_pywc.countInFiles()


if __name__ == '__main__':
	main()

