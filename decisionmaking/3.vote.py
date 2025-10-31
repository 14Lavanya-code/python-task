print("Vote Eligiblity Or not")
print("------------------------")
age=int(input("Enter the age:"))
if(age>=18):
    print("You are eligible for voting")
else:
    nage=18-age
    print("You are eligible not for voting. \n Your age is",age,"waiting for",nage,"year")
    