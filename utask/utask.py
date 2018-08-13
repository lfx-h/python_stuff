import subprocess, shlex, os, getpass, sys, ctypes
username = getpass.getuser()
defaults = ('sihost', 'svchost', 'taskhostw', 'explorer', 'igfxEM', 'Shell', 'MSASCuiL', 'nvtray', 'BTTray', 'RAV', 'unsec', 'SystemSettings', 'ApplicationFrameHost', 'SearchUI', 'conhost', 'Taskmgr', 'nvapiw', 'Dell', 'IAStor')#add whatever you need into this list

def useless_p():
	tlist = subprocess.check_output(['tasklist', '/v'])
	tread = tlist.splitlines()
	print('List for potentially useless programs:\n______________________________________')
	count = 1
	udict = {}
	for item in tread:
		sp = tuple(filter(None, item.split()))
		try:
			if username in sp[7]:
				if 'Running' in sp[6]:
					if not any(x in sp[0] for x in defaults):
						
						up = (('{0} - ' + sp[0] + ' : ' + ''.join(sp[9:50])).format(count))
						udict.update({str(count) : sp[0]})
						print up
						count += 1

		except IndexError:
			continue
			
	return udict

def kill(process):
	name = dict[process]
	str = ('Taskkill /IM %s') % name
	try:
		check = subprocess.check_call(str)
	except subprocess.CalledProcessError:
		print('Process requires manual termination through task manager')
		subprocess.call(['start', 'taskmgr.exe'], shell=True)

	
print('Gathering processes...')
dict = useless_p()	
print('\n\n\nType the # of the program you want to kill in the form of "#>1" and then enter')

while True:
	number = raw_input('#>')
	try:
		float(number)
	except ValueError:
		print('Value must be numeric')
		continue
	try:
		kill(number)
	except KeyError:
		print('Value must be in range')
		continue
			
