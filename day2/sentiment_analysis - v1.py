import pandas

inputfile = open('../day2/file1 (1).csv')
file1 = pandas.read_csv(inputfile)
#file1.columns ['Type','Site','Comments','Rating','Date']


inputfile = open('../day2/file1 (2).csv')
file2 = pandas.read_csv(inputfile)


#combine the datasets
data = pandas.DataFrame()
data = pandas.concat([file1,file2],sort=False)
#file1.columns ['Type','Site','Comments','Rating','Date']

data['index'] = data.index
#print(data)

#Total count of each site
distOfDetails = data.groupby(by='Subsite', as_index=False).agg({'index': pandas.Series.nunique}).sort_values(by='index', ascending=False)
#distOfDetails = data.groupby(by='Subsite', as_index=False).agg({'index': pandas.Series.nunique}).sort_values(by='index', ascending=False)

distOfDetails.columns =['Subsite','COUNT']
print(distOfDetails)

#Total count of overall experience rating


