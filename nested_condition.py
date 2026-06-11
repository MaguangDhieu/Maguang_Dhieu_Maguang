#Nested ConditionExample

#what is nested condition?
#Nested condition is a condition that is inside another condition. It is also known as a nested
#If statement is a conditional statement that is used to execute a block of code if a condition is true. It can also be used to execute a block of code if a condition is false using the else statement. The elif statement is used to check multiple conditions.
#write a program for Login Authentication that takes a username

username = input("Enter your username: ")
password = input("Enter your password: ")

if username == "admin":
    if password == "password123":
        print("Login successful! Welcome, admin.")
    else:
        print("Incorrect password. Please try again.")
else:
    print("Username not found. Please try again.")
    