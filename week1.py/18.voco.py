
l = input("Enter a single alphabet letter: ")
if len(l) == 1 and l.isalpha():
    char =l.lower()
    if l == 'a' or l == 'e' or l == 'i' or l == 'o' or l == 'u':
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Invalid input, enter a single alphabet letter.")