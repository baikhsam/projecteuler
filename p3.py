import math
factors = []
limit = int(math.sqrt(600851475143))
target = 600851475143

for i in range(2, limit+1):
  if target % i == 0:
    factors.append(i)

primefacts = []
check = 0
for num in factors:
  for i in range(2, limit+1):
    if num != i and num % i == 0:
      check += 1
  if check <=0:  
    primefacts.append(num)
print(max(primefacts))
