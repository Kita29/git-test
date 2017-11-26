def str_method():
    print("str.capitalize('hello') = ", str.capitalize('hello'))
    print("'hello'.capitalize() = ", 'hello'.capitalize())
    print("help(str.capitalize) = ", help(str.capitalize))
    print("str.center('hello',20) = ", str.center('hello',20))
    print("('TTA' + 'G'*3).count('T') = ", ('TTA' + 'G'*3).count('T'))
    print("'{0} and {1}'.format('work','may') = ", '{0} and {1}'.format('work','may'))
    print("'{1} and {0}'.format('work','may') = ", '{1} and {0}'.format('work','may'))

    n = 10
    print("n = ", n)
    print("Binary - '{:b}'.format(n) = ", '{:b}'.format(n))
    print("Unicode - '{:c}'.format(n) = ", '{:c}'.format(n))
    print("Po osnovaniy 10 - '{:d}'.format(n) = ", '{:d}'.format(n))
    print("Po osnovaniy 16 - '{:x}'.format(n) = ", '{:x}'.format(n))
    print("'spec'.startswith('a') = ", 'spec'.startswith('a'))

    s = '      \n sssss \n'
    print("s = '      \n sssss \n'")
    print("s.split() = ", s.split())
    print("'HeLlo'.swapcase() = ", 'HeLlo'.swapcase())
    print("'HELLO'.swapcase().endswith('o') = ", 'HELLO'.swapcase().endswith('o'))

    s = 'Hello! My name is Alina'
    print("s = ",s)
    print("s.upper() = ", s.upper())
    print("s.lower() = ", s.lower())
    print("s.title() = ", s.title())
    print("s.find('ell',2,3) = ", s.find('ell',2,3))
    print("s.count('l',1,5) = ", s.count('l',1,5))
    print("s.isalpha() = ", s.isalpha())
    print("s.isdigit() = ", s.isdigit())
    print("s.islower() = ", s.islower())
    print("s.istitle() = ", s.istitle())
    print("s.isspace() = ", s.isspace())

    print("'TT' + 'rr' = ", 'TT' + 'rr')
    print("'TT'.__add__('rr') = ", 'TT'.__add__('rr'))
    print("str.__add__('TT','rr') = ", str.__add__('TT','rr'))
    
    

    
