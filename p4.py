end = True
dromes = []
for i in range(100,1000):
  for j in range(100,1000):
    num = i * j
    flipped = int(str(num)[::-1])
    if num == flipped:
      dromes.append(num)
print(max(dromes))
