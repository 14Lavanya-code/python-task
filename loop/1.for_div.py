print("Divisible by 6 But Not by 9 ")
print("===============================")
for i in range(1,100):
    if(i%6==0 and i%9!=0):
        print(i)

print("Sum of all odd numbers 1 to 50")
print("===============================")
sum=0
for i in range(1,51,2):
    sum+=i
    print(f"{i}={sum}")
print(sum)

print("Divisible by 4 and 6 (Count) ")
print("===============================")
c=0
for i in range(1,200):
    if(i%4==0 and i%6==0):
        c+=1
        print(f"{i}={c}")
print("COUNT: ",c)
print("Table display ")
print("===============================")
n=int(input("Enter the table:"))
for i in range(1,11):
    print(f"{i}*{n}={i*n}")




print("Factorial on given number n ")
print("===============================")
fact=1
fac=int(input("Enter the Number:"))
for i in range(1,fac+1):
    fact*=i
    print(fact)



print("Prime Number Between 1 and 50 ")
print("===============================")

for num in range(2, 51):
    c = 0
    for i in range(2, num):
        c += (num % i == 0)
    if c == 0:
        print(num)
print("===============================")



print("Sum of digit")
num = 1234
sum_digits = 0
length = len(str(num))
for i in range(length):
    digit = num % 10
    sum_digits += digit
    num //= 10

print("Sum of digits:", sum_digits)

print("===============================")
print("cube")
for i in range(1, 101):
    root = round(i ** (1/3))
    if root ** 3 == i:
        print(i)


print("===============================")
print("Reverse")
num = 123
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10
print("Reversed number:", reverse)

print("===============================")
print("skip by 5")

for x in range(1, 101):
    if x % 10 == 5:
        continue
    print(x)



        

