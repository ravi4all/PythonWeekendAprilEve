Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class Emp:
	id = 0
	name = ""
	age = 0

>>> Emp
<class '__main__.Emp'>
>>> type(Emp)
<class 'type'>
>>> Emp.id
0
>>> Emp.name
''
>>> Emp.age
0
>>> Emp.salary
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    Emp.salary
AttributeError: type object 'Emp' has no attribute 'salary'
>>> Emp.salary = 12000
>>> Emp
<class '__main__.Emp'>
>>> Emp.salary
12000
>>> Emp.id = 101
>>> Emp.name = "Ram"
>>> Emp.id
101
>>> Emp.id = 101
>>> Emp.id = 102
>>> Emp.id
102
>>> emp_1 = Emp()
>>> type(emp_1)
<class '__main__.Emp'>
>>> emp_1.__main__
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    emp_1.__main__
AttributeError: 'Emp' object has no attribute '__main__'
>>> emp_1.id
102
>>> emp_2 = Emp()
>>> emp_2.id = 103
>>> emp_2
<__main__.Emp object at 0x02F81FF0>
>>> emp_2.id
103
>>> emp_1.id
102
>>> 
