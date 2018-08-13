import time, scandir, os

#pathing variables
root =  os.path.abspath(os.sep)
check_user = os.getenv('username')
user = 'C:\Users\%s' % check_user

def nocase(string):
	string = (''.join((string.lower()).split()))
	return string
	
def search(path, value):
	check = 0
	value = nocase(value)
	for item in scandir.walk(path):
		try:
			clist = []
			clist.extend(item[1]), clist.extend(item[2])
			for file in clist:
				if value in file.lower() or value in nocase(file):
					print 'Found in: ', item[0]
					if os.path.isfile(os.path.join(item[0], file)):
						print 'File name: ', file
					elif os.path.isdir(os.path.join(item[0], file)):
						print 'Directory name: ', file
					print '\n'
					check = 1
					break
		except UnicodeError:
			print 'Error in directory: ', item
			continue
	if check == 0:
		print 'Not Found'

print 'READ ME!!\nThis script is not case sensitive nor space sensitive. It will ignore all capitalized letters and interpret them as neutral and spaces will be set to None\nTo copy a directory highlight it and press: Enter or MB2 and copy\n'

while True:
	print 'Directory to search from:'
	print "Type 'root' for C: OR 'user' for C:\Users\{}".format(check_user)

	while True:
		r = raw_input()
		if r == 'root':
			print '\nDirectory to search from: ', root
			print 'File/Directory to search for:'
			var = raw_input()
			tstart = time.time()
			search(root, var.lower())
			break
		if r == 'user':
			print '\nDirectory to search from: ', user
			print 'File/Direcotry to search for:'
			var = raw_input()
			tstart = time.time()
			search(user, var.lower())
			print var
			break
		else:
			print "\nError\nPlease input 'user' or 'root' again."
			pass
		
	tend = time.time()
	print 'Time of search elapsed: ', (tend - tstart), 'seconds'
	
	print 'If you would like to close the program press: ctrl + c'
	print 'If you would like to search again press: Enter'
	raw_input()
	continue
	
