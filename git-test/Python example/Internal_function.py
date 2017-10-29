def outer(a, b):
    def inner(c, d):
        return c + d
    return inner(a, b)

def kn(a):
    def inner():
        return a + 5
    return inner
# example: a = kn(6) ---> a()
