'''
def calc(x,y):
    z = x + y
    return z
'''

def calc(x,y):
    return x+y,x-y,x/y,x*y

#a = calc(4,5)
#a,b,c,d = calc(4,5)
#print(a,b)

#a,*b = calc(4,5)
#print(a,b)

a,*b,c = calc(4,5)
print(a,b,c)
