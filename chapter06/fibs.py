fibs = [0, 1]
for i in range(0, 8):
    fibs.append(fibs[-2] + fibs[-1])
print(fibs)
print()

fibs.clear()
nums = []
for i in range(0, 11):
    nums.append(i)
    if i <= 1:
        fibs.append(i)
        continue
    fibs.append(fibs[i-1] + fibs[i-2])
print(nums)
print(fibs)
    