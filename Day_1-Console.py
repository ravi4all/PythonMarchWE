Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("Hello wordl")
Hello wordl
>>> print("Hello world")
Hello world
>>> a = 12
>>> b = 3
>>> a + b
15
>>> a - b
9
>>> a / b
4.0
>>> a // b
4
>>> a * b
36
>>> a ** b
1728
>>> a,b = 3,5
>>> a,b = b,a
>>> a
5
>>> b
3
>>> import os
>>> import sys
>>> import random
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/March/PythonWE_12-30/Code_1.py 
16
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/March/PythonWE_12-30/Code_1.py 
16
Sum is 16
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/March/PythonWE_12-30/Code_1.py 
16
Sum is 16
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/March/PythonWE_12-30/Code_1.py 
16
Traceback (most recent call last):
  File "C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/March/PythonWE_12-30/Code_1.py", line 5, in <module>
    print("Sum is"+c)
TypeError: can only concatenate str (not "int") to str
>>> 12 + '2'
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    12 + '2'
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 12 * '2'
'222222222222'
>>> 'a'* 8
'aaaaaaaa'
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/March/PythonWE_12-30/Code_1.py 
16
Sum is 16
Sum of 12 and 4 is 16
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/March/PythonWE_12-30/Code_1.py 
16
Sum is 16
Sum of 12 and 4 is 16
Sum is 16
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/March/PythonWE_12-30/Code_1.py 
16
Sum is 16
Sum of 12 and 4 is 16
Sum is 16
Sum of 12 and 4 is 16
>>> name = 'Ravi'
>>> msg = "hello {}".format(name)
>>> msg
'hello Ravi'
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/March/PythonWE_12-30/Code_1.py 
16
Sum is 16
Sum of 12 and 4 is 16
Sum is 16
Sum of 12 and 4 is 16
Sum of 12 and 4 is 16
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/March/PythonWE_12-30/Code_2.py 
Enter your name : Ram
Hello Ram
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/March/PythonWE_12-30/Code_2.py 
Enter your name : Ram
Hello Ram
Enter first num : 24
Enter second num : 56
2456
>>> num_1
'24'
>>> num_2
'56'
>>> type(num_1)
<class 'str'>
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/March/PythonWE_12-30/Code_2.py 
Enter your name : Ram
Hello Ram
Enter first num : 23
Enter second num : 22
45
>>> print("hello","ram")
hello ram
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> x = True
>>> True = 'hello'
SyntaxError: can't assign to keyword
>>> raw_input(" : ")
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    raw_input(" : ")
NameError: name 'raw_input' is not defined
>>> import sys
>>> sys.getsizeof(12)
28
>>> sys.getsizeof(0)
24
>>> sys.getsizeof(None)
16
>>> sys.getsizeof(True)
28
>>> a = "hello"
>>> a[0]
'h'
>>> a[3]
'l'
>>> a = "hello world"
>>> a[0] = 'x'
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    a[0] = 'x'
TypeError: 'str' object does not support item assignment
>>> a[-1]
'd'
>>> a[0:8]
'hello wo'
>>> a[3:5]
'lo'
>>> a[:]
'hello world'
>>> a[:4]
'hell'
>>> a[0:]
'hello world'
>>> a[0:100]
'hello world'
>>> a[5:0]
''
>>> a[0:10:2]
'hlowr'
>>> a[-5:-2]
'wor'
>>> a[-2:-5]
''
>>> a[-2:-5]:-1
>>> a[-2:-5:-1]
'lro'
>>> a[::-1]
'dlrow olleh'
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> dir(str())
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> a.islower()
True
>>> a.isupper()
False
>>> a.isalpha()
False
>>> a.isdigit()
False
>>> a.isspace()
False
>>> a.isalnum()
False
>>> a[0].islower()
True
>>> a.capitalize()
'Hello world'
>>> a.title()
'Hello World'
>>> a.upper()
'HELLO WORLD'
>>> a.lower()
'hello world'
>>> a.center(10)
'hello world'
>>> a.center(20)
'    hello world     '
>>> len(a)
11
>>> a.center(12)
'hello world '
>>> a.center(13)
' hello world '
>>> a.center(50)
'                   hello world                    '
>>> a.center(30, '$')
'$$$$$$$$$hello world$$$$$$$$$$'
>>> a.center(30, '#')
'#########hello world##########'
>>> a.count('e')
1
>>> a.count('l')
3
>>> a.startswith('h')
True
>>> a.endswith('e')
False
>>> a.endswith('d')
True
>>> a.find('l')
2
>>> a.find('l',3)
3
>>> a.find('l',4)
9
>>> a.rfind('l')
9
>>> names = ['ram','shyam','aman']
>>> ' '.join(names)
'ram shyam aman'
>>> x = "hello this is python"
>>> x.split()
['hello', 'this', 'is', 'python']
>>> y = x.split()
>>> ' '.join
<built-in method join of str object at 0x000002A957472260>
(
>>> ' '.join(x)
'h e l l o   t h i s   i s   p y t h o n'
>>> ' '.join(y)
'hello this is python'
>>> names
['ram', 'shyam', 'aman']
>>> y1 = ' '.join(y)
>>> y1
'hello this is python'
>>> ' '.join(y)
'hello this is python'
>>> _
'hello this is python'
>>> 10 + 12
22
>>> _
22
>>> x = "hello\nthis\nis\npython"
>>> print(x)
hello
this
is
python
>>> x.split()
['hello', 'this', 'is', 'python']
>>> x.split('\n')
['hello', 'this', 'is', 'python']
>>> x.split('hello')
['', '\nthis\nis\npython']
>>> 
