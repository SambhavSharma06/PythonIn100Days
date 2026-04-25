# FunctionTools in Python!!

# def cube(x):
#     return x*x*x
#
# # print(cube(2))
#
# l = [1,2,4,6,4,3]
# # newl = []
# # for item in l:
# #     newl.append(cube(item))
# # print(newl)
# #MAP
# # newl = list(map(cube,l))
# # print(newl)
#
# newl = list(map(lambda x:x*x*x,l))
# print(newl)
#
# #Filter
# def filter_function(a):
#     return a > 4
#
# newnewl = list(filter(filter_function,l))
# print(newnewl)
#REDUCE
from functools import reduce
#List of Numbers
numbers = [1,2,3,4,5]
#Calculate the sum of the numbers using the reduce function
def mynumber(x,y):
  return x + y
sum = reduce(mynumber,numbers)
#print the sum
print(sum)
