
def is_prime(num1):
    for i in range(2,num1):
        if num1 % i == 0:
            return False
    return True

n = int(input())
if is_prime(n) == True:
    print("prime")
else:
    print("composite")

# 2 = 2
# 3 = 3
# 4 = 2 4 X
# 5 = 5
# 6 = 2 3 6 X
# 7 = 7
# 8 = 2 4 8 X
# 9 = 3 9 X
# 10 = 2 5 10 X
# 11 = 11

# 16 = 4
#
# 2 * 8
# 4 * 4
# 8 * 2