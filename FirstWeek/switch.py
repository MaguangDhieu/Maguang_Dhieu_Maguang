#grade = input("Enter your grade (A, B, C, D, F): ")
#match grade:
  #  case grade
light_color = input("Enter a traffic light color (red, yellow, green): ")
match light_color:
    case "red": 
        print("Stop!")
    case "yellow":
        print("Caution! Prepare to stop.")
    case "green":
        print("Go!")
    case _:
        print("Invalid traffic light color.")
        