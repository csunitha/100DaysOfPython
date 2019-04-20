'''
Program to define groups. And display them in various ways.
'''

import re

'''
#Creating groups in regex with parenthesis 
'''

print(' \n\n Creating groups in regex with parenthesis  \n')

searchtext = 'My number is 415-555-4242.'
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search(searchtext)

print("Search text is: " + searchtext + '\n') 
print('group(1) ' + mo.group(1)) # returns gorup 1
print('group(2) ' + mo.group(2)) # returns group 2
print('group(0) ' + mo.group(0)) # returns entire matched text
print('just group()  ' + mo.group())  # returns entire matched text
# lists all the groups. grouos return tuple hence converting to str
print('groups() returned as tuple ' + str(mo.groups())) 

#groups return tuple, hence doing multiple assignment to variables
areacode, mainnumber = mo.groups()
print ('area code ' + areacode)
print ('main number ' + mainnumber)

'''
#Matching multiple groups with the pipe
'''

print(' \n\n Matching multiple groups with pipe \n')
heroRegex = re.compile (r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
print('group1 ' + mo1.group())

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())
print(mo.group(1))
