#function for pattern recogniser
def semordnilap_recogniser():
	# list for storing file data
	list = []
	new_list = [] 
	# taking filename input from user
	filename = str(raw_input('enter the filename to be opened:'))
	try:
		with open(filename, 'r') as file:
			for lines in file:
				line = lines.strip()
				list.append(line) 
		for word in list:
			words = word.split(" ")
			for word in words:
				new_list.append(word)
		new_list.remove('')
		for i in range(len(new_list)):
			for j in range(1, len(new_list)):
				if new_list[i] == new_list[j][::-1]:
					print new_list[i]+' '+new_list[j]
	except:
		print 'no such file'			


if __name__ == '__main__':
    semordnilap_recogniser()

