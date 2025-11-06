print(" concatenate a given string to the end of another string.")
s1=input("enter a string1:")
s11=input("enter a string2:")
print(s1+s11)

print(" test if a given string contains the specified sequence of char values.")
s2=input("enter a sentence:")
search=input("Searching char:")
print(search in s2)

print("Convert all the characters in a string to lowercase.")
s3=input("enter a string:")
print(s3.lower())

print("trim any leading or trailing whitespace from a given string")
s4=input("Enter a sentence:")
print(s4.strip())

print("reverse a string")
s5=input("enter a string:")
print(s5[::-1])

print("replace all spaces with underscores")
s6=input("enter the sentence:")
print("After replace:",s6.replace(" ","_"))

print("string made of the middle three characters")
s7=input("enter the sentence:")
m=len(s7)//2
r=s7[m-1:m+2]
print("middle three character",r)



print("First and last letter to capital")
s = input("Enter the sentence: ")
d = ""
print("Count number of words in a string")
s8 = input("Enter a sentence: ")
word = s8.split()
print("Total number of words:", len(word))
for i in s:
    if not i.isdigit():
        d += i

c = len(d)
print("", d[0].upper(),d[1:c-1],d[c - 1].upper())


print("length of a given string")
a = input("Enter a string: ")
print("Length of string:", len(a))

print("Count number of occurrences of a word")
s7 = input("Enter a sentence: ")
cou = input("Enter a word to count: ")
print(f"'{cou}' occurs", s7.count(cou), "times")

    
print("replace of old,new in a given string")
s9 = input("Enter a string: ")
old = input("Enter character to replace: ")
new = input("Enter new character: ")
print("After replacement:", s9.replace(old, new))

print("count vowels in a string")

s10 = input("Enter a string: ")
vowels = "aeiouAEIOU"
c = sum(1 for ch in s10 if ch in vowels)
print("Number of vowels:", c)

print("Check if string has only whitespace")
white = input("Enter a string: ")
print("Contains only whitespace:", white.isspace())

print("Remove all digits from a string")
rem = input("Enter a string with numbers: ")
res = ''.join(ch for ch in rem if not ch.isdigit())
print("String without digits:", res)




