firstname = input("What is your first name? ")
lastname = input("What is your last name? ")
birth_year = int(input("What year were you born? "))
current_year = int(input("What is the current year? "))
age = current_year - birth_year
city =input("What city do you live in? ")
print(f"Hello, {firstname} {lastname}! You are {age} years old.")
print(f"You live in {city}.")