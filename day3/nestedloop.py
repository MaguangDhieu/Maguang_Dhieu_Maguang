#for i in range(2):
 #   print(i)
   # for j in range(10, 14):
       # print( j)

#x = [1, 2]
#y = [10, 11]
#for i in x:
           # for j in y:
               # print(f" {i}  {j}")



for i in range(2, 4):
    for j in range(1, 14):
        if i==j:
            continue
        print(i, "*", j, "=", i * j)
        print()