'''
This program extracts lines in the file which has
string matching'LoginRequest'
And this is done using regex and tuples
'''

import re
loginRequests = []
linenum = 0
regexpattern = re.compile("LoginRequest", re.IGNORECASE)
with open('logfile.log', 'rt') as mylogfile:
    for logline in mylogfile:
        linenum += 1
        if regexpattern.search(logline) != None:
            loginRequests.append((linenum, logline.rstrip('\n')))
                                
for request in loginRequests:
    print ("Line num : " + str(request[0]) + " : " + request[1])
                                 
       
        
