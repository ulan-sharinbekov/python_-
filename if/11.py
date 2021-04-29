a = int(input())
b = int(input())
c = int(input())

mx = 0
mn = 0

if a >= b and a >= c:
    mx = a
elif b >= a and b >= c:
    mx = b
else:
    mx = c

if a <= b and a <= c:
    mn = a
elif b <= a and b <= c:
    mn = b
else:
    mn = c

print(mx - mn)