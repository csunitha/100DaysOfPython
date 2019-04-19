'''
Simple Program to open file using 'with open'
and strip the new line character and add to a list
'''

loginRequests = []
with open('logfile.log', 'rt') as mylogfile:
    print ('line appending in progress')
    for logline in mylogfile:
        mylines.append(logline.rstrip('\n'))
        print('.',end='')
print(mylines)
