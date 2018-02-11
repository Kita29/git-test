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
