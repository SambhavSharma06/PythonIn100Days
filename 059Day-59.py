#Decorators in Python!!

#SIMPLE
# def greet(fx):
#  def mfx():
#      print("Good Morning")
#      fx()
#      print("Thanks for using the function")
#  return mfx()
#
# @greet
# def hello():
#     print("Hello World")
#
# def add(a, b):
#     print(a+b)
#
# # greet(hello)()
# hello()

#COMPLEX FOR ARGUMENTS

def greet(fx):
    def mfx(*args, **kwargs):
        print("Good morning")
        fx(*args, **kwargs)
        print("Thanks for using this function")
    return mfx

@greet
def hello():
    print("Hello world")

@greet
def add(a,b):
    print(a+b)

#greet(hello)()
hello()
# greet(add(1,2))
add(1,2)