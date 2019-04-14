Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> data = [4,5,7,8,2,5,7,'hi','hello','hey',10.5,12.55]
>>> data.append(100)
>>> data
[4, 5, 7, 8, 2, 5, 7, 'hi', 'hello', 'hey', 10.5, 12.55, 100]
>>> numbers = []
>>> for i in range(0,101,2):
	numbers.append(i)

	
>>> numbers
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
>>> numbers.pop()
100
>>> numbers.pop(10)
20
>>> numbers.remove(52)
>>> numbers
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]
>>> num = [2,4,5,6,7,8,12,34,56,2,56,22,66,34,87,34,64]
>>> numbers + num
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 2, 4, 5, 6, 7, 8, 12, 34, 56, 2, 56, 22, 66, 34, 87, 34, 64]
>>> numbers.extend(num)
>>> numbers
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 2, 4, 5, 6, 7, 8, 12, 34, 56, 2, 56, 22, 66, 34, 87, 34, 64]
>>> numbers.count(2)
3
>>> numbers.count(4)
2
>>> numbers.count(22)
2
>>> numbers.index(2)
1
>>> numbers.index(2,1)
1
>>> numbers.index(2,2)
48
>>> numbers.index(2,49)
57
>>> numbers.count(4)
2
>>> for i in range(len(numbers)):
	if numbers[i] == 2:
		print(i)

		
1
48
57
>>> numbers.insert(4,400)
>>> numbers
[0, 2, 4, 6, 400, 8, 10, 12, 14, 16, 18, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 2, 4, 5, 6, 7, 8, 12, 34, 56, 2, 56, 22, 66, 34, 87, 34, 64]
>>> num
[2, 4, 5, 6, 7, 8, 12, 34, 56, 2, 56, 22, 66, 34, 87, 34, 64]

>>> numbers.insert(4,num)
>>> numbers
[0, 2, 4, 6, [2, 4, 5, 6, 7, 8, 12, 34, 56, 2, 56, 22, 66, 34, 87, 34, 64], 400, 8, 10, 12, 14, 16, 18, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 2, 4, 5, 6, 7, 8, 12, 34, 56, 2, 56, 22, 66, 34, 87, 34, 64]
>>> data = [['Ram','Shyam','Gopal'],['IT','HR','IT'],['TCS','HCL','TCS']]
>>> data[0]
['Ram', 'Shyam', 'Gopal']
>>> data[0][0]
'Ram'
>>> data[1][0]
'IT'
>>> data[2][0]
'TCS'
>>> data[0][0],data[1][0],data[2][0]
('Ram', 'IT', 'TCS')
>>> for i in range(len(data[0])):
	print(data[0][i],data[1][i],data[2][i])

	
Ram IT TCS
Shyam HR HCL
Gopal IT TCS
>>> for i in range(len(data)):
	for j in range(len(data[i])):
		print(data[i][j])

		
Ram
Shyam
Gopal
IT
HR
IT
TCS
HCL
TCS
>>> for i in range(len(data)):
	for j in range(len(data[i])):
		print(data[i][j], end = ' ')

		
Ram Shyam Gopal IT HR IT TCS HCL TCS 
>>> for i in range(len(data)):
	for j in range(len(data[i])):
		print(data[i][j], end = ' ')
	print()

	
Ram Shyam Gopal 
IT HR IT 
TCS HCL TCS 
>>> tup = 45,
>>> tup
(45,)
>>> tup = 45,21,34,56,78
>>> tup = (45,21,34,56,78)
>>> tup[0] = 100
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    tup[0] = 100
TypeError: 'tuple' object does not support item assignment
>>> del tup[0]
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    del tup[0]
TypeError: 'tuple' object doesn't support item deletion
>>> emp = name, sal, dept = 'Ram', 24000, 'HR'
>>> emp
('Ram', 24000, 'HR')
>>> name
'Ram'
>>> sal
24000
>>> dept
'HR'
>>> name = 'Shyam'
>>> emp
('Ram', 24000, 'HR')
>>> a = 10,12
>>> a
(10, 12)
>>> a,b = 10,12
>>> a
10
>>> b
12
>>> d = {'name':'Ram','age':40,'sal':45000,'dept':'IT'}
>>> d.keys()
dict_keys(['name', 'age', 'sal', 'dept'])
>>> d.values()
dict_values(['Ram', 40, 45000, 'IT'])
>>> d.items()
dict_items([('name', 'Ram'), ('age', 40), ('sal', 45000), ('dept', 'IT')])
>>> d[0]
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    d[0]
KeyError: 0
>>> d['name']
'Ram'
>>> d['age']
40
>>> d['address'] = 'delhi'
>>> d
{'name': 'Ram', 'age': 40, 'sal': 45000, 'dept': 'IT', 'address': 'delhi'}
>>> d['age']  = 41
>>> a
10
>>> d
{'name': 'Ram', 'age': 41, 'sal': 45000, 'dept': 'IT', 'address': 'delhi'}
>>> 
