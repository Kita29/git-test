def operator_if():
    pH = input("Enter value pH: ")
    if len(pH) > 0:
        pH = float(pH)
        if pH > 0:
            if pH == 5.0:
                print(pH, "Coffee")
            if pH == 8.0:
                print(pH, "Water")
            elif 7.36 < pH < 7.44:
                print(pH, "Blood")
            else:
                print("I don't know")
        else:
            print("Incorrect")
    else:
        print("It's empty")
