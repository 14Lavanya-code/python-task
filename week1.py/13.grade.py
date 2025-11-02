print("    Grade")
print("--------------")
mark=int(input("Enter Your Mark:"))
if(mark>=90 and mark<=100):
    print("Your Mark is",mark,"\n A grade")
elif(mark>=75 and mark<90):
    print("Your Mark is",mark,"\n B grade")
elif(mark>=50 and mark<75):
    print("Your Mark is",mark,"\n C grade")
else:
    print("Your Mark is",mark,"\n Fail")

