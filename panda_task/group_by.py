import pandas as pd

# Moderate GroupBy Tasks Explained in Words
data = {
    "Name": ["Ravi", "Ravi", "Anu", "Anu", "Kiran", "Kiran"],
    "Department": ["IT", "IT", "HR", "HR", "IT", "HR"],
    "Month": ["Jan", "Feb", "Jan", "Feb", "Jan", "Feb"],
    "Salary": [30000, 32000, 28000, 29000, 35000, 36000]
}
df=pd.DataFrame(data)
print("")
# 📝 GroupBy Tasks
# Q1. Find total and maximum salary for each employee
print("Total and maximum salary for each employee")

tot_max_sal=df.groupby("Name")["Salary"].agg(
    Total_salary="sum",
    max_salary="max"
)
print(tot_max_sal)
# Q2. Find average salary for each department and sort it descending
avg_sal_dep=df.groupby("Department")["Salary"].mean().sort_values(ascending=False)
print(avg_sal_dep)
# Q3. Find department-wise total salary for only February
print("department-wise total salary for only February")
feb_data=df[df["Month"]=="feb"]
tot_sal_dep=df.groupby("Department")["Salary"].sum()
print(tot_sal_dep)
# Q4. Find employees whose total salary is greater than 60,000
print("employees whose total salary is greater than 60,000")
gre_sal=df[df["Salary"]>=60000]
tot_sal_gre=df.groupby("Name")["Salary"].sum()
print(tot_sal_gre)
# Q5. Find month-wise total salary for each department
print("month-wise total salary for each department")
mon_tot_sal=df.groupby("Month")["Salary"].sum()
print(mon_tot_sal)
# Q6. Find department-wise salary count, sum, and average
sal_sac=df.groupby("Department")["Salary"].aggregate(
    sal_sum="sum",
    sal_count="count",
    sal_avg="mean"
)
print(sal_sac)
# Q7. Find which month has the highest total salary
print("month has the highest total salary")
mon_hig=df.groupby("Month")["Salary"].sum()
hi_mon=mon_hig.idxmax()
hig_val=mon_hig.max()
print(mon_hig)
print("highest total salary",hi_mon,'with',hig_val)
# Q8. Add a column showing department average salary using transform()
df["avg_salary"]=df.groupby("Department")["Salary"].transform("mean")
print(df)
# Q9. Find employees whose salary is above their department’s average
above_avg=df[df["Salary"]>df["avg_salary"]]
print(above_avg)
# Q10. Convert department-wise total salary into a dictionary
print("department-wise total salary into a dictionary")
dept_tot_sal_dis = df.groupby("Department")["Salary"].sum().to_dict()
print(dept_tot_sal_dis)
