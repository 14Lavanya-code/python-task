print("Largest Of Three Number")
print("--------------")
num1=int(input("Enter the number1:"))
num2=int(input("Enter the number2:"))
num3=int(input("Enter the number3:"))
if(num1>=num2):
    if(num1>=num3):
        print(num1," is lagest number")
    else:
        print(num3," is lagest number")
else:
    if(num2>=num3):
        print(num2," is lagest number")
    else:
        print(num3," is lagest number")