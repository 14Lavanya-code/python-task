print("          login system")
print("---------------------------")
c_username = "user"
c_password = "0987"
username = input("Enter username: ")

if username == c_username:
    password = input("Enter password: ")
    if password ==c_password:
        print("Login successful! Welcome,", username)
    else:
        print("Incorrect password. Access denied.")
else:
    print("Username not found.")