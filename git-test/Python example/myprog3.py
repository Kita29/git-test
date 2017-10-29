a = 3 # global variable
print('global variable a = ', a)
y = 8
print('global variable y = ', y)

def func ():
    print('func: global variable a = ', a)
    y = 5 # local variable
    print('func: local variable y = ', y)

func() # call function
print('??? y = ', y) # display global variable y
