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
x = 13195
y = 2
while isprime(int(x/y)) == False and x/y>28:
  y += 1
  print(y, " ", x/y)  
print("largest prime factor = ",x/y)
print(isprime(29))
print(isprime(29.0))
print(isprime(10/2))