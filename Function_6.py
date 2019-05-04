# Menu Driven Program
def add(x,y):
    z = x + y
    print(z)

def sub(x,y):
    z = x - y
    print(z)

def div(x,y):
    z = x / y
    print(z)

def mul(x,y):
    z = x * y
    print(z)

print("""
1. Add
2. Sub
3. Div
4. Mul
""")
ch = input("Enter your choice : ")
f_num = int(input("Enter first number : "))
s_num = int(input("Enter second number : "))

todo = {"1":add, "2":sub, "3":div, "4":mul}
todo.get(ch)(f_num, s_num)
