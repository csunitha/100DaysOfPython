import pandas
import matplotlib.pyplot as plt

inputfile = open('../day2/file1 (1).csv')
file = pandas.read_csv(inputfile)
data = pandas.DataFrame(file)
data['index'] = data.index
#print(data)

#Total count of each site
distOfDetails = data.groupby(by='Subsite', as_index=False).agg({'index': pandas.Series.nunique}).sort_values(by='index', ascending=False)
distOfDetails.columns =['Sites','Total']
#print(distOfDetails)

#Total count of overall experience rating
distOfDetails = data.groupby(by='Q1.5: Overall experience', as_index=False).agg({'index': pandas.Series.nunique}).sort_values(by='index', ascending=False)
distOfDetails.columns =['Experience rating','Count']
print(distOfDetails)

#Display as chart using matplotlib pyplot
plt.pie(distOfDetails['Count'],autopct='%1.0f%%', shadow=True, startangle=360)
plt.show()

