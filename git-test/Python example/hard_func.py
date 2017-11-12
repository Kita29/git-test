def hard_func():
    x = float(input("Enter x = "))
    y = float(input("Enter y = "))
    import math
    z = (x + ((2 + y) / (x**2))) / (y + (1 / (math.sqrt((x**2) + 10))))
    q = 2.8 * math.sin(x) + math.fabs(y)
    print("z = ", round(z, 2), " q = ", round(q,2) )

