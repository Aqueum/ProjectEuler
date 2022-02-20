from operator import truediv


def multiple(number, divisor):
  if number % divisor == 0:
    return True
  else:
    return False

print(multiple(5,2))