import glob, sys, mmap

path = 'C:/xampp/htdocs/testdb/*.php'
files = glob.glob(path)

print ('Current path is', path)
if(input('\nWould you like to change the path? y/n   :    ') == 'y'):
	path = input('\nnew path: ')
string_val = input('\nWhat string would you like to search for:  ')

for file in files:
	with open(file) as myFile:
		try:
			for num, line in enumerate(myFile, 1):
				if string_val in line:
					print ('found at line:', num, file)
		except:
			print ('error')