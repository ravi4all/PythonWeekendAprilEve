Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def add():
	a = 10
	b = 20
	c = a + b

>>> add()
>>> print(add())
None
>>> def add():
	a = 10
	b = 20
	c = a + b
	return c

>>> print(add())
30
>>> def add(x,y):
	return x + y

>>> add(1,2)
3
>>> def address(addr):
	print(addr)

>>> address("ABC")
ABC
>>> address("Office Address","Home Address","Secondary Address")
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    address("Office Address","Home Address","Secondary Address")
TypeError: address() takes 1 positional argument but 3 were given
>>> def address(*addr):
	print(addr)

	
>>> address("Office Address","Home Address","Secondary Address")
('Office Address', 'Home Address', 'Secondary Address')
>>> def address(*addr):
	for a in addr:
		print(a)

		
>>> address("Office Address","Home Address","Secondary Address")
Office Address
Home Address
Secondary Address
>>> def h():
	x = 10
	def i():
		print(x)

>>> i()
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    i()
NameError: name 'i' is not defined
>>> def h():
	x = 10
	def i():
		print(x)
	i()

>>> h()
10
>>> def h():
	print("This is function H")

>>> def g():
	print("This is function G")

>>> def h(g):
	print("This is function H")

	
>>> h(g())
This is function G
This is function H
>>> 
