# Task 1: Create a Set
# 1. Create a set named students with the following values:
# o &quot;Ravi&quot;, &quot;Anu&quot;, &quot;Karthi&quot;, &quot;Anu&quot;, &quot;Meena&quot;
# 2. Print the set.
# 3. Observe and write why one value is missing.

# Task 2: Add Elements
# 1. Add a new student &quot;Suresh&quot; to the students set using add().
# 2. Print the updated set.

# Task 3: Update Set
# 1. Create another set named new_students with values:
# o &quot;Divya&quot;, &quot;Ravi&quot;
# 2. Update students using update().
# 3. Print the result.

# Task 4: Remove Elements
# 1. Remove &quot;Meena&quot; using remove().
# 2. Try removing &quot;Arun&quot; using discard().
# 3. Print the set after each operation.

# Task 5: Pop and Clear
# 1. Use pop() to remove one element from the set.
# 2. Print the set.
# 3. Use clear() to remove all elements.
# 4. Print the set again.

# Task 6: Join Sets
# 1. Create two sets:
# 2. A = {10, 20, 30, 40}
# 3. B = {30, 40, 50, 60}
# 4. Find and print:
# o Union

# o Intersection
# o Difference (A − B)
# o Symmetric Difference


print("********************set**********************")
print("create set")
s1={"Ravi", "Anu", "Karthi", "Anu", "Meena"}
print(s1)
print("*******************Add Elements***********************")
s1.add("suresh")
print(s1)
print("*******************Update set***********************")
s1.update(["divya","ravi"])
print(s1)
print("*******************Remove Elements***********************")

print("************remove()*************")
s1.remove("Meena")
print(s1)
print("************discard()*************")
s1.discard("Arun")
print(s1)
print("*********Pop and Clear***************")
s1.pop()
print(s1)
s1.clear()
print("**************Join Sets****************************")
A = {10, 20, 30, 40}
B = {30, 40, 50, 60}

print("------Union-------")
u=A.union(B)
print(u)
print("---Intersection----")
i=A.intersection(B)
print(i)
print("----Difference----")
d=A.difference(B)
print(d)
print("---Symmetric Difference----")
s=A.symmetric_difference(B)
print(s)


