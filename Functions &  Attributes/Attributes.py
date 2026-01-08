import pandas as pd

data = {
    "Name": ["Arjun", None, "Kavya", "Rohit"],
    "Age": [24, 26, None, 28],
    "City": ["Chennai", "Delhi", None, None]
}
df=pd.DataFrame(data)
# Print the shape of the DataFrame.
print("++++++++++++++++++++++++++++++++++++++++")
print("shape of the DataFrame")
print(df.shape)
# Display all column names.
print("++++++++++++++++++++++++++++++++++++++++")
print("column names")
print(df.columns)
# 8. Check the data types of each column.
print("++++++++++++++++++++++++++++++++++++++++")
print("Datatype")
print(df.dtypes)
# Set Name as the index.
print("++++++++++++++++++++++++++++++++++++++++")
print("Set Name as the index")
df=df.set_index("Name")
print(df)

# 10. Reset the index back to default.
print("++++++++++++++++++++++++++++++++++++++++")
print("Reset the index ")
df=df.reset_index()
print(df)