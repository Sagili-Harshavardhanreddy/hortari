from collections import Counter
list1 = a = [int(x) for x in input().split()]
#list1 = [3,6,4,4,5,5,7,7]
list2 = dict(Counter(list1))
print(list2)
list3 = []
list4 = []
for key in list2:
    if(list2[key] == 1):
        print("{}".format(list2[key]))
        list3.append(key)


list1.sort()
print(list1)

for i in list3:
    if i in list1:
        list1.remove(i)
        

list1.sort()
list3.sort()

list3.extend(list1)

print(list3)
