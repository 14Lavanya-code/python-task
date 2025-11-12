print("1 Write a Python program to find and print all prime numbers between 1 and 100 using") 
co=0
for i in range(2,101):
    num=True
    for j in range(2,i):
        if i%j==0:
            num=False
            break
    if num:
        print(i,end="  ")
        co+=1
print("Total count",co)
print("Pyramid using Nested for loop")
for i in range(1,6):
    print('  '*(6-i),end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    for k in range(i-1,0,-1):
        print(k,end=" ")
    print()
print("3 Write a Python program to calculate the electricity bill based on the following conditions:")

units = int(input("Enter units consumed: "))
bill = 0

if units <= 100:
    bill = units * 1.5
elif units <= 200:
    bill = (100 * 1.5) + ((units - 100) * 2.5)
elif units <= 300:
    bill = (100 * 1.5) + (100 * 2.5) + ((units - 200) * 4.0)
else:
    bill = (100 * 1.5) + (100 * 2.5) + (100 * 4.0) + ((units - 300) * 5.0)
if bill > 1000:
    bill += bill * 0.10

print("Total Bill: ₹{:.1f}".format(bill))
print("starz")
rows = 5  
for i in range(rows):
    s1 = ' ' * (rows-i- 1)
    s2 = '*' * (2 * i + 1)
    print(s1 + s2)
for i in range(rows- 2,-1,-1):
    s1 = ' ' * (rows - i - 1)
    s2 = '*' * (2 * i + 1)
    print(s1 + s2)