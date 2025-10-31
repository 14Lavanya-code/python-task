print("    Alpha / Digit / special character")
print("---------------------------------------")
a=input("enter the character:")
if len(a) != 1:
    print("Please enter only one character:")
elif a.isalpha():
    print("it is an alphabet .")
elif a.isdigit():
    print("it is an digit .")
else:
    print("It is a special character.")

