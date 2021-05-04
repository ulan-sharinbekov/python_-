t11 = int(input())
t21 = int(input())
t12 = int(input())
t22 = int(input())
t13 = int(input())
t23 = int(input())
t14 = int(input())
t24 = int(input())

t1total = t11 + t12 + t13 + t14
t2total = t21 + t22 + t23 + t24

if t1total > t2total:
    print(1)
elif t1total < t2total:
    print(2)
else:
    print("DRAW")
