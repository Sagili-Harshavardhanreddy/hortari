from collections import Counter
list1 = list(input("enter an array:"))
list2 = dict(Counter(list1))
print(list2)
list3 = []
for key in list2:
    if list2[key] > 1:
        print("{}".format(list2[key]))
        list3.append(key)

list2 = list(set(list2))
for i in list3:
    if i in list2:
        list2.remove(i)

print(list2)
