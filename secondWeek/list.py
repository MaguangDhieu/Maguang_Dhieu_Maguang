a = [1, 2, 3, 4, 5]
print(a)
print(type(a))
b = ["apple", "banana", "cherry", "date", "elderberry"]
print(b)    
print(type(b))
c = [1, "apple", 3.14, True, None]
print(c)
print(type(c))
print(a[0])
print(b[1])
print(c[2])
print(a[-1])
print(b[-2])
print(c[-3])
b.append("fig")
print(b)
b.insert(2, "grape")
print(b)
b[2] = "kiwi"
print(b)