print("1. Create a list of 5 of your favorite fruits.")
l1=['mango', 'Orange', 'banana',"apple","Pine apple","pomegranate"]
print(l1)
print("****************************************************")
print("2. Add a new fruit to the list using a list method.")
l2="lemon"
l1.append(l2)
print(l1)
print("****************************************************")
print("3. Remove one fruit from the list.")
l1.remove('mango')
print(l1)
print("****************************************************")
print("4. Print the number of fruits in your list.")
print("length:",len(l1))
print("****************************************************")
print("5. Print all the fruits one by one using a for loop.")
for i in l1:
    print(i)
print("****************************************************")
print("6. Reverse the list and print it.")
l1.reverse()
print(l1)
print("****************************************************")
print("7. Sort the list alphabetically and print it.")
l1.sort()
print(l1)
print("****************************************************")
print("8. Check if a particular fruit (like 'Apple') is in the list.")
for i in l1:
    if(i in 'apple'):
        print("List Contain 'apple'")
print("****************************************************")

    