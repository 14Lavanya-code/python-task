print("*********************************")
print("1.Reverse a given list in Python  ")

l = [100, 200, 300, 400, 500]
print(l)
print("*********************************")
print("2.Concatenate two list  ")
list1 = ["hello","madam"]
list2 = ["Dear", "Sir"]
print(list1)
print(list2)
print(list1+list2)
print("*********************************")
print("3. Remove empty strings from the list of strings")
li=["pen","pencil"," ","eraser"," ","scale"]
while " " in li:
    li.remove(" ")
print(li)
print("*********************************")
print("4.Write a Python program to convert a string to a list.")
st=input("Enter the name:")
li1=list(st)
print(st)
print(li1)
print("*********************************")
print("5.Check if a list contains an element")
li3=[1, 2, 3, "a","b","c"]
print(li3)
if li3==[]:
    print(" list contains an No  element")
else:
    print(" list contains an element")
print("*********************************")
print("Remove All enlement in list")
li5=[1, 2, 3, "a","b","c"]
print(li5)
li5.clear()
print("LIST:",li5)
print("*********************************")
print("Count the occurrence of a specific object in a list pets")
pets = ['dog', 'cat', 'fish', 'fish', 'cat']
print("Number of times 'cat' appears:", pets.count('cat'))
print("*********************************")
print("8.Return the length of a list")
n=[1, 2, "m", "l","b","c"]
print(len(n))
print("*********************************")
print("9. Insert a value at a specific index in an existing list")
n1=["m", "l","b","c"]
n1.insert(2,"o")
print(n1)
print("*********************************")
print("10. Write a Python program to clone or copy a list.")
a=["a",2,"hello",True]
b=a.copy()
print(b)
print("*********************************")
print("11. Write a Python program to extend a list without append.")
li6=['a', 'b']
li7=['c', 'd']
ex=li6.extend(li7)
print()
lets= ['a', 'b']
lets.extend('c1234')
print(lets) 
print("*********************************")
print("12.sRemove duplicates from a list")
li8= [3, 2, 2, 1, 1, 1]
emp=[]
for i in li8:
    if i not in emp:
        emp.append(i)
print(emp)
print("*********************************")
print("13.Find the index of the 1st matching element")
ind=["zero","one","two","three","four"]
ext=ind.index("two")
print(ext)
print("*********************************")