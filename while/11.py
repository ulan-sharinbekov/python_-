# n = int(input())
#
# power = 0

# while True:
#     if n == 2**power:
#         print("YES")
#         break
#     elif n > 2**power:
#         power += 1
#     elif n < 2**power:
#         print("NO")
#         break

n = int(input())
swt = False
i = 1
while i <= n:
    if i == n:
        swt = True
        break
    else:
        i*=2

if swt == True:
    print("YES")
else:
    print("NO")
