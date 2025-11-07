print("Program to print Right Triangle")
for i in range(1,6):
    for j in range(1,i+1):
        print(i, end=" ")
    print()

print("Program to print left Triangle")
for i in range(0,6):
    for j in range(1,6-i):
        print(" ", end=" ")
    for k in range(0,i+1):
        print(i,end=" ")   
    print()
print("Write a program to print a square")

for i in range(1,6):
    for j in range(1,6):
        print(i, end=" ")
    for k in range(1,i-j):
        print(" ",end=" ")
    print()

print("program to print 8")
print("Program to print number 8 pattern")

for i in range(7):
    for j in range(5):
        if (j == 0 or j == 4) and (i != 0 and i != 3 and i != 6) or (i == 0 or i == 3 or i == 6) and (j > 0 and j < 4):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print("Program to print a hollow square")

for i in range(5):   # number of rows
    for j in range(5):  # number of columns
        if i == 0 or i == 4 or j == 0 or j == 4:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print("Program to print a hollow right triangle")

rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        if j == 1 or j == i or i == rows:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print("Program to print a hollow inverse right triangle")

rows = 5
for i in range(rows, 0, -1):
    for j in range(1, i + 1):
        if j == 1 or j == i or i == rows:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


print("Program to print an inverse left triangle")

rows = 5
for i in range(rows, 0, -1):
    # print leading spaces
    for j in range(rows - i):
        print(" ", end=" ")
    # print stars
    for k in range(i):
        print("*", end=" ")
    print()


