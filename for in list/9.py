s = input().split()
for i in range(len(s)-1):
    if int(s[i]) > 0 and int(s[i+1]) > 0:
        print(s[i], s[i+1])
        break
    elif int(s[i]) < 0 and int(s[i+1]) < 0:
        print(s[i], s[i+1])
        break

a = [int(i) for i in input().split()]
for i in range(1, len(a)):
    if a[i - 1] * a[i] > 0:
        print(a[i - 1], a[i])
        break
