def operator_if():
    pH = input("Enter value pH: ")
    if len(pH) > 0:
        pH = float(pH)
        if pH > 0:
            if pH == 5.0:
                print(pH, "Coffee")
            elif pH == 8.0:
                print(pH, "Water")
            elif pH == 3.0:
                print(pH, "Apple juice")
            elif pH == 5.5:
                print(pH, "Shampoo")
            elif 7.36 < pH < 7.44:
                print(pH, "Blood")
            elif 9.0 < pH < 10.0:
                print(pH, "Soap")
            else:
                print("I don't know")
        else:
            print("Incorrect")
    else:
        print("It's empty")
