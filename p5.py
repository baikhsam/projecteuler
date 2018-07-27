end = True
n = 1
lower = 1
upper = 20
nums = -1

for n in range(lower, 232792561):
  check = 0
  for m in range(lower, upper + 1):
    if n % m != 0:
      check += 1
  if check == 0:
    nums = n
    break
print(nums)
