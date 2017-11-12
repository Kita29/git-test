def rand(val1):
    import random
    val2 = random.randint(0,10)
    if val1 == val2:
        print("Victory")
    else:
        print("You next variant? ")
        

if __name__ == "__main__":
    val1 = int(input("Enter numeric: "))
    rand(val1)
