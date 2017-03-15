import os.path
import matplotlib.pyplot as plt

class fileListMaker:
	def __init__(self, path):
		self.path = path
		self.listOfFiles = []
	def parseFilesNames(self):
		import glob
		self.listOfFiles = glob.glob(os.path.expanduser(self.path))
	def validateFiles(self):
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
			f_output.write("\n"+f+"\n")
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

class dataPresenter:
	def __init__(self, matchedLines, filesName):
		self.rawData = matchedLines
		self.filesName = filesName
		self.process = {}
		self.hitEff = {}
		self.purity = {}
		self.cleanRawData()

	def cleanRawData(self):
		for fileName in self.filesName:
			self.cleanRawDataForGivenFile(fileName)

	def cleanRawDataForGivenFile(self, fileName):
		del self.rawData[fileName][0] #removing first line
		del self.rawData[fileName][-1] #removing last line
		temp_process = []
		temp_hitEff = []
		temp_purity = []
		for line in self.rawData[fileName]:
			splitted_line = line.split()
			temp_process.append(splitted_line[2])
			temp_purity.append(splitted_line[16])
			temp_hitEff.append(splitted_line[19])
		self.process[fileName] = temp_process
		self.purity[fileName] = temp_purity
		self.hitEff[fileName] = temp_hitEff

	def plotData(self):
		for fileName in self.filesName:
			self.plotDataForGivenFile(fileName)

	def plotDataForGivenFile(self, fileName):
		plt.clf()
		plt.plot(self.hitEff[fileName], self.purity[fileName], "ro")
		plt.ylabel("purity [%]")
		plt.xlabel("hit eff [%]")
		splitted_fileName = fileName.split("/")
		plt.savefig("purityVsEff_"+splitted_fileName[-1]+".pdf")









