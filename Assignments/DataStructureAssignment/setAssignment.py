beverages = set(("tea", "coffee", "water", "milk"))
print(beverages)
beverages.update([ "soda", "juice"])
print(beverages)

mySet = {"oven", "kettle", "microwave", "refrigerator"}
print(mySet)
if "microwave" in mySet:
    print("Microwave found!")
else:
    print("Microwave not found")
    mySet = {"oven", "kettle", "microwave", "refrigerator"}
    mySet.remove("kettle")
    print(mySet)
for item in mySet:
    print(item)

fruits = {"Apple", "Banana", "Orange", "Mango"}
more_fruits = ["Pineapple", "Grapes"]
fruits.update(more_fruits)
print(fruits)


ages = {20, 21, 22}
first_names = {"Abraham", "John", "Mary"}
combined_set = ages.union(first_names)
print(combined_set)