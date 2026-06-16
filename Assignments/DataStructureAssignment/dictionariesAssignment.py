Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}

print("Shoe size:", Shoes["size"])

Shoes["brand"] = "Adidas"

print(Shoes)

Shoes["type"] = "sneakers"
print("Keys:", list(Shoes.keys()))

print("Values:", list(Shoes.values()))

print("size" in Shoes)

for key, value in Shoes.items():
    print(key, ":", value)

Shoes.pop("color")
print(Shoes)

Shoes.clear()
print(Shoes)

student = {"name": "Abraham", "course": "Computer Science"}
student_copy = student.copy()
print(student_copy)

students = {
    "student1": {
        "name": "John",
        "age": 20
    },
    "student2": {
        "name": "Mary",
        "age": 21
    },
    "student3": {
        "name": "Abraham",
        "age": 22
    }
}

print(students)
print(students["student1"]["name"])
print(students["student1"]["age"])
print(students["student2"]["name"])
print(students["student2"]["age"])
print(students["student3"]["name"])
print(students["student3"]["age"])

