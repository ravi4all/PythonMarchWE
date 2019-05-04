a = 23
b = 33
def calc():
    global a
    a = 12
    #b = 33
    c = a + b
    print(c)

calc()
z = a + b
print(z)
