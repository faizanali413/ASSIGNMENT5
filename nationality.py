age = int(input("Enter your age: "))
if age >= 18:
    nationality = input("Do you have Pakistani nationality? (yes/no): ").strip().lower()
    
    if nationality == "yes":
        print("You are eligible to vote.")
    elif nationality == "no":
        print("Please obtain a valid ID to vote.")
    else:
        print("Invalid input for nationality.")
else:
    print("You are not eligible to vote as you are under 18.")
