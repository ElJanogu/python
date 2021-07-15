myList1 = [1, 6, 3, 6, 8, 9]
myList2 = ["This", "is", "a", "list"]

print(len(myList1))
print(len(myList2))

print(myList1[2])
print(myList2[3])

print(myList1)
print(myList2)

myList3 = [3, True, "Hallo"]
print(myList3)

a = myList1[1]
b = myList2[-2]

c = myList1[2:-1]
d = myList1[2:]
e = myList1[:-3]

print(a)
print(b)

print(c)
print(d)
print(e)

if 3 in myList1:
    # code
    pass

myList1[0] = 23
myList1[2:4] = [-17, 22]
myList2[3] = ["Another", "Funny", "List"]

print(myList1)
print(myList2)
print(myList3)

myList3.insert(1, False)
myList1.append(54)

print(myList1)
print(myList3)

myList1.extend(myList2)

print(myList1)

myList1.remove(6)
myList3.pop(1)
myList2.pop()

print(myList1)
print(myList2)
print(myList3)

del myList3[1]
del myList3

myList1.clear()

for a in myList2:
    # code
    pass

for i in range(len(myList2)):
  print(myList2[i])

i = 0
while i < len(myList2):
  print(myList2[i])
  i = i + 1