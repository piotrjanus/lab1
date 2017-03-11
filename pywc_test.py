import unittest
import os
from pywc import pywc


class test_pywc(unittest.TestCase):
	def test_compare_my_pywc_and_default_wc(self):
		fileNameToCount = "pywc_test.py"
		my_pywc = pywc([fileNameToCount])
		my_pywc.countInFiles()
		os.remove('pywc.log')

		import subprocess
		p = subprocess.Popen(['wc', fileNameToCount], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		out, err = p.communicate()
		out = out.split()
		self.assertEqual(int(out[0]),my_pywc.lines[fileNameToCount])	
		self.assertEqual(int(out[1]),my_pywc.words[fileNameToCount])
		self.assertEqual(int(out[2]),my_pywc.chars[fileNameToCount])

if __name__ == '__main__':
	unittest.main()
