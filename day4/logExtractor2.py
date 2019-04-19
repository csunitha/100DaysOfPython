'''
This program extracts lines in the file which has
string matching'LoginRequest'
And this is done using the string find method and list
'''

loginRequests = []
linenum = 0
searchstring = "loginrequest".lower()
with open('logfile.log', 'rt') as mylogfile:
    for logline in mylogfile:
        linenum += 1
        if logline.lower().find(searchstring) != -1:
            loginRequests.append("Line " +
                                 str(linenum) +
                                 ": " +
                                 logline.rstrip('\n'))
for request in loginRequests:
    print (request)
                                 
       
        
