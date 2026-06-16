# Login Authentication Example

username = input("Enter your username: ")
password = input("Enter your password: ")

users = {
    "admin": "password123",
    "user1": "pass1",
    "user2": "pass2"
}

max_attempts = 3
attempts = 0
while attempts < max_attempts:
    if username in users:
        if password == users[username]:
            print("Login successful! Welcome, {}.".format(username))
            break
        else:
            print("Incorrect password. Please try again.")
    else:
        print("Username not found. Please try again.")
    attempts += 1
else:
    print("Username not found. Please try again.")

    