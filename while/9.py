# Задача №3059. Список степеней двойки

n = int(input())

power = 0

while 2**power <= n:
    print(2**power, end=" ")
    power+=1
