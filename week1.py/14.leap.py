print("Leap Year")
print("--------------")
year=int(input("Enter the year:"))
if(year%400==0):
    print(year," is leap number")
elif(year%100==0):
    print(year," is not leap number")
elif(year%4==0):
    print(year," is leap number")
else:
     print(year," is not leap number")