try:

    n = int("int")
    res = n/0

except ZeroDivisionError:
    print("Can not be divided by zero !")
except ValueError:
    print("Enter a valid value")
else:
    print("Result:", res)
    

finally:
       print("Execution is complete")
