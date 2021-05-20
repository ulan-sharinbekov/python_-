s = input().split()
nums = []
for i in s:
    nums.append(int(i))
mn = 0
for i in nums:
    if i % 2 == 1 and mn == 0:
        mn = i
    elif i % 2 == 1 and i < mn:
        mn = i
print(mn)