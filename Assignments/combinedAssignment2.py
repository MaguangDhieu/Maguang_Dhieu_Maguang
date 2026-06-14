users = {
    "admin": {"password": "admin123", "role": "Admin"},
    "customer": {"password": "cust123", "role": "Customer"},
    "cashier": {"password": "cash123", "role": "Cashier"}
}

attempts = 3
logged_in = False

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

            logged_in = True
            break

        else:
            attempts -= 1
            print(f"Incorrect password! Attempts left: {attempts}")

    else:
        attempts -= 1
        print(f"Username not found! Attempts left: {attempts}")

if not logged_in:
    print("\nAccount locked! You have used all 3 login attempts.")
    exit()

COUPONS = {
    "SAVE5": 5,
    "SAVE10": 10,
    "VIP15": 15
}

subtotal = float(input("\nEnter subtotal amount (UGX): "))


if subtotal >= 100000:

    if subtotal >= 500000:
        discount_rate = 15

    elif subtotal >= 200000:
        discount_rate = 10

    else:
        discount_rate = 5

else:
    discount_rate = 0

discount_amount = subtotal * discount_rate / 100
after_discount = subtotal - discount_amount

print(f"\nSubtotal Discount Applied: {discount_rate}%")


coupon = input("Enter Coupon Code (Press Enter to Skip): ").strip().upper()

coupon_discount = 0

if coupon != "":

    if coupon in COUPONS:
        coupon_discount = COUPONS[coupon]
        print(f"Valid Coupon: {coupon} ({coupon_discount}% Off)")
    else:
        print("Invalid Coupon Code!")

else:
    print("No Coupon Applied.")

coupon_amount = after_discount * coupon_discount / 100
after_coupon = after_discount - coupon_amount

location = input(
    "\nEnter Location (Uganda/Kenya/Tanzania/Rwanda): "
).strip().capitalize()

if location == "Uganda":
    tax_rate = 18

elif location == "Kenya":
    tax_rate = 16

elif location == "Tanzania":
    tax_rate = 15

elif location == "Rwanda":
    tax_rate = 20

else:
    tax_rate = 18
    print("Unknown Location! Default Tax Rate Applied.")

tax_amount = after_coupon * tax_rate / 100
final_price = after_coupon + tax_amount

print("\n               RECEIPT")
print(f"Customer/User       : {username}")
print(f"Role                : {role}")
print(f"Subtotal            : UGX {subtotal:,.0f}")
print(f"Subtotal Discount   : UGX {discount_amount:,.0f}")
print(f"Coupon Discount     : UGX {coupon_amount:,.0f}")
print(f"Amount After Discount: UGX {after_coupon:,.0f}")
print(f"Tax ({tax_rate}%)           : UGX {tax_amount:,.0f}")
print(f"FINAL PRICE         : UGX {final_price:,.2f}")


