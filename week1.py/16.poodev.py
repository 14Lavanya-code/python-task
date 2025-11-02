print("positive or negative /odd or even ")
a=int(input("enter the number:"))
if(a>0):
    print("Positive number")
    if(a%2==0):
        print("even number")
    else:
        print("odd number")
else:
    print("Negative number or zero")

