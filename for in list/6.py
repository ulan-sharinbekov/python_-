s = input().split()
for i in range(len(s)):
    if int(s[i]) % 2 == 0:
        print(s[i], end=" ")