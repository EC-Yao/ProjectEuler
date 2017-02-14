max = 0;

for a in range(100, 999):
  for b in range(a, 999):
    if (str(a*b))[::-1] == str(a * b):
      if a * b > max:
        max = a * b
        
print(max)
