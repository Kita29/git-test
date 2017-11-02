def input_example():
    s = input("Enter the string: ")
    print(s)
    print(type(s))
    s = input("Enter the numeric: ")
    print(s)
    print(type(s))
    s = int(input("Enter the numeric: "))
    print(s)
    print(type(s))

def input_name():
    val = input("What is your name?\n")
    print("Hello, " + val + "!")

def operation_with_strings():
    s = "Don't take it to heart"
    print("s = ", s)
    print("First symbol = " + s[0])
    print("Last symbol = " + s[-1])
    print("Last symbol with number " + str(len(s)-1) + " = " + s[len(s)-1])
    print("s[1:3] = ", s[1:3]) # from 1 to 3 (not incl.)
    print("s[:3] = ", s[:3]) # from 0 to 3 (not incl.)
    print("s[:] = ", s[:]) # all string
    print("s[::-1] = " ,s[::-1])
    print("s = ", s)
    print("Do it: 'J' + s[1:]")
    print('J' + s[1:])
    print("But string s remained = ", s)

def sum_and_multiplication():
    val1 = int(input("Enter the first number\n"))
    val2 = int (input("Enter the second number\n"))
    val3 = int(input("Enter the third number\n"))
    print("Sum entered numbers = ", val1 + val2 + val3)
    print("Multiplication entered numbers = ", val1 * val2 * val3)
    
