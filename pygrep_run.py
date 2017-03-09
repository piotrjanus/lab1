from pygrep import pygrep

my_grep = pygrep("../lab1/Logs/*")
my_grep.findInFiles("PrChecker.Downs")
my_grep.writeToFile()
