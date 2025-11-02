print("Input marks for three subjects")
mark1 = int(input("Enter marks for subject 1: "))
mark2 = int(input("Enter marks for subject 2: "))
mark3 = int(input("Enter marks for subject 3: "))

if mark1 >= 40 and mark2 >= 40 and mark3 >= 40:
    print("result:Pass")
    average = (mark1 + mark2 + mark3) / 3
    if average >= 90:
        print("You are Outstanding Student")
else:
    print("Fail")

