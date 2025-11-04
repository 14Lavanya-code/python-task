print("************************")
print("1)Print 1 to 20")
print("************************")
for i in range(1,21):
    print(i)


print("************************")
print("2) even numbers 2 to 50")
print("************************")
for i in range(2,51,2):
    print(i)



print("************************")
print("3) Odd numbers 1 to 50")
print("************************")
for i in range(1,50,2):
    print(i)


print("************************")
print("4) Square numbers from 1 to 15")
print("************************")
for i in range(1,16):
    print(f"square value:{i} is {i**2}")



print("************************")
print("5) Cube numbers from 1 to 10")
print("************************")
for i in range(1,11):
    print(f"cube value:{i} is {i**3}")
    



print("************************")
print("6) Print 10 down to 1 reverse order")
print("************************")
for i in range(10,0,-1):
    print(i)



print("************************")
print("7) Multiplication Table of 5")
print("************************")
for i in range(1,11):
    print(f"{i}*5={i*5}")



print("************************")
print("8) Print all char string one by one")
print("************************")
char=["a","b","c","d","e"]
print("string is",char)
for i in char:
    print(i)
print("-------------------------")
num=[1,2,3,4,5]
print("number is",num)
for x in num:
    print(x)



print("************************")
print("10) Divisible by 3 between 1 to 30 ")
print("************************")
for i in range(1,31):
    if(i%3==0):
        print(f"{i}")
print("-------------------------")
