import math
running = True
n = 2
limit = 2000000
list = []
while(running):
  check = 0
  for i in range(2, int(math.sqrt(limit)+1)):
    if n != i and n % i == 0:
      check += 1
  if check == 0:
    #number is prime
    list.append(n)  
  if len(list) == limit - 1:
    running = False
    break
  n += 1
print(sum(list))
