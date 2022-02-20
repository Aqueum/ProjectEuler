# a function that takes arguments number and divisor
# and returns true if number is multiple of divisor
# otherwise false
def multiple(number, divisor):
  if number % divisor == 0:
    return True
  else:
    return False

x = 0
y = 0
while x < 10:
  if multiple(x,3) or multiple(x,5):
    y += x
  x += 1

print(y)