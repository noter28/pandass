import pandas as pd
import sys

'''
df = pd.DataFrame({'id':range(15), 'chars':['ab']*15})
print(df)
'''
df=pd.read_csv('qwerty.csv', sep=',')

print(df.columns)
#print(df.dtypes)
print(df.info)
print(df.describe())
'''
new_line = {'data':25,'type':23}
df=df.append(new_line, ignore_index=True)
print(df.info)
df=df.drop(['type'],axis=1)
print(df)
'''
