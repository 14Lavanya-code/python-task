print("Python Task-function")
print("******************************************************************")
print(" Find the Key Found in Dictionary using Arbitrary Keyword Argument.")
print("*****example 1*****")
def add(**n):
    print(n)
add(name="lava",age=18)
print("*****example 2*****")
def add(a,b,**n):
    print("a:",a,"  b:",b)
    print(n)
add(2,"lav",name="lava",age=18)
print("******************************************************************")
print(" Find the Value Found using Arbitrary Argument.")
print("*****example 1*****")

def add(*n):
    print(n)
add("lava",6,"udha")

print("*****example 2*****")
def add(a,b,*n):
    print("a:",a,"  b:",b)
    print(n)
add(1,2,"name","age","user")

print("******************************************************************")
print(" Python function to sum all the numbers in a list using Arbitrary Argument.")


def add(*n):
    print("add(14,16,2,12,1994,2005)",sum(n)) 
add(14,16,2,12,1994,2005)
print("******************************************************************")
print("Python function to print the even numbers from a given list using Arbitrary Argument.")
def add(*n):
    for i in n:
         if i%2==0:
            print(i)
add(14,16,2,12,1994,2005)
print("******************************************************************")
print(" Python function to check whether a number is perfect or not using Arbitrary Argument.")


def perfect(*n):
    for num in n:
        if num <= 0:
            print(num, "is not a Perfect Number")
            continue

        total = 0
        for i in range(1, num):
            if num % i == 0:
                total += i

        if total == num:
            print(num, "is a Perfect Number")
        else:
            print(num, "is not a Perfect Number")

perfect(6, 28, 12, 15)

print("******************************************************************")
print(" Remove a last key from a dictionary using Arbitrary Keyword Argument.")

def last(**data):
    print("original:",data)
    last_key=list(data.keys())[-1]
    data.pop(last_key)
    print("remove :",data)
last(name="lava",age=18,address="madurai")
print("******************************************************************")
print(" Python function to print a Simple Calculator.")
def cal(a,b):
    print("***************")
    print("number 1 :",a,"\nnumber 2 :",b)
    print("***************")
    print("sum      :",a+b)
    print("sub      :",a-b)
    print("multiple :",a*b)
    print("divide   :",a/b)
    print("modulus  :",a%b)
cal(10,5)
print("******************************************************************")
print(" Python function that checks whether a passed string is palindrome or not.")
def pali(*n):
    print("number is",n)
    for  i in n:
        num=i   
        rev=0

        while num>0:
            m=num%10
            rev=rev*10+m    
            num//=10
        if(rev==i):
            print("palindrome")
        else:
            print("not palindrome")
pali(121,789)
print("******************************************************************")
print(" Python function that counts number of vowels, consonants, and special characters in a passed string.")

print(" Python function that counts number of vowels, consonants, and special characters in a passed string.")

def count_chars(s):
    vowels = 0
    consonants = 0
    special = 0

    for ch in s:
        if ch.isalpha():
            if ch.lower() in ('a', 'e', 'i', 'o', 'u'):
                vowels += 1
            else:
                consonants += 1
        else:
            special += 1

    print("Vowels:", vowels)
    print("Consonants:", consonants)
    print("Special Characters:", special)

count_chars("Hello World!@123")
