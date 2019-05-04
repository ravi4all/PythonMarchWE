'''
def add(x,y):
    z = x + y
    print(z)
'''

def add(x = 0, y = 0):
    z = x + y
    print(z)
    
def sub(x,y):
    #z = x - y
    z = x - y if x > y else y - x
    print(z)

#add(2,2)
add(y=2,x=5)
sub(3,7)
