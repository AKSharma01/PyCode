import os, sys, subprocess

class FileObject:
	"""docstring for FileObject"""
	def __init__(self, location):
		self.location = location
	
	def fileRead(self):
		try:
			file_object = file(self.filenames).read()
		except Exception as e:
			print "*******************"
			print "File not found !!!!"
			print "*******************"
			
		list_word = []
		sentance_len = 0
		file_object = file_object.split()
		for idx, words in enumerate(file_object) :
			sentance_len = sentance_len + 1
			if words[0] == words[0].lower()  :
				try:
					if file_object[idx+1][0] == file_object[idx+1][0].upper() and sentance_len > 1 :
						list_word.append(words)
						print ' '.join(list_word)
						sentance_len = 0
						list_word = []
					else :
						list_word.append(words)
				except :
					list_word.append(words)
			else :
				list_word.append(words)
		print ' '.join(list_word)

	
	def locationValidation(self):
		if self.location:
			try:
				pwd = subprocess.check_output("cd {location} && pwd".format(location = self.location), shell = True)
			except:
				print "Location if not valid."
				return False
		else:
			pwd = subprocess.check_output("pwd", shell = True)

		print "Your Present Working Directory is:\n{pwd}".format(pwd = pwd)
		files = subprocess.check_output("ls {}".format(pwd), shell = True)
		if not files:
			print "No file in this directory"
			return False
		os.system("ls {loc} ".format(loc = pwd))
		file_name = raw_input("Enter the File name:  ")
		full_filename_loc = '{loc}/{file}'.format(loc = pwd[0:-1], file = file_name)
		self.filenames = full_filename_loc
		# print self.filenames
		return True


if __name__ == '__main__':
	file_location = raw_input("Enter The file Location (optional) : ")
	fo = FileObject(file_location)
	if fo.locationValidation():
		fo.fileRead()
