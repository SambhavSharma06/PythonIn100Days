#Dictionaries in Python!!

dic = {
    "name":"Harry",
    "age":20,
}

print(dic)
print(dic["name"])
print(dic["age"])
print(dic.keys())
print(dic.values())

for key in dic.keys():
    print(key)

for value in dic.values():
    print(value)

for key, value in dic.items():
    print(key)