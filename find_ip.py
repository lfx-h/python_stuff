import re, urllib2

link = raw_input('Website link: ')
if('http://' not in link):
	link = 'http://' + link
print 'Looking up "' + link + '"...'

html = urllib2.urlopen(link)
page_source = html.read()
raw = page_source.split()

print 'What are you looking for?'
print '1 - ip values'
if(raw_input('>') == '1'):
	try:
		for item in raw:
			ip = re.findall(r'(?:^|\b(?<!\.))(?:1?\d\d?|2[0-4]\d|25[0-5])(?:\.(?:1?\d\d?|2[0-4]\d|25[0-5])){3}(?=$|[^\w.])', item)
			try:
				if(len(ip[0].split('.')) > 3):
					print ip
			except IndexError:
				pass
	except TypeError as e:
		print e
	print 'No other values found'
else:
	print 'closing...'
