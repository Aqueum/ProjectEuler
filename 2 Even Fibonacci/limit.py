limit = 4000000
a, b, total = 0, 1, 0
while b <= limit:
    a, b = b, a + b
    if a % 2 == 0:
        total += a
print("Result :", total)
