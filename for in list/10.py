s = input().split()
nums = []
for i in s:
    nums.append(int(i))
cnt = 0
for i in range(1,len(nums)-1):
    if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
        cnt += 1
print(cnt)
# print(s)
# print(nums)
