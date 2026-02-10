# Tuple's methods in Python!!
Numbers = (1,2,3,4,5,6,7,8,9,10)
ListNo = list(Numbers)
ListNo.append(11)
ListNo.pop(0)
ListNo[3] = 15
print(ListNo)

Tut1 = (1,2,3,3,3)
Tut2 = (4,5,6)

Tut3 = Tut1 +Tut2
print(Tut3)

print(Tut3.count(3))

Tut1.index(3,4,5)

res = len(Tut3)
print(res)