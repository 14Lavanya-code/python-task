import pandas as pd
print("Create a DataFrame")
print("==========Task 1=================")
df={
    "name":["lavanya","Almas","Guru"],
    "age":[21,20,22],
    "City":["madurai","coimbatore","chennai"]
}
dafr=pd.DataFrame(df)
print(dafr)
print("==========Task 2=================")
print("Print only the Name column")
n=pd.DataFrame(df["name"])
print(n)
print("Print Name and City columns together")
naci = dafr[["name","City"]]
print(naci)
