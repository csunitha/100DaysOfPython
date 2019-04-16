import csv
feedbackFile = open('feedback.csv')
csvReader = csv.reader(feedbackFile)

for row in csvReader:
	print('Row #' + str(csvReader.line_num) + ' ' + str(row) + '\n')

feedbackFile.close()
