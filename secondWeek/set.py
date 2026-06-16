cars = {"Toyota", "Honda", "Ford", "Chevrolet"}
print(cars)
print((type(cars)))

name = {"John", "Alice", "Bob", "Eve",100, 200, 300, 400, 500}
print(name)
print((type(name)))


letters = {"a", "b", "c", "d", "e","a", "b", "c", "d", "e"}
print(letters)
print((type(letters)))


names = {"John", "Alice", "Bob", "Eve",100, 200, 300, 400, 500}
print(names)
print((type(names)))
names.add("Charlie")
print(names)
names.remove("Eve")
print(names)
numbers = {1, 2, 3, 4, 5}
print(numbers)
numbers.add(6)
print(numbers)
numbers.remove(3)
print(numbers)
numbers.clear()
print(numbers)
del numbers

age = {23,25,60, 34, 45,"john"}
student = {"John", "Alice", "Bob", "Eve"}
w= age.union(student)
print(w)
x = age.intersection(student)
print(x)
y = age.difference(student)
print(y)
z = age.symmetric_difference(student)
print(z)
age.update(student)
print(age)
age.intersection_update(student)
print(age)
age.difference_update(student)
print(age)
age.symmetric_difference_update(student)
print(age)

