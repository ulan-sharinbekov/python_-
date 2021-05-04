# Задача №3058. Минимальный делитель

n = int(input())

div = 2
#
# while n % div != 0:
#     div+=1
#
# print(div)


while True:
    if n % div == 0:
        break
    div+=1
print(div)