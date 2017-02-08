a = 1
b = 1
totalSum = 0
while a <= 4000000:
  if a % 2 == 0:
    totalSum += a
  b = a + b
  a = b - a
print(totalSum)
