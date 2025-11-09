print("Check if an element is not in a list")
a = [1, 2, 3, 4]
print(5 not in a)
print("***************************************")
print("Create a list of 5 numbers and print it")
a = [10, 20, 30, 40, 50]
print(a)
print("***************************************")
print("Find the length of a list using len()")
print(len(a))
print("***************************************")
print("Access elements using positive and negative indexes")
print("Positive index:", a[2])
print("Negative index:", a[-2])
print("***************************************")
print("Update the 3rd element of a list")
a[2] = 99
print(a)
print("***************************************")
print("Delete an element from a list using del")
del a[1]
print(a)
print("***************************************")
print("Append a new element to the list using append()")
a.append(60)
print(a)
print("***************************************")
print("Insert an element at a specific position using insert()")
a.insert(1, 25)
print(a)
print("***************************************")
print("Remove an element using remove()")
a.remove(25)
print(a)
print("***************************************")
print("Remove the last element using pop()")
a.pop()
print(a)
print("***************************************")
print("Clear all elements using clear()")
a.clear()
print(a)
print("***************************************")
print("Print all elements of a list using a for loop")
a = [1, 2, 3, 4]
for i in a:
    print(i)
print("***************************************")
print("Find the sum of all elements using sum()")
print(sum(a))
print("***************************************")
print("Find the maximum and minimum values using max() and min()")
print("Max:", max(a))
print("Min:", min(a))
print("***************************************")
print("Count how many times an element appears using count()")
a = [1, 2, 2, 3, 2]
print(a.count(2))
print("***************************************")
print("Find the index of a specific element using index()")
print(a.index(3))
print("***************************************")
print("Reverse a list using reverse()")
a.reverse()
print(a)
print("***************************************")
print("Sort a list in ascending and descending order using sort()")
a.sort()
print("Ascending:", a)
a.sort(reverse=True)
print("Descending:", a)
print("***************************************")
print("Copy one list to another using copy()")
b = a.copy()
print(b)
print("***************************************")
print("Print only even numbers from a list")
for i in a:
    if i % 2 == 0:
        print(i)
print("***************************************")
print("Print only odd numbers from a list")
for i in a:
    if i % 2 != 0:
        print(i)
print("***************************************")
print("Add two lists using + operator")
x = [1, 2]
y = [3, 4]
print(x + y)
print("***************************************")
print("Repeat list elements using * operator")
print(x * 3)
print("***************************************")
print("Check if an element exists in a list using in")
print(2 in x)
print("***************************************")
print("Slice a list (print first 3 and last 3 elements)")
z = [1, 2, 3, 4, 5, 6, 7]
print("First 3:", z[:3])
print("Last 3:", z[-3:])
print("***************************************")
print("Find the largest 2 numbers in a list")
z.sort(reverse=True)
print(z[:2])
print("***************************************")
print("Find duplicate elements in a list")
z = [1, 2, 2, 3, 3, 4]
dup = []
for i in set(z):
    if z.count(i) > 1:
        dup.append(i)
print(dup)
print("***************************************")
print("Remove duplicate elements from a list")
print(list(set(z)))
print("***************************************")
print("Merge two sorted lists into one sorted list")
a = [1, 3, 5]
b = [2, 4, 6]
print(sorted(a + b))
print("***************************************")
print("Create a list of squares of numbers from 1 to 10 using a loop")
squares = []
for i in range(1, 11):
    squares.append(i ** 2)
print(squares)
print("***************************************")
print("Separate even and odd numbers into two lists")
even = []
odd = []
for i in z:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print("Even:", even)
print("Odd:", odd)
print("***************************************")
print("Create a nested list (list inside a list)")
nested = [[1, 2], [3, 4], [5, 6]]
print(nested)
print("***************************************")
print("Access elements from a nested list")
print(nested[1][0])
print("***************************************")
print("Flatten a nested list (convert to one single list)")
flat = []
for sub in nested:
    flat.extend(sub)
print(flat)
print("***************************************")
print("Find common elements between two lists")
a = [1, 2, 3]
b = [2, 3, 4]
print(list(set(a) & set(b)))
print("***************************************")
print("Find elements present in one list but not in another")
print(list(set(a) - set(b)))
print("***************************************")
print("Remove all occurrences of a specific element from a list")
z = [1, 2, 2, 3, 2]
while 2 in z:
    z.remove(2)
print(z)
print("***************************************")
print("Convert a list into a tuple")
print(tuple(a))
print("***************************************")
print("Find the average of list elements")
nums = [10, 20, 30]
print(sum(nums) / len(nums))
print("***************************************")
print("Count positive, negative, and zero numbers in a list")
lst = [-1, 0, 2, -3, 0, 4]
pos = neg = zero = 0
for i in lst:
    if i > 0:
        pos += 1
    elif i < 0:
        neg += 1
    else:
        zero += 1
print("Positive:", pos)
print("Negative:", neg)
print("Zero:", zero)
print("***************************************")
print("Find product of all elements in a list (without using math.prod())")
product = 1
for i in nums:
    product *= i
print(product)