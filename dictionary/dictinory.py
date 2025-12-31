print("***************Dictionary ************************************")

print("1)Create a dictionary named student with keys: name, age, and marks.")
student={"name":"lavanya","age":21,"marks":480}
print("Student details are ",'\n',student)
print("============================================================")
print("2)Print the value of the key name from the student dictionary")
print("Student name:",student["name"])
print("============================================================")
print("Add a new key grade with value 'A' to the student dictionary.")
student['grade']='A'
print(student)
print("============================================================")
print("Update the value of marks in the student dictionary.")
student["marks"]=500
print("Student details are ",'\n',student)
print("============================================================")
print("Remove the key age from the dictionary.")
del student["age"]
print(student)
print("============================================================")
print("Check whether the key email exists in the dictionary.")
print(student)
if "email" in student:
    print("The key email exists in the dictionary")
else:
    print("The key email NOT exists in the dictionary")
print(student)
if "name" in student:
    print("The key name exists in the dictionary")
else:
    print("The key name NOT exists in the dictionary")
print("============================================================")
print("Print all keys in the dictionary.")
print(student.keys())
print("============================================================")
print("Print all values in the dictionary.")
print(student.values())
print("============================================================")
print("Print all key–value pairs using a for loop.")
for key,value in student.items():
    print(key ,":", value)
print("============================================================")
print("Create a dictionary with 5 subjects as keys and their marks as values. Find the total marks.")
mark={"english":98,"tamil":89,"maths":87,"physics":82,"chemistry":85,"computer science":99}
print(mark)
print("============================================================")
print("Find the maximum value from a dictionary of marks.")
print("maximum value:",max(mark.values()))

print("============================================================")
print("Count the number of keys in a dictionary.")
print(len(mark.values()))
print("============================================================")
print("Convert two lists (keys and values) into a dictionary.")
n=["name","age","mark"]
m=["lava",21,490]
mn=dict(zip(n,m))
print(mn)
print("============================================================")
print("Create a dictionary and copy it into another dictionary.")
copy1=mark.copy()
print(copy1)
print("============================================================")
print("Create a dictionary of 3 employees and their salaries. Increase each salary by 10%.")
e={}
emp=int(input("enter number of employee add:"))
for i in range(emp):
    k1=input("enter name:")
    v1=float(input("enter salary:"))
    e[k1]=v1
for k1 in e:
    e[k1]+=e[k1]*(10/100)
print( e)
print("============================================================")