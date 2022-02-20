x = 1
y = 2
z = y
while x < 4000000:
  next = x + y
  x = y
  y = next
  if next < 4000000 and next % 2 == 0:
    print(next)
    z += next
print("answer = ", z)