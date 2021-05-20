list1 = ["Derbes", "Azamat", "Dauren","Dana","Derbes", "Derbes","Dias"]

set1 = set(list1)
for i in set1:
    if list1.count(i) > 1:
        print(i)