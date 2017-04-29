Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:18:55) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = []
>>> a.append('Hi')
>>> a
['Hi']
>>> a.append('Hello','User')
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    a.append('Hello','User')
TypeError: append() takes exactly one argument (2 given)
>>> a.append(['Hello','User'])
>>> a
['Hi', ['Hello', 'User']]
>>> a.append([1,2,3,4])
>>> a
['Hi', ['Hello', 'User'], [1, 2, 3, 4]]
>>> a[1]
['Hello', 'User']
>>> a.pop()
[1, 2, 3, 4]
>>> a
['Hi', ['Hello', 'User']]
>>> a.insert(0,[0,1,2,3])
>>> a
[[0, 1, 2, 3], 'Hi', ['Hello', 'User']]
>>> a.remove(2)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a.remove(2)
ValueError: list.remove(x): x not in list
>>> a.remove('Hi')
>>> a
[[0, 1, 2, 3], ['Hello', 'User']]
>>> del(a[0])
>>> a
[['Hello', 'User']]
>>> a.extend([1,2,3,4,5,6])
>>> a
[['Hello', 'User'], 1, 2, 3, 4, 5, 6]
>>> a.extend('Hi','Python')
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    a.extend('Hi','Python')
TypeError: extend() takes exactly one argument (2 given)
>>> a.extend(['Hi','Python'])
>>> a
[['Hello', 'User'], 1, 2, 3, 4, 5, 6, 'Hi', 'Python']
>>> a.count()
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    a.count()
TypeError: count() takes exactly one argument (0 given)
>>> a.count(0)
0
>>> a.count(7)
0
>>> t = (1,2,3)
>>> t
(1, 2, 3)
>>> t.extend([0,1])
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    t.extend([0,1])
AttributeError: 'tuple' object has no attribute 'extend'
>>> a = ('Hi',1,4,6,'Python')
>>> a
('Hi', 1, 4, 6, 'Python')
>>> dictionary = {'id':101,'name':'Ram','age':25}
>>> dictionary.keys
<built-in method keys of dict object at 0x0000000003439D08>
>>> dictionary.keys()
dict_keys(['name', 'id', 'age'])
>>> dictionary.values()
dict_values(['Ram', 101, 25])
>>> for i in dictionary:
	print(i)

name
id
age
>>> for i in dictionary.items():
	print(i)

('name', 'Ram')
('id', 101)
('age', 25)
>>> dictionary['name']
'Ram'
>>> dictionary['name'] = 'Shyam'
>>> dictionary
{'name': 'Shyam', 'id': 101, 'age': 25}
>>> dictionary.update('id' : 102)
SyntaxError: invalid syntax
>>> dictionary.update('id', 102)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    dictionary.update('id', 102)
TypeError: update expected at most 1 arguments, got 2
>>> dictionary.update('id')
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    dictionary.update('id')
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> dictionary.update()
>>> dictionary.popitem()
('name', 'Shyam')
>>> dictionary
{'id': 101, 'age': 25}
>>> 
