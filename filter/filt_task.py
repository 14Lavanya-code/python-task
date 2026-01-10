import pandas as pd

print("Total Salary by Department")

data = {
    "Name": ["Ravi", "Ravi", "Anu", "Anu", "Kiran", "Kiran"],
    "Department": ["IT", "IT", "HR", "HR", "IT", "HR"],
    "Month": ["Jan", "Feb", "Jan", "Feb", "Jan", "Feb"],
    "Salary": [30000, 32000, 28000, 29000, 35000, 36000]
}

df=pd.DataFrame(data)
print(df)
print("Total Salary by Department")
tot_sal=df.groupby("Department")["Salary"].sum()
print(tot_sal)
print("Average Salary by Department")
avg_tot=df.groupby("Department")["Salary"].mean()
print(avg_tot)
print(" Count of Employees by Department")
cou_tot=df.groupby("Department")["Name"].count()
print(cou_tot)
print("Max Salary in Each Department")
max_tot=df.groupby("Department")["Salary"].max()
print(max_tot)
print("Min Salary in Each Department")
min_tot=df.groupby("Department")["Salary"].min()
print(min_tot)
print("Total Salary by Name")
tot_sal=df.groupby("Name")["Salary"].sum()
print(tot_sal)
print("Average Salary by Department and Month")
avg_sal_dep=df.groupby(["Department","Month"])["Salary"].mean()
print(avg_sal_dep)
print("Multiple Aggregations")
mul_agg=df.groupby("Department")["Salary"].agg(
    tot_salary="sum",
    avg_salary="mean",
    max_salary="max",
    min_salary="min",
    count_emp="count"
)
print(mul_agg)
mul_agg=mul_agg.rename(columns={
    "tot_salary":"Total_Salary",
    "avg_salary":"Average_Salary",
    "max_salary":"Max_Salary",
    "min_salary":"Min_Salary",
    "count_emp":"Employee_Count"
})
print(mul_agg)