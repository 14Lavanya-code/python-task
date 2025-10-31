print("    Grade")
print("--------------")
mark=int(input("Enter Your Mark:"))
if(mark>80 and mark<=100):
    print("Your Mark is",mark,"\n A grade")
elif(mark>70 and mark<=80):
    print("Your Mark is",mark,"\n B grade")
elif(mark>50 and mark<=70):
    print("Your Mark is",mark,"\n C grade")
elif(mark>35 and mark<=50):
    print("Your Mark is",mark,"\n D grade")
else:
    print("Your Mark is",mark,"\n Fail")

