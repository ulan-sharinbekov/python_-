s = input().split()
nums = []
for i in s:
    nums.append(int(i))

mx = nums[0]
index = 0
for i in range(len(nums)):
    if mx < nums[i]:
        mx = nums[i]
        index = i

print(mx, index)
