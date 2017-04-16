Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:18:55) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = 'Hello world, This is "python"'
>>> a
'Hello world, This is "python"'
>>> print(a)
Hello world, This is "python"
>>> a = "\Hello\"
SyntaxError: EOL while scanning string literal
>>> a = "\nHello\n"
>>> a
'\nHello\n'
>>> print(a)

Hello

>>> a = r"\nHello\n"
>>> print(a)
\nHello\n
>>> print("""Hello world !!!)
This is  python programming,
BMPL
""")
Hello world !!!)
This is  python programming,
BMPL

>>> print("Hello"*5)
HelloHelloHelloHelloHello
>>> print("Hello"*5+"World")
HelloHelloHelloHelloHelloWorld
>>> print("Hello\n"*5)
Hello
Hello
Hello
Hello
Hello

>>> a = "Hello"
>>> len(a)
5
>>> a.replace("H","O")
'Oello'
>>> a[::-1]
'olleH'
>>> a[0]
'H'
>>> a[0:3]
'Hel'
>>> a[0:4]
'Hell'
>>> a[-1]
'o'
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
>>> a = "machine"
>>> a[:2]
'ma'
>>> a[2:]
'chine'
>>> a[0:] + 's'
'machines'
>>> a = ["I","LIKE","LOGIC"]
>>> print("".join(a))
ILIKELOGIC
>>> a = [1,2,3,4,5,6]
>>> for i in a:
	print(i)

1
2
3
4
5
6
>>> i
6
>>> a = []
>>> a.push(10)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    a.push(10)
AttributeError: 'list' object has no attribute 'push'
>>> a.append(10)
>>> a
[10]
>>> a.append(12)
>>> a
[10, 12]
>>> a.insert(1,8)
>>> a
[10, 8, 12]
>>> a.pop()
12
>>> a
[10, 8]
>>> a.remove(0)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    a.remove(0)
ValueError: list.remove(x): x not in list
>>> a.remove(10)
>>> a
[8]
>>> a = [1,2,3,4,5,6,7]
>>> a.index(4)
3
>>> a.reverse()
>>> a
[7, 6, 5, 4, 3, 2, 1]
>>> a.sort()
>>> a
[1, 2, 3, 4, 5, 6, 7]
>>> a = [2,5,3,1,7,9,44,2,2,56,7,8]
>>> a.sort()
>>> a
[1, 2, 2, 2, 3, 5, 7, 7, 8, 9, 44, 56]
>>> a.sort(rev)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    a.sort(rev)
NameError: name 'rev' is not defined
>>> a.sort(reversed = True)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    a.sort(reversed = True)
TypeError: 'reversed' is an invalid keyword argument for this function
>>> a.sort('reversed' = True)
SyntaxError: keyword can't be an expression
>>> a.sort(reverse = True)
>>> a
[56, 44, 9, 8, 7, 7, 5, 3, 2, 2, 2, 1]
>>> b = ["Hi","Python","Programming"]
>>> a.extend(b)
>>> a
[56, 44, 9, 8, 7, 7, 5, 3, 2, 2, 2, 1, 'Hi', 'Python', 'Programming']
>>> a.insert(0,b)
>>> a
[['Hi', 'Python', 'Programming'], 56, 44, 9, 8, 7, 7, 5, 3, 2, 2, 2, 1, 'Hi', 'Python', 'Programming']
>>> del(a['Python'])
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    del(a['Python'])
TypeError: list indices must be integers or slices, not str
>>> a.index('Python')
14
>>> del(a[14])
>>> a
[['Hi', 'Python', 'Programming'], 56, 44, 9, 8, 7, 7, 5, 3, 2, 2, 2, 1, 'Hi', 'Programming']
>>> 
