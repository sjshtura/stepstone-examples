import re

searchstring = 'the cat in the hat'

x = 1
offset = 0
while offset < len(searchstring):
	x = re.search('at',searchstring[offset:])
	print(x.span())
	offset = x.start() + 1

