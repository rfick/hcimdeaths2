#Spaces in names come as replacement characters, change them to spaces
def cleanName(name):
	name = list(name)
	for i in range(len(name)):
		if(ord(name[i]) == 160):
			name[i] = ' '
	name = ''.join(name)
	return name

#In url, spaces are replaced with %A0, this does that
def searchName(name):
	returnName = ''
	name = list(name)
	for i in range(len(name)):
		if(name[i] == ' '):
			returnName = returnName + '%A0'
		else:
			returnName = returnName + name[i]
	return returnName