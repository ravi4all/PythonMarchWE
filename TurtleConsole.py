Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/March/PythonWE_12-30/Loop_1.py 
0
1
2
3
4
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/March/PythonWE_12-30/Loop_1.py 
0
Inside Loop
1
Inside Loop
2
Inside Loop
3
Inside Loop
4
Inside Loop
Outside Loop
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/March/PythonWE_12-30/Loop_1.py 
0
Inside Loop
1
Inside Loop
2
Inside Loop
3
Inside Loop
4
Inside Loop
Outside Loop
Where am I...?
1
3
5
7
9
11
13
15
17
19
>>> import turtle
>>> t = turtle.Pen()
>>> t.shape('turtle')
>>> t.forward(200)
>>> t.left(90)
>>> t.forward(200)
>>> t.left(90)
>>> t.forward(200)
>>> t.left(90)
>>> t.forward(200)
>>> t.left(90)
>>> t.reset()
>>> for i in range(4):
	t.forward(200)
	t.left(90)

	
>>> t.reset()
>>> for i in range(20):
	t.forward(5*i)
	t.left(90)

	
>>> t.reset()
>>> for i in range(20):
	t.circle(5*i)
	t.forward(5*i)
	t.left(90)

	
>>> t.reset()
>>> for i in range(20):
	t.circle(5*i)
	t.left(90)

	
>>> t.reset()
>>> 
