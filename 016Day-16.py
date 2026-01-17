#Match Case Statements in Python!!
Grade = input("Enter your Grade: ")
match Grade:
    case "A":
        print("70% and above")
    case "B":
        print("60% to 69%")
    case "C":
        print("50% to 59%")
    case _:
        print("Fail") 
        
    