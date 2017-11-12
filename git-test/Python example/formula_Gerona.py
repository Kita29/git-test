def formula_Gerona(side1, side2, side3):
    import math
    p = (side1 + side2 + side3) / 2
    s = math.sqrt(p * (p - side1) * (p - side2) * (p - side3))
    return s

if __name__ == "__main__":
    side1 = float(input("Enter the side1 triangle: "))
    side2 = float(input("Enter the side2 triangle: "))
    side3 = float(input("Enter the side3 triangle: "))
    print("The square = ", formula_Gerona(side1, side2, side3))
