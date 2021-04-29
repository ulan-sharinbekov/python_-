a = int(input())
b = int(input())
c = int(input())

# if a >= b and a >= c:
#     print(a)
# elif b >= a and b >= c:
#     print(b)
# else:
#     print(c)
#
# d = a
# if d < b:
#     d = b
# if d < c:
#     d = c
#
# print(d)

d = 0
if a > b:
    d = a
else:
    d = b

if d > c:
    print(d)
else:
    print(c)