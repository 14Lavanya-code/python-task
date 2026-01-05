import pandas as pd
print("Row Operations")


data={ 
    "name":["lavanya","almas","guru"],
    "age":[21,25,23],
    "city":["madurai","cmd","vnr"]
}

af=pd.DataFrame(data)
print(af)
print("***************")
print("the second row using loc")
print("***************")
print("loc     ")
print(af.loc[0,"city"])
print("***************")
print("task 2")
print(print(af.loc[af["age"]>21]))
print("***************")
print("the second row using iloc")
print("***************")
print("iloc           ")
print(af.iloc[0,0])

print(af.iloc[0:2,0:3])
print("***************")

print("*******************************************")

print("Slicing Rows")
print("*******************************************")
print("first two rows of the DataFrame")
a=af.iloc[0:2]
print(a)
print("*******************************************")
print("only rows where Age is greater than 23")
age1=af.loc[af["age"]>23]
print(age1)
print("*******************************************")


print("Add a New Column")
print("*******************************************")
af["mark"]=[30000,40000,50000]
print(af)

print("*******************************************")
print("Modify a Column")
print("*******************************************")
print("Increase the Age of all people by 1")
upage=af["age"]=af["age"]+1
print(upage)
print("*******************************************")
print("Increase the Age of only Kiran by 1 using loc.")
af.loc[af["name"]=="guru","age"]+=1
print(af)