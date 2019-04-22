''' day6 Understanding on iterators '''


listvalues = [1,2,3,4,8,9,10]

print (listvalues)
print ('list of values through simply iterating the list')
for val in listvalues:
    print (val)

print ('\n')
print ('list of values through simply reversing the list')
for val in reversed(listvalues):
    print (val, end='') #end removes the line break

print ('\n\nThe last element in the list  ' + str(listvalues [-1]))

#sequence unpacking
sequencevalues = [21,35,78]
a, b, c = sequencevalues

print ('\n\nsequence ' + str(sequencevalues))
print ('printing b in the sequence extracted using sequence unpacking ' + str(b))
