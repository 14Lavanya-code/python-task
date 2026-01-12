import pandas as pd
import numpy as np
data={
    'Name':['Arun','Bala','Chithra','Divya','ezil'],
    'Age':[21,22,23,22,21],
    'Marks':[85,90,78,88,92]
}
df=pd.DataFrame(data)
print(df)
h=df.head(3)
print(h)
av=df['Marks'].mean()
print("Average",av)
print("pass if mark>=80, as fail")
0
df['Result'] = np.where(df['Marks'] >= 80, 'Pass', 'Fail')
print(df)

mor_mark=df[df['Marks']>=85]
print(mor_mark)





subject=['Maths','science','English','Computer']
Marks=[78,85,88,92]

print("Draw a Bar chart")
print("addtitle,xlable,ylable")
print("Change the marker style")
print("display the graph")

