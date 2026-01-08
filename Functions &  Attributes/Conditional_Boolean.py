
import pandas as pd
import numpy as np
data = {
    "Name": ["Arjun", "Kavya", "Rohit", "Meena"],
    "Age": [28, 32, 35, 26],
    "Salary": [40000, 50000, 60000, 38000],
    "City": ["Chennai", "Bangalore", "Mumbai", "Bangalore"]
}
df=pd.DataFrame(data)

# 16. Display employees whose Salary is greater than 40,000.
print("Display employees whose Salary is greater than 40,000")
print(df[df["Salary"]>40000])
# 17. Show only Name and Salary for employees in Bangalore.
print("Show only Name and Salary for employees in Bangalore")
print(df[df["City"]=="Bangalore"][["Name","Salary"]])
# 18. Create a new column Status where Salary > 40,000.
print("Create a new column Status where Salary > 40,000")
df["Status"]=np.where(df["Salary"]>40000,"High","Low")
print(df)
# 19. Count how many employees belong to each City.
print("Count how many employees belong to each City")
city_co=df["City"].value_counts()
print(city_co)
# 20. Select employees whose Age is between 25 and 35.
print("Select employees whose Age is between 25 and 35")
age_bet=df[(df["Age"]>=30)& (df["Age"]<= 35)]
print(age_bet)