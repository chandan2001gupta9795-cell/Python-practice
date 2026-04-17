list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

common = False

for i in list1:
    if i in list2:
        common = True
        break

if common:
    print("Lists share common elements")
else:
    print("Lists have no common elements")