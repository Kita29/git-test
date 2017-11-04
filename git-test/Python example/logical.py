def logical():
    y = 6>8
    print("y = 6>8 ", y)
    print("not y ", not y)
    print("not None ", not None)
    print("not 2 ", not 2)
    print("2>4 and 45>3 ", 2>4 and 45>3) # logical statement
    print("'' and 2 ", '' and 2) # object
    x = 0
    print("-5 < x < 10 ", -5 < x < 10) # x > -5 and x < 10
    x = 5 < 10
    y = 2 > 3
    print("x = 5 < 10 \ny = 2 > 3 \nx or y ", x or y)
    print("(x or y) + 6 = ", (x or y) + 6)
    val = int(input("Enter numeric: "))
    print("Result 1/x = ", val and 1/val) # if two numiric is true return right object
    print("L = ", ord('L'))
    print("Ф = ", ord('Ф'))
    print("A = ", ord('A'))
    print("Symbol a included in string abc?", 'a' in 'abc')
    print("Symbol A included in string abc?", 'A' in 'abc')
    print("Symbol \"\" included in string abc?", '""' in 'abc')
