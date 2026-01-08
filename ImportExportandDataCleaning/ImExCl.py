import pandas as pd
print("Import, Export and Data Cleaning")
print("CSV Import and Export")
print("**********Task 1*********************")

# Create a DataFrame
# - Save it as students.csv
# - Read the CSV file and save it as students_output.csv without index


data = {
    "Name": ["Ravi", "Kiran", "Meena"],
    "Age": [22, 25, 28],
    "City": ["Chennai", "Bangalore", "Hyderabad"]
}

df=pd.DataFrame(data)
df.to_csv("students.csv",index=False)
print("File created")
s=pd.read_csv("students.csv")
print(s)
print("**************************************")


print("Excel Import and Export")
# - Create a DataFrame
# - Save it as employees.xlsx
# - Read the Excel file and export it as employees_output.xlsx
print("**********Task 2***********************")
data1 = {
    "EmpName": ["Arun", "Divya", "Suresh"],
    "Salary": [30000, 40000, 50000],
    "Dept": ["HR", "IT", "Finance"]
}
df_ex=pd.DataFrame(data1)
df_ex.to_excel("employees.xlsx",index=False)

print("2nd file created")
dt_ex_read=pd.read_excel("employees.xlsx")
print(dt_ex_read)
print("**************************************")

print("JSON Export (records)")
# Task:
# - Create a DataFrame
# - Export it to JSON using orient=&#39;records&#39; and indent=4
print("**********Task 3***********************")

data3 = {
    "Name": ["Alice", "Bob"],
    "Age": [22, 25],
    "City": ["Chennai", "Bangalore"]
}

df_js=pd.DataFrame(data3)

df_js.to_json("students.json", orient="records", indent=4)
print("3rd file created")

dt_js_read=pd.read_json("students.json")
print(dt_js_read)

print("**************************************")
print("JSON Export (columns) ")
print("**********Task 4***********************")
data4 = {
    "Product": ["Pen", "Book"],
    "Price": [10, 50]
}
df_js1=pd.DataFrame(data4)

df_js1.to_json("product.json",indent=4)
print("4rd file created")
df_js1_read=pd.read_json("product.json")
print(df_js1_read)
print("**************************************")
print("5: Drop Rows with Any Missing Values ")
print("**********Task 5***********************")
data5 = {
    "Name": ["John", "Sara", "Mike"],
    "Age": [25, None, 30],
    "City": ["NY", "LA", None]
}
df5=pd.DataFrame(data5)

df_drop=df5.dropna()
print("====drop a data in none=== ")
print(df_drop)


print("**************************************")
print(" Drop Rows Where All Values Are Missing")
print("**********Task 6***********************")
data6 = {
    "A": [1, None],
    "B": [None, None],
    "C": [None, None]
}
df6=pd.DataFrame(data6)
df6_all_drop=df6.dropna(how="all")
print(df6_all_drop)

print("**************************************")
print("Drop Columns with Missing Values ")
print("**********Task 7***********************")
data7 = {
    "Name": ["Ravi", "Kiran"],
    "Age": [22, None],
    "City": ["Chennai", "Bangalore"]
}
df7=pd.DataFrame(data7)
df7_drop_col=df7.dropna(axis=1)
print(df7_drop_col)

print("**************************************")
print("Drop Rows Based on Specific Column ")
print("**********Task 8***********************")
data8 = {
    "Name": ["Anna", "Tom", "Sam"],
    "Age": [21, None, 23],
    "City": ["Paris", "Rome", "Berlin"]
}
df8=pd.DataFrame(data8)
df_age_drop=df8.dropna(subset=["Age"])
print(df_age_drop)
print("**************************************")
print("inplace=True ")
print("**********Task 9***********************")
data9 = {
    "Name": ["A", "B", "C"],
    "Age": [20, None, 25]
}
df9=pd.DataFrame(data9)
df9.dropna(inplace=True)
print(df9)
print("**************************************")
print("CSV → Clean → Excel ")
print("**********Task 10***********************")
data10 = {
    "Student": ["Raj", "Priya", "Kumar"],
    "Marks": [85, None, 90],
    "City": ["Chennai", "Madurai", None]
}
df10=pd.DataFrame(data10)
#save csv file
df10.to_csv("stu_detils.csv",index=False)
#read csv file
s10=pd.read_csv("stu_detils.csv")

print(s10)
# Remove rows where Marks is missing
df10.dropna(subset=["Marks"],inplace=True)
print(df10)
# Export to Excel
df10.to_excel("stu_details.xlsx",index=False)
print(df10)
print("**************************************")
print(" JSON → Clean → CSV")
print("**********Task 11***********************")
data11 = {
    "Item": ["Laptop", "Mouse", None],
    "Price": [50000, None, 800]
}
df11=pd.DataFrame(data11)
df11.to_json("item.json")

#  Export to JSON
s11=pd.read_json("item.json")
print(s11)
# Remove rows with missing values
df11.dropna(inplace=True)
print(df11)
# Save to CSV
df11.to_csv("item.csv")
print("csv file saved")
print("**************************************")
print("Multiple Missing Values ")
print("**********Task 12***********************")
data12 = {
    "Name": ["Ramesh", None, "Sita"],
    "Age": [None, 24, 26],
    "City": ["Delhi", None, "Mumbai"]
}
df12=pd.DataFrame(data12)
# Remove rows with any missing values
rem_dro=df12.dropna()
print(rem_dro)
print("empty values removed")
print("**************************************")
print("Subset Cleaning ")
print("**********Task 13***********************")
print("**************************************")
data13 = {
    "Employee": ["E1", "E2", "E3"],
    "Salary": [30000, None, 45000],
    "Dept": ["HR", "IT", "Finance"]
}
df13=pd.DataFrame(data13)
# Remove rows where Salary is missing
s13=df13.dropna(subset=["Salary"])
print(s13)
print("Export Cleaned Data to JSON ")
print("**********Task 14***********************")
data14 = {
    "Name": ["Leo", "Mia", None],
    "Age": [21, 22, 23]
}
df14=pd.DataFrame(data14)
# Remove rows with missing values
df_remove=df14.dropna()

# Export to JSON using orient="records" and indent=4
df_remove.to_json("clean_data.json",orient="records",indent=4)
print(df_remove)
print("**************************************")
print("Full Practical Workflow ")
print("**********Task 15***********************")
data_final = {
    "Name": ["Arjun", "Kavya", None, "Rohit"],
    "Age": [24, None, 26, 28],
    "City": ["Chennai", "Delhi", "Mumbai", None]
}
# Create a DataFrame
df15=pd.DataFrame(data_final)

# - Remove rows where Age is missing
df15_r=df15.dropna(subset=["Age"])
print(df15_r)
# - Save the cleaned data to CSV
df15_r.to_csv("details.csv",index=False)
# - Export the same cleaned data to JSON using orient="records"
df15_r.to_json("details.json",orient="records",indent=4)
print(df15_r)
print("**************************************")