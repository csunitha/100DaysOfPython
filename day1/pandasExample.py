import pandas
csvFile = open('test.csv')
pandafile = pandas.read_csv(csvFile)

#This prints all the row of specific column
#print(pandafile['Subsite']) 
#print(pandafile['Q1.7: Please share why you are dissatisfied with the overall website. *'])

'''
#list all the column names in the pandafile
for header in pandafile:
    print('column ' + header)
'''

#print('\n\n************************ actual feedback ********************* \n\n')
    
#Want to try loop it through each row of specific column decorate and show
feedbacklist = pandafile['Q1.7: Please share why you are dissatisfied with the overall website. *']

for feedback in feedbacklist:
    print(feedback + '\n')

csvFile.close()
