import math
running = True
n = 2
list = []
while(running):
  check = 0
  for i in range(2, int(math.sqrt(10001*350)+1)):
    if n != i and n % i == 0:
      check += 1
  if check == 0:
    #number is prime
    list.append(n)  
  if len(list) == 10001:
    running = False
    break
  n += 1
print(list[10001])
