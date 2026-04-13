# Generators in Python!!

def gen():
    for i in range(1, 10):
        if i % 2 == 0:
            yield i

g = gen()
#It will print one by one!!
print(next(g))
print(next(g))
print(next(g))
print(next(g))
