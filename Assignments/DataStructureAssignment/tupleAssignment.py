x =("samsung","iphone","tecno","redmi")
print(x[0])
print(x[-2])
phones = list(x)
phones[1] ="itel"
x= tuple(phones)
print(x)
x = x + ("Huawei",)
print(x)
for phone in x:
    print(x)
phones = list(x)
phones.pop(0)
x = tuple(phones)
print(x)

cities =tuple(["Kampala","Gulu","Lira","Adjumani","Arua","Mukono"])
print(cities)

c1, c2, c3, c4, c5, c6  = cities
print(c1, c2, c3, c4, c5, c6)

print(cities[1:4])

first_name =("Abraham" , "Maguang")
last_name =("Dhieu", "Ajak")
full_name = first_name + last_name
print(full_name)
print(len(full_name))


colors = ("red", "green", "blue", "yellow", "orange")
print(colors *3)

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(8)
print(x)


