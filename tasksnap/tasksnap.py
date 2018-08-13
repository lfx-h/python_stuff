import subprocess, datetime, os, glob, ast, shlex

snapTime = datetime.datetime.now()
formatTime = str(snapTime).replace(':', '.')
subprocess.call(['mkdir', 'C:\Users\{}\Desktop\TaskLog'.format(os.getenv('username'))], shell=True)
path = 'C:/Users/{}/Desktop/TaskLog/TaskSnapLog{}.txt'.format(os.getenv('username'), formatTime)

def getbTask():
	tasklist = subprocess.check_output(['tasklist', '/v'])
	taskread = tasklist.splitlines()
	snapList = []
	for item in taskread:
		if len(item) != 0:
			service = tuple(item.split())
			sName = service[0]
			sPID = service[1]
			sSession = service[2]
			sMem = service[4]
			sTime = service[8]
			snapList.append((sName, sPID, sSession, sMem, sTime))
	return snapList
	
def getaTask():
	tasklist = subprocess.check_output(['tasklist', '/m'])
	pass
	
			
def logSnap():
	file = open(path, 'a')
	file.write('{}'.format(getbTask()))
	file.close()

def formatSnap(time):
	#(-1 latest, 0 oldest)
	newPath = 'C:/Users/{}/Desktop/TaskLog/'.format(os.getenv('username'))
	files = filter(os.path.isfile, glob.glob(newPath + '*'))
	files.sort(key=lambda x: os.path.getmtime(x))
	for x in files:
		if x.endswith('ini'):
			files.remove(x)
		else:
			pass
			
	file = open(files[time], 'r')
	content = file.read()
	content = ast.literal_eval(content)
	file.close()
	return content
	
def compareSnap(snap1, snap2):
	clist = []
	for tup2 in snap2:
		if not any(tup1 for tup1 in snap1 if tup2[0] == tup1[0]):		
			snap2 = [x for x in snap2 if x[0] != tup2[0]]
			#removes matching tuple from the snap2 array
			clist.append(tup2)
	return clist
		
def getDetails():
	list = compareSnap(formatSnap(0), formatSnap(-1))
	input = raw_input('Process to check: ')
	try:
		float(list[int(input)-1][1])
		var = list[int(input)-1][1]
	except:
		var = list[int(input)-1][2]
		
	print 'Checking for PID ', var, '...'
	print (list[int(input)-1][0])
	print var
	p =subprocess.Popen(['powershell.exe', 'Get-Process -ID {} | Select-Object *'.format(var)], shell=True)
	p.communicate()
	
count = 1
logSnap()
print '#   Image name      |   PID   |  Session  | Memory | CPU Time'
for item in compareSnap(formatSnap(0), formatSnap(-1)):
	print ('{} -').format(count), '  |  '.join(item)
	count += 1
getDetails()

	


