age = int(input("Enter age: "))

if age < 13:
    print("Child")
else:
    if age <= 19:
        print("Teenage")
    else:
        if age <= 59:
            print("Adult")
        else:
            print("Senior Citizen")