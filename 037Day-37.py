#Finally keyword in Python !!
def func1():
    try:
        l = [1, 5, 6, 7]
        i = int(input("Enter a index: "))
        print(l[i])
        return 1
    except:
        print("Index out of range")
        return 0


    finally:
      print("Ending program")
# print("I am always executed")

x = func1()
print(x)
#FINALLY WILL EXECUTE EVEN IF THE FUNCTION/METHOD WILL RETURN A VALUE OR NOT OR ANYTHING HAPPENS.