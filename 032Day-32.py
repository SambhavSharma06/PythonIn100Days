#Set Methods in Python!!

s1 = {1,2,5,6}
s2 = {2,5,6}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
s1.update(s2)
print(s1,s2)
print(s1.symmetric_difference(s2))
print(s1.issuperset(s2))
print(s1.issubset(s2))
s1.add(7)
s1.remove(7)
#Remove....Error
#Discard.....WithoutError
del s1
#print(s1) Will not gonna work!!
