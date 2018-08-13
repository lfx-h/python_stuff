import subprocess, shlex, re, socket
'''
Windows only script programmed on 'Microsoft Windows [Version 10.0.16299.125]'
By shaxeey

Command line commands used: netsh, ipconfig
Functions:
netw.help() - list of functions
netw.networkList() - return a list with 2 sublists 
netw.printed() - readable wifilist format
netw.find.ipv4/ipv6/dns/gateway/subnet/ipconfig()
'''
def help():
	print 'Functions:\nnetw.networkList() - array of networks\nnetw.printed - readable networks\nnetw.find.ipv4/ipv6/dns/gateway/subnet/ipconfig()'

class find:
	#a getter class, returns data in a singular string except for find.ipconfig(), which is readable
	@staticmethod
	def format():
		raw = subprocess.check_output(shlex.split('ipconfig /all'), shell=True).splitlines()
		idx = raw.index('Wireless LAN adapter Wi-Fi:')
		raw = raw[idx:]
		return raw
		
	@staticmethod
	def ipv4():
		for data in find.format():
			if 'IPv4 Address' in data:
				data = list(data)
				data = ''.join(data[39:-12])
				return data
				break
				
	@staticmethod
	def ipv6():
		for data in find.format():
			if 'IPv6 Address' in data:
				data = list(data)
				data = ''.join(data[39:-12])
				return data
				break
				
	@staticmethod
	def dns():
		for data in find.format():
			if 'DNS Suffix' in data:
				data = list(data)
				data = ''.join(data[39:])
				return data
				break
				
	@staticmethod
	def subnet():
		for data in find.format():
			if 'Subnet Mask' in data:
				data = list(data)
				data = ''.join(data[39:])
				return data
				break
			
	@staticmethod
	def gateway():
		for data in find.format():
			if 'Default Gateway' in data:
				data = list(data)
				data = ''.join(data[39:])
				return data
				break
				
	@staticmethod
	def ipconfig():
		for item in find.format():
			print item
			
	
def networkList():
	#vars
	sn = []
	separator = []
	networkArray = []
	raw = subprocess.check_output(shlex.split('netsh wlan show networks mode=bssid')).splitlines()
	i = 0
	formater = False
	#sets a separator between singular networks
	for v in raw:
		words = v.split()
		for match in words:
			if re.search(r'\b' + match + r'\b', 'SSID'):
				separator.append(raw.index(v))
	#start
	for x in raw:
		if 'Interface name' in x:
			if 'Wi-Fi' in x:
				interface = 'Wi-Fi'
				#unf
		if 'currently visible' in x:
			numNetworks = re.sub('\D', '', x)
			#unf
		try:
			#checks whether a new SSID is being itterated through
			if raw.index(x) == separator[i]:
				if len(sn) != 0:
					if not format_data(sn) in networkArray:
						#appends a singlur network to the networkArray array
						networkArray.append(format_data(sn))
				formater = True
				del sn[:]
				i += 1
		except IndexError:
			pass
		#only runs once for order
		if formater:
			sn.append(x)
		#only executes if the raw array reaches the end
		if x == ''.join(raw[-1:]):
			if len(sn) != 0:
				if not format_data(sn) in networkArray:
					networkArray.append(format_data(sn))
	return networkArray
	
def format_data(dataList):
	netList = []#[[base],[bssid]] 
	base = []#[0]=SSID, [1]=Auth, [2]=Encryption
	bssid = []#[0]=AP mac, [1]=signal%, [2]=Channel
	for data in dataList:
		words = data.split()
		for match in words:
			if re.search(r'\b'+ match + r'\b', 'SSID'):
				data = list(data)
				data = ''.join(data[9:])
				if data == '':
					data = 'Hidden Network'
				base.append(data)
		if 'Authentication' in data:
			data = list(data)
			data = ''.join(data[30:])
			base.append(data)
		if 'Encryption' in data:
			data = list(data)
			data = ''.join(data[30:-1])
			base.append(data)
		for match in words:
			if re.search(r'\b'+ match + r'\b', 'BSSID'):
				data = list(data)
				data = ''.join(data[30:])
				bssid.append(data)
		if 'Signal' in data:
			data = list(data)
			data = ''.join(data[30:-2])
			bssid.append(data)
		if 'Channel' in data:
			data = list(data)
			data = ''.join(data[30:-1])
			bssid.append(data)
				
	netList.append((base, bssid))
	return netList
			
def printed():
	try:
		for network in networkList():
			try:
				print '\n___________________________________'
				print 'SSID           : ' + network[0][0][0]
				print 'Authentication : ' + network[0][0][1]
				print 'Encryption     : ' + network[0][0][2]
				print '	|BSSID  AP : ' + network[0][1][0]
				print '	|Signal  % : ' + network[0][1][1]
				print '	|Channel # : ' + network[0][1][2]
			except IndexError:
				print 'Missing BSSID, please refresh Wi-Fi cache by clicking on the wifi on your taskbar'
	except subprocess.CalledProcessError:
		print 'Error getting list of networks, Wi-Fi not detected'
			
			
