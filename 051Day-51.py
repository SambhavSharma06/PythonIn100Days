#Tell,Seek and truncate in Python!!

# with open('Day-51.0.txt','r') as file:
#     print(type(file))
#     file.seek(10)
#     print(file.tell())
#     data = file.read(5)
#     print(data)

with open('Day-51.1.txt','w') as f:
    f.write('Hello World')
    f.truncate(5)

with open('Day-51.1.txt','r') as f:
    print(f.read())

