import unittest
import sys
import os.path
from pygrep import *

class test_fileListMaker(unittest.TestCase):
	def test_path_to_dir_instead_of_file(self):
		tempDirName = "unit_tests1_temp"
		if not os.path.exists(tempDirName):
			os.makedirs(tempDirName)
		else:
			print "Unit test need to use"+tempDirName+"dir. Please remove it and then run the tests"
			sys.exit()
		fileList = fileListMaker(tempDirName)
		fileList.parseFilesNames()
		fileList.validateFiles()
		os.removedirs(tempDirName)
		self.assertEqual([],fileList.listOfFiles)

	def test_correct_file(self):
		tempFileName = "file_for_unit_test"
		if not os.path.exists(tempFileName):
			tempFile = open(tempFileName, 'w')
			tempFile.close()
		else:
			print "Unit test need to use" +tempFileName+ " file. Please remove it and then run the tests"
			sys.exit()
		fileList = fileListMaker(tempFileName)
		fileList.parseFilesNames()
		fileList.validateFiles()
		os.remove(tempFileName);
		self.assertEqual(tempFileName,fileList.listOfFiles[0])

class test_pygrep(unittest.TestCase):
	def test_finding_string_in_sample_file(self):
		tempFileName = "file_for_unit_test"
		stringToFind = "pattern123"
		if not os.path.exists(tempFileName):
			tempFile = open(tempFileName, 'w')
			tempFile.write(stringToFind)
			tempFile.close()
		else:
			print "Unit test need to use" +tempFileName+ " file. Please remove it and then run the tests"
			sys.exit()
		my_grep = pygrep(tempFileName)
		my_grep.findInFiles(stringToFind)
		os.remove(tempFileName);
		self.assertEqual(my_grep.matched[tempFileName][0],stringToFind)

if __name__ == '__main__':
	unittest.main()
