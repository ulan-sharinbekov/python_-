# Задача №3062. Утренняя пробежка

# 10
# 11
# 12.1
# 13.31
# 14.641
# 16.1051
# 17.71561
# 19.48
# 21.43

x = int(input())
y = int(input())

cnt = 1
while x < y:
    print(x)
    x = x * 1.1

    cnt+=1
print(cnt)