import math 
pie = math.pi
print("value of pi:", pie)

#external modules like pandas, numpy, scipy

import pandas

data ={
    "Name":( "John", "Pter","Simon"),
    "Age": (21, 23, 32)
}
print ("data")
df = pandas.DataFrame(data)
print(df)

  
from math import pi
print(pi)
#importing modules with aliases
import math as m
result = m.sqrt(16)
print("Square root of 16:", result)

#importing everything from a module
from math import *
print (pi)
print(factorial(8))