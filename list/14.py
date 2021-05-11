list1 = [1,6,4,8,1,3,13.5,123.0]
list2 = ["acd", "gmfdk", "abc"]

list1.sort()
print(list1)

list3 = [[1, 2, 3],
         [4, 5, 6, 6, 4],
         [7, 8, 9, 6]
        ]
list3.sort(key=len)
print(list3)