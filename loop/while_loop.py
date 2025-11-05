print("numbers from 10 down to 1")
i = 10
while (i >= 1):
    print(i)
    i -= 1



print("2. Find the sum of even digits in a number")
n = 4283
even = 0
while (n > 0):
    digit = n % 10
    if digit % 2 == 0:
        even += digit
    n //= 10
print("Sum of even digits:", even)



print("3.Count how many even digits are in a number") 
num = 4283
count = 0
while( num > 0):
    digit = num % 10
    if digit % 2 == 0:
        count += 1
    num //= 10
print("Count of even digits:", count)



print("4. Check if a number is a palindrome")
num = 121
original = num
reverse = 0
while (num > 0):
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10
print("Palindrome:", original == reverse)



print("5. Find the reverse of a number")
num = 1234
reverse = 0
while (num > 0):
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10
print("Reversed number:", reverse)



print("6. Print the Fibonacci series up to 100") 
a, b = 0, 1
while (a <= 100):
    print(a)
    a, b = b, a + b



print("7. Compute the power of a number manually") 
base = 2
exp = 5
result = 1
while (exp > 0):
    result *= base
    exp -= 1
print("Power:", result)



print("8. Keep printing numbers by 2 until it becomes less than 1 (and count how many times)")
num = 20
count = 0
while (num >= 1):
    print(num)
    num -= 2
    count += 1
print("Count:", count)



print("9. Print digits of a number from last to first, one per line") 
num = 1234
while num > 0:
    digit = num % 10
    print(digit)
    num //= 10



print("10. Compute the sum of squares of digits of a number ") 
num = 123
sum_squares = 0
while num > 0:
    digit = num % 10
    sum_squares += digit ** 2
    num //= 10
print("Sum of squares:", sum_squares)


