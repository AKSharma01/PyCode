# Question no : 4)

import sys, os
import subprocess


class WordLatency:
	"""docstring for WordLatency"""
	def __init__(self, file_path, file_name):
		self.file_path = file_path
		self.file_name = file_name

	def wordInFile(self):
		if self.file_path:
			self.file_name = self.file_path + '/' + self.file_name
		try:
			total_len = word_number = 0
			self.file_open = file(self.file_name).read()
			print self.file_name 
		except Exception as e:
			print "---------------------------------------"
			print "Invalid Path ! "+str(e)
			print "Your location is {}".format(os.path.dirname(os.path.abspath(__file__)))
			print "Files in your Current dir. : \n{filenames}".format(filenames = subprocess.check_output("ls", shell=True))
			print "---------------------------------------"
		for word in self.file_open.split():
			total_len = total_len + len(word)
			word_number = word_number + 1
		print "Sum words len = {wordlen}, total word = {totalword}, Avg word latency = {wordlatency}".format(wordlen = total_len, totalword = word_number, wordlatency = float(total_len/word_number))


if __name__ == '__main__':
	file_path = str(raw_input("Enter the absolute path of the file without trailing slash (optional): "))
	file_name = str(raw_input("Enter the file with extension: "))
	wl = WordLatency(file_path, file_name)
	wl.wordInFile()