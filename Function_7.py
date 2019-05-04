def calc(x,y,opr):
    expression = x + opr + y
    #print(expression)
    result = eval(expression)
    print(result)

print("""
1. Add
2. Sub
3. Div
4. Mul
""")
ch = input("Enter your choice : ")
f_num = input("Enter first number : ")
s_num = input("Enter second number : ")

todo = {"1":"+", "2":"-", "3":"/", "4":"*"}
opr = todo.get(ch)
calc(f_num, s_num, opr)
