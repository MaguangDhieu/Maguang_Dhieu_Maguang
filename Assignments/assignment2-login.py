
users = {
        "admin": {"password": "admin123", "role": "Admin"},
        "customer": {"password": "cust123", "role": "Customer"},
        "cashier": {"password": "cash123", "role": "Cashier"}
    }

attempts = 3
while attempts > 0:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in users:
        if password == users[username]["password"]:
            role = users[username]["role"]

            print("\nLogin Successful!")
            print("Welcome,", username)
            print("Role:", role)

            if role == "Admin":
                print("Access: All features available.")
            elif role == "Customer":
                print("Access: Browse products and place orders.")
            elif role == "Cashier":
                print("Access: Process sales and payments.")

            break
        else:
            attempts -= 1
            print(f"Incorrect password! Attempts left: {attempts}")
    else:
        attempts -= 1
        print(f"Username not found! Attempts left: {attempts}")

if attempts == 0:
    print("\nAccount locked! You have used all 3 login attempts, try again in about three hours.")


