import pandas as pd

data = {
    "Name": ["Arjun", "Kavya", "Rohit", "Meena"],
    "Age": [28, 32, 35, 26],
    "Salary": [40000, 50000, 60000, 38000],
    "City": ["Chennai", "Delhi", "Mumbai", "Chennai"]
}
df=pd.DataFrame(data)
print(df)
# Sort the DataFrame by Age in ascending order.
print("Sort the DataFrame by Age in ascending order")
df_arrange=df.sort_values(by="Age",ascending=True)
print(df_arrange)
# 12. Sort the DataFrame by Salary in descending order.
print("Sort the DataFrame by Salary in descending order")
df_arrange_des=df.sort_values(by="Age",ascending=False)
print(df_arrange_des)
# 13. Increase Salary by 5000 for employees whose Age &gt; 30.
print("Increase Salary by 5000 for employees whose Age >30")
df.loc[df["Age"]>30,"Salary"]+=5000
print(df)
# 14. Replace "Chennai" with "Chennai City" in the City column.
print("Replace 'Chennai' with 'Chennai City' in the City column")
df["City"]=df["City"].replace("Chennai","Chennai city")
print(df)
# 15. Add a new row using .loc.
df.loc[len(df)]=["lavanya",22,80000,"Chennai"]
print(df)