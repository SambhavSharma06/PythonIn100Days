#Read,Write and Open in Python!!

# f = open('Day-49.0.txt','r')
# print(f.read())
# f.close()

# f = open('Day-49.1.txt','w')
# print(f.write)
# f.close()

# f = open('Day-49.0.txt','w')
# f.write('Hello World')
# f.close()

# f = open('Day-49.0.txt','a')
# f.write('Hello,world!')
# f.close()

with open('Day-49.0.txt','a') as f:
    f.write("Hey I am inside with")
