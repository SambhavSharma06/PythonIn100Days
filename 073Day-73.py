#Magic/Dunder Methods in Python!!
class Box:
    def __init__(self, *items):
        self.items = list(items)

    def __str__(self):
        return str(self.items)

    def __len__(self):
        return len(self.items)

    def __getitem__(self, i):
        return self.items[i]

    def __add__(self, other):
        return Box(*(self.items + other.items))

    def __eq__(self, other):
        return self.items == other.items

    def __call__(self, item):
        self.items.append(item)


a = Box(1, 2, 3)
b = Box(4, 5)

print(a)
print(len(a))
print(a[0])
print(a + b)
print(a == b)
a(99)
print(a)
