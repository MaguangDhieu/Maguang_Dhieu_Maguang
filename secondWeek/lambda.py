numbers = [4,5,7,3,8,9,22,11,35]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)
greater_than_10 = list(filter(lambda x: x > 10, numbers))
print(greater_than_10)
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

fruit = ["Cherry", "Banana", "Apple", "Date", "Fig","Guava","manago"]
short = list(filter(lambda x: len(x) < 5, fruit))
print(short)
long = list(filter(lambda x: len(x) > 5, fruit))
print(long)

fruit = ["Cherry", "Banana", "Apple", "Date", "Fig","Guava","manago"]
sorted_by_length = sorted(fruit, key=len)
print(sorted_by_length)

sorted_by_length_desc = sorted(fruit, key=len, reverse=True)
print(sorted_by_length_desc)