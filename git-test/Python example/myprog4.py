x = 50 # global variable
def func():
    global x # tell that x - global variable
    print('x = ', x)
    x = 2 # change global variable
    print('Change global variable x on ', x)

func()
print('Value x = ', x)
    
