COUPONS = {
    "SAVE10": 5,
    "SAVE20": 10,
    "VIP30": 15
}

subtotal = float(input("Enter subtotal amount (UGX): "))

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
print(f"Subtotal             :  UGX {subtotal:,.0f}")
print(f"Subtotal Discount    :  UGX {discount_amount:,.0f}")
print(f"Coupon Discount      :  UGX {coupon_amount:,.0f}")
print(f"Amount After Discount:  UGX {after_coupon:,.0f}")
print(f"Tax ({tax_rate}%)     :  UGX {tax_amount:,.0f}")
print(f"FINAL PRICE          :  UGX {final_price:,.2f}")


