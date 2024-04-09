import pandas as pd
arr=[10,20,30]
indx=['x','y','z']
series1=pd.Series(arr,index=indx)
print(series1['x'])

b={'a':1,'b':2,'c':3}
series2=pd.Series(b)
print(series2)

series3=pd.Series(b,index=['a','c'])
print(series3)

data1={'calories':[100,250,360],'age':[17,19,22]}

indig=pd.Series(['ind1','ind2','ind3'])
datat=pd.Series("day1", "day2", "day3")
df1=pd.DataFrame(data1,index=indig)
df = pd.DataFrame(data1, index = datat)
print(df1)
print(df1.loc[['ind1','ind3']])
print(df1.to_string())

#If you have a large df normal printing only gives first 5 and last 5 rows

dfc=pd.read_csv('data.csv')
data3={'c1':[1,2,3,4],'c2':[1,2,3,4],'c3':[1,2,3,4],'c4':[1,2,3,4],'c5':[1,2,3,4],'eh':[1,2,3,4],'ehh':[1,2,3,4],'c-5':[1,2,3,4],'c-4':[1,2,3,4],'c-3':[1,2,3,4],'c-2':[1,2,3,4],'c-1':[1,2,3,4]}
df3=pd.DataFrame(data3)
print(df3)
print("\n")
print(df3.to_string())
pd.options.display.max_rows=999
print(pd.options.display.max_rows)
data4=pd.Series('ind1','ind2')
df4=pd.read_json('data.json')
print(df4)

df5 = pd.read_json('data.json')
print(df5)
df6=pd.read_csv('data.csv')
print(df6.to_string())
print(df6.info())
