from sympy import *
# def isPrime(x):
#   y = int(x/2)
#   while y>1:
#     if x % y == 0:
#       return False
#     else:
#       y -= 1
#       print(y)
#   return True
# x = 600851475143

def zeroDP(x):
  if round(x,10) - int(round(x,0)) == 0:
    return int(round(x,0))
  else: 
    return False
  
x = 13195
# if x%2 != 0:
#   y = prevprime(x/2)
# else: 
#   y = prevprime(x)
# while isprime(zeroDP(x/y)) == False and x/y>1:
#   print(y, " ", x/y)
#   y += 1
# print("largest prime factor = ",x/y)

# while x%y!=0:
#   print(y)
#   y=prevprime(y)
# print("largest prime factor = ",y)
y = 2
 
while y<x:
  print(y)
  while x%y != 0 and y<x:  
    # print("not", y)  
    y=nextprime(y)
  y=nextprime(y)
print("largest prime factor = ",y)

