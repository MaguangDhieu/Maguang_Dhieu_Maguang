def greet():
    print("Hello, welcome to the world of Python programming!")
greet()
def square_number():
    number = 5
    squared = number * number
    print(squared)


square_number()


def rectangle_area():
    length = int(input("Enter the length of the rectangle: "))
    width = int(input("Enter the width of the rectangle: "))
    area = length * width
    print("The area of the rectangle is:", area)
rectangle_area()


def hello_name(name):
    print("My name is " + name)
hello_name("John")

def display(name,age):
    print(name)
    print(age)
display("Alice", 30)
    


def add_numbers(num1, num2):
    return num1 + num2
result = add_numbers(5, 10)
print(result)


