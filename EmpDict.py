emp = [
    {'emp_id':101,'emp_name':'Ram','emp_dept':'IT','emp_sal':45000},
    {'emp_id':102,'emp_name':'Shyam','emp_dept':'HR','emp_sal':35000},
    {'emp_id':103,'emp_name':'Raman','emp_dept':'HR','emp_sal':55000},
    {'emp_id':104,'emp_name':'Aman','emp_dept':'IT','emp_sal':40000},
    {'emp_id':105,'emp_name':'Gopal','emp_dept':'IT','emp_sal':20000},
    {'emp_id':106,'emp_name':'Manoj','emp_dept':'HR','emp_sal':23000},
    {'emp_id':107,'emp_name':'Shivam','emp_dept':'IT','emp_sal':28000},
    ]

for i in range(len(emp)):
    if emp[i]['emp_dept'] == 'IT':
        print(emp[i])
# Fetch data of those emp whose name start with 'A'
# Fetch data of those emp whose salary is under 30000


students = [
    {'name':'Ram','hobby':'cricket','class':8,'marks':[56,67,88]},
    {'name':'Shyam','hobby':'cricket','class':9,'marks':[56,56,78]},
    {'name':'Amit','hobby':'football','class':8,'marks':[87,70,98]},
    {'name':'Aman','hobby':'hockey','class':9,'marks':[88,76,89]},
    {'name':'Gopal','hobby':'football','class':8,'marks':[58,62,81]}
]
'''
Fetch average marks of all students like:
    Ram : 67
    Shyam : 87
'''
