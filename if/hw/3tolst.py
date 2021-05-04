m1 = int(input())
m2 = int(input())
m3 = int(input())

if (m1 > 94 and m1 < 727) and (m2 > 94 and m2 < 727) and (m3 > 94 and m3 < 727):
    if m1 >= m2 and m1 >=m3:
        print(m1)
    elif m2>=m3 and m2 >= m1:
        print(m2)
    else:
        print(m3)
else:
    print("Error")