import math

numbers = set(range(math.ceil(math.sqrt(600851475143)) , 1, -1))
primes = []

while numbers:
  p = numbers.pop()
  primes.append(p)
  numbers.difference_update(set(range(p * 2, math.ceil(math.sqrt(600851475143)) + 1, p)))

for a in range(0, len(primes) - 2):
  if 600851475143 % primes[len(primes) - 1 - a] == 0:
    print(primes[len(primes) - 1 - a])
    break
