morale = 70
strength = 75
injuries = 0

print(" FIFA World Cup 2026 Simulation ")
print("You are the manager of a national football team.\n")

# Pre-Tournament Preparation
while True:
    print("\nPre-Tournament Preparation")
    print("1. Intensive Training")
    print("2. Friendly Match")
    print("3. Recovery Session")
    print("4. Start Tournament")

    choice = input("Choose an activity: ")

    if choice == "1":
        strength += 5
        injuries += 10
        print("Team trained hard! Strength increased.")
    elif choice == "2":
        morale += 5
        print("Friendly match played. Morale increased.")
    elif choice == "3":
        injuries = max(0, injuries - 10)
        print("Players recovered. Injuries reduced.")
    elif choice == "4":
        break
    else:
        print("Invalid choice.")

print("\n GROUP STAGE")

for match in range(1, 4):

    if injuries >= 50:
        print(f"Match {match}: Too many injuries! Match skipped.")
        continue      

    print(f"\nGroup Match {match}")
    result = input("Result (win/draw/loss): ").lower()

    if result == "win":
        morale += 10
        strength += 2
    elif result == "draw":
        morale += 2
    elif result == "loss":
        morale -= 10
    else:
        print("Invalid input. Match counted as draw.")

    print(f"Morale: {morale}, Strength: {strength}, Injuries: {injuries}")

    if morale <= 20:
        print("Team morale collapsed. Eliminated from tournament.")
        break

else:
    print("\nQualified for Knockout Stage!")


    stages = [
        "Round of 16",
        "Quarter-final",
        "Semi-final",
        "Final"
    ]

    for stage in stages:

        print(f"\n {stage}")

  
        pass

        result = input("Result (win/loss): ").lower()

        if result == "win":
            morale += 5
            print(f"You won the {stage}!")
        else:
            print(f"You lost in the {stage}.")
            break       
    else:
        print("\n🏆 Congratulations! You won the 2026 FIFA World Cup!")

print("\nSimulation Ended.")