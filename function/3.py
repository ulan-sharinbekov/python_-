def min4(num1, num2, num3, num4):
    a = min2(num1, num2) #4
    b = min2(num3, num4) #6
    return min2(a,b) #4

def min2(num1, num2):
    if num1 > num2:
        return num2
    else:
        return num1

s = input().split()
a = int(s[0])
b = int(s[1])
c = int(s[2])
d = int(s[3])

print(min4(a,b,c,d))