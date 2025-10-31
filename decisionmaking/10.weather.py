print("Weather check cold/warm/hot/cool")
print("--------------")
we=input("enter Your climate\n(cold/warm/hot/cool):")
if(we=="hot"):
    print("this is hot climate \n Take water more.")
elif(we=="warm"):
    print("This is warm climate.\nEnjoy the sunshine!")
elif(we=="cool"):
    print("This is cool climate.\nWear a light jacket.")
elif(we=="cold"):
    print("This is cold climate.\nStay warm and cozy!")
else:
    print("Invalid input. Please enter: hot, warm, cool, or cold.")

