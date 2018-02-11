def f(x,y):
    print(x+y)

f([1, 2, 3], [4, 5, 6])
f("123", "456")
f(1,2)

h = ['bonjour', 7, 'hola', -1.0, 'privet']
print("h = ", h)
if 7 in h:
    print("7 included in list")
print("_____")
g = h[1:2]
print("h[1:2] = ", g)
print("_____")
a = [-1, 1, 66.25, 333, 333, 1234.5]
print("a = ", a)
del a[0]
print("del a[0] -> a = ", a)
del a[2:4]
print("del a[2:4] -> a = ", a)
del a[:]
print("a[:] = ", a)
print("_____")
print("h = ", h)
p = h
print("p = ", p)
p[0] = 1
print("p[0] = 1")
print("h = ", h)
print("p = ", p)
print("_____")
x = y = [1, 2]
print("x is y = ", x is y)
x = [1, 2]
y = [1, 2]
print("x is y = ", x is y)
print("_____")
a = [4, 3, [2, 1]]
b = a[:]
print("b is a = ", b is a)
b[2][0] = -100
print("b[2][0] = -100")
print("a = ", a)
print("_____")
import copy
a = [4, 3, [2, 1]]
b = copy.deepcopy(a)
b[2][0] = -100
print("a = ", a)
