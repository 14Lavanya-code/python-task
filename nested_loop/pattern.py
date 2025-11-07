print("Pattern 1") 
rows = 6
for i in range(rows):
    print(chr(65 + i) * (i + 1))
print("Pattern 2") 

rows = 5
ch = 65
for i in range(rows):
    for j in range(i + 1):
        print(chr(ch), end="")
        ch += 1
    print()

print("Pattern 3")
# Pattern 3
rows = 5
for i in range(rows):
    print(chr(65 + i) * (i + 1))

print("Number Pattern 1")

rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("Number Pattern 2")   

rows = 5
for i in range(rows, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


print("Number Pattern 3 (pyramid)") 
rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i), end="")
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("Number Pattern 4 (inverted pyramid) ")

rows = 5
for i in range(rows, 0, -1):
    print(" " * (rows - i), end="")
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

