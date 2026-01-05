import pandas as pd

print("Series Creation")
print("Create a Pandas Series with values: 5, 10, 15, 20")
sp=pd.Series([5,10,15,20],index=["W","X","Y","Z"])
print("Print the Series")
print(sp)
print("X =",sp['X'])