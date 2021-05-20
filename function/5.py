def election(num1,num2,num3):
    if num1 + num2 + num3 > 1:
        return 1
    return 0

a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
print(election(a,b,c))
# 1 1 1 = 3
# 1 1 0 = 2
# 1 0 0 = 1
# 0 0 0 = 0
