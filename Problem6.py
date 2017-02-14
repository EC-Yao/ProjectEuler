squareSums = 0
sumSquares = 0

for a in range(1, 101):
  sumSquares += a * a
  squareSums += a

squareSums *= squareSums
print(abs(sumSquares - squareSums))
