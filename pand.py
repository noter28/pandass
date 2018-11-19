import pandas as pd
import sys

'''
df = pd.DataFrame({'id':range(15), 'chars':['ab']*15})
print(df)
'''
df1=pd.read_csv('df1.csv', sep=',')
df2=pd.read_csv('df2.csv', sep=',')
country = ['UA',u'RF',u'RF',u'RF',u'RF']
df2.insert(1,'country',country)
print(df2)




'''
print(df.columns)
#print(df.dtypes)
print(df.info)
print(df.describe())

new_line = {'data':25,'type':23}
df=df.append(new_line, ignore_index=True)
print(df.info)
df=df.drop(['type'],axis=1)
print(df)
'''
