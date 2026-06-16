name = ["Alice", "Bob", "Charlie", "David", "Eve"]
print(name[1])
name[0] = " Brown"
print(name)
name.append("Frank")
print(name)
name.insert(2, "Bathel")
print(name)
name.pop(3)
print(name)
print(name[-1])

cars = ["Toyota", "Honda", "Ford", "Chevrolet", "Nissan", "Hyundai",  "Subaru"]
print(cars[2:5])



countries = ["USA", "Canada", "Mexico", "Brazil", "Argentina", "Chile", "Colombia"]
copy_countries = countries.copy()
print(copy_countries)

for country in countries:
    print(country)

animals = ["Dog", "Cat", "Elephant", "Giraffe", "Lion", "Tiger", "Bear", "Alligator", "Zebra", "Monkey"]
animals.sort()
print("Ascending:", animals)
animals.sort(reverse=True)
print("Descending:", animals)
for animal in animals:
    if "a" in animal.lower():
        print(animal)

first_name = ["John", "Alice", "Bob", "Eve"]
last_name = ["Smith", "Johnson", "Williams", "Brown"]
full_name = first_name + last_name
print(full_name)