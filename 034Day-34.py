#Dictionary Methods in Python

ep1 = {122:45,123:89,567:69,670:69}

ep2 = {222:67,566:90}

# ep1.update(ep2)
# print(ep1)
# # DIC IS ORDERED!!
#
# ep1.clear()
# ep1.pop(122)
# print(ep1)
ep1.popitem()#Last keyword will go.
# print(ep1)
# del ep1
del ep1[122]
print(ep1)

