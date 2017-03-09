class fileListMaker:
	def __init__(self, path):
		self.path = path
		self.listOfFiles = []
	def parseFilesNames(self):
		import glob
		self.listOfFiles = glob.glob(self.path)
	def validateFiles(self):
		import os.path
		for fname in self.listOfFiles:
			if not os.path.isfile(fname):
				print "file: "+ '\x1b[0;31;47m'+fname + '\x1b[0m' + " is not readable" 
		self.listOfFiles = [fname for fname in self.listOfFiles if os.path.isfile(fname)]

class pygrep:
	def __init__(self, path):
		self.fileListHelper = fileListMaker(path)
		self.fileListHelper.parseFilesNames()
		self.fileListHelper.validateFiles()
		self.filesName = self.fileListHelper.listOfFiles
		self.matched = {}

	def writeToFile(self):
		f_output = open('output.log', 'w')
		for f in self.filesName:
			f_output.write(f+"\n")
			for line in self.matched[f]:
				f_output.write(line)
 
	def findInFiles(self, pattern):
		for f in self.filesName:
			self.matched[f] = self.findInFile(pattern, f)

	def findInFile(self, pattern, fileName):
		linesWithPattern = []
		with open(fileName) as f:
			for line in f:
				if pattern in line:
					linesWithPattern.append(line)
		return linesWithPattern


		
