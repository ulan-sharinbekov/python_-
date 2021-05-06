n = int(input())
zero = 0
pos = 0
neg = 0
for i in range(n):
    num1 = int(input("введите число: "))
    if num1 == 0:
        zero+=1
    elif num1 > 0:
        pos +=1
    else:
        neg += 1
print(zero, pos, neg)