s = input().split()
nums = []
for i in s:
    nums.append(int(i))

mn = 1001
for i in nums:
    if i < mn and i > 0:
        mn = i
print(mn)
