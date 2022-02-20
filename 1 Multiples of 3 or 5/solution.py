# a function that takes arguments number and divisor
# and returns true if number is multiple of divisor
# otherwise false
def multiple(number, divisor):
  if number % divisor == 0:
    return True
  else:
    return False

print(multiple(5,2))