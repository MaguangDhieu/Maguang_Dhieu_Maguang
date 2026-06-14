bill = float(input("Enter total bill amount ($): "))
people = int(input("Enter number of people: "))

if bill <= 0 or people <= 0:
    print("Error: Bill amount and number of people must be greater than 0.")
else:
    print("\nTip Options")
    print("1. 10%")
    print("2. 15%")
    print("3. 20%")
    print("4. Custom")

    choice = input("Choose a tip option (1-4): ")

    if choice == "1":
        tip_percent = 10
    elif choice == "2":
        tip_percent = 15
    elif choice == "3":
        tip_percent = 20
    elif choice == "4":
        tip_percent = float(input("Enter custom tip percentage: "))
    else:
        print("Invalid choice. Default tip of 10% applied.")
        tip_percent = 10

 
    tip_amount = bill * tip_percent / 100
    total_bill = bill + tip_amount
    per_person = total_bill / people

    print("\n      BILL RECEIPT  ")
    print(f"Bill Amount      : ${bill:.2f}")
    print(f"Tip Percentage   : {tip_percent}%")
    print(f"Tip Amount       : ${tip_amount:.2f}")
    print(f"Total Bill       : ${total_bill:.2f}")
    print(f"Number of People : {people}")
    print(f"Amount Per Person: ${per_person:.2f}")
   