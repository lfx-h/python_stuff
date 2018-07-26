import re, urllib2, nltk

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
			ip = re.findall(r'(?:\d{1,3}\.)+(?:\d{1,3})', item)
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
