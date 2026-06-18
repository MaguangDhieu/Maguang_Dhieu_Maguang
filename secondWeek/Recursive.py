def factorial (n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
#print(factorial(5))
#number = int(input("Enter a number: "))
#result = factorial(number)
#print("The factorial of", number, "is", result)


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)
#print(factorial(5))
#number = int(input("Enter a number: ")) 
#print("The factorial of", number, "is", factorial(number))

def count_down(n):
    if n == 0:
        print("Finished!")
    else:
        print(n)
        count_down(n-1)
count_down(7)


def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
#print(fibonacci(10))
#number = int(input("Enter a number: "))
#print("The Fibonacci number at position", number, "is", fibonacci(number))

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for i in range(10):
 #print(fibonacci(i))

#print(fibonacci(10))


 def binary_search(arr, target, left,right):
    if left > right:
        return -1
    mid = (left + right) 
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, right)
    else:
        return binary_search(arr, target, left, mid - 1)
    sorted_list = [1,3,5,7,9,11,13,15,17,19]
    print(binary_search(sorted_list, 11, 0, len(sorted_list) - 1))