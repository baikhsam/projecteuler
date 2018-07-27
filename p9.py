a = 0
b = 0
c = 0 
answer = 1
for i in range(1, 200):
  for j in range(1, 200):
    for k in range(1, 200):
      if k ** 2 == i ** 2 + j ** 2:
        if k + i + j == 1000:
          answer = k * i * j
print(answer)
