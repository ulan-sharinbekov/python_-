s = input().split()
nums = []
for i in s:
    nums.append(int(i))
n = int(input())

swt = False
for i in range(len(nums)):
    if n > nums[i]:
        print(i+1)
        swt = True
        break
if swt == False:
    print(len(nums)+1)


