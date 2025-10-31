print("  Mark and Attenence ")
print("--------------")
marks = float(input("Enter student's marks: "))
attendance = float(input("Enter student's attendance percentage: "))

if marks >= 85 and attendance >= 90:
    print("Eligible for Scholarship")
else:
    print("Not Eligible for Scholarship")