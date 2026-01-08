import pandas as pd

data = {
    "Name": ["Arjun", "Kavya", "Rohit", "Meena", "Suresh", None],
    "Age": [28, 32, 35, 26, 41, None],
    "Salary": [40000, 50000, 60000, 38000, 72000, 45000],
    "City": ["Chennai", "Delhi", "Mumbai", "Chennai", "Bangalore", None]
}
df=pd.DataFrame(data)

# 21. Export the DataFrame to a CSV file.
print("Export the DataFrame to a CSV file")
df.to_csv("employee.csv",index=False)

# 22. Import the CSV file back into Pandas.
print("Import the CSV file back into Pandas")
df_imp=pd.read_csv("employee.csv")
print(df_imp)
# 23. Display the first 5 rows using head().
print("Display the first 5 rows using head()")
print(df_imp.head(5))
# 24. Display the last 3 rows using tail().
print("Display the last 3 rows using tail()")
print(df_imp.tail(3))
# 25. Check if the DataFrame contains any missing values.
print("Check if the DataFrame contains any missing values")
print(df_imp.isnull().values.any())
print("+++++++++++++++++++++++++++++++")
print(df_imp.isnull().any())