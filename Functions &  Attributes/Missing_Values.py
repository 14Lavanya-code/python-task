
import pandas as pd
# Create a DataFrame that contains missing values in the Name, Age, and City columns.
print("Create a DataFrame")
data = {
    "Name": ["Arjun", None, "Kavya", "Rohit"],
    "Age": [24, 26, None, 28],
    "City": ["Chennai", "Delhi", None, None]
}
df=pd.DataFrame(data)
print(df)
# Check and display the total number of missing values in each column.
print(df.isnull().sum())
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("Remove all rows where the City value is missing")
# Remove all rows where the City value is missing.
df_clean=df.dropna(subset=["City"])
print(df_clean)
# Calculate the average (mean) of the Age column and fill the missing Age values with this average.
print("Calculate the average (mean) ")
age_means=df["Age"].mean()
print(age_means)
df["Age"]=df["Age"].fillna(age_means)
print(df)
# Replace all missing values in the Name column with the string "Unknown".
df["Name"]=df["Name"].fillna("Unknown")
print(df)


