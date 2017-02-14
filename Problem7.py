listPrimes = [2]

for a in range(3, 10000000):
  isPrime = True
  for b in range(0, len(listPrimes)):
    if a % listPrimes[b] == 0:
      isPrime = False
  if isPrime:
    listPrimes.append(a)
  if len(listPrimes) > 10000:
    break
    
print(listPrimes[10000])
