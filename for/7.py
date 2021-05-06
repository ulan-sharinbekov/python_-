n = int(input())

mn = 0
for i in range(n, 1, -1):

    if n % i == 0:
        mn = i
        # print(mn)
print(mn)


