year = int(input())

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("YES")
else:
    print("NO")

# and (*)
# 0 0 =>0
# 1 0 =>0
# 0 1 =>0
# 1 1 =>1
#
# or (+)
# 0 0 => 0
# 1 0 => 1
# 0 1 => 1
# 1 1 => 1
#
