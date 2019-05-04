# closures
def outer():
    x = 12
    def inner_1():
        y = 34
        z = x + y
        return z
    def inner_2():
        y = 21
        z = x - y
        return z
    #z = inner_1()
    #return z
    return inner_1, inner_2

#x = outer()
#print(x())

x = outer()
inner_1 = x[0]
inner_2 = x[1]
print(inner_2())

