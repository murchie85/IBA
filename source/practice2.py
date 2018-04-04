# pyton OOO 


class Employee:
	# this is like the constructore
	#when we create methods in a class  they receive the instance as the first argument automatically
	#we call it self, but this is convention
	#after self we specify what args we want to accept
	def __init__(self, first, last, pay):
		self.first = first # the same as saying emp_1.first = 'Corey', this is done automatically when we create emp_1 Employee objects
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'

emp_1 = employee('corey', 'cumgullet', '50000')# don't need to pass self (the instance)
emp_2 = employee('bob', 'cunt', '20000')

print(emp_1)
print(emp_2)

print(emp_1.email)
print(emp_2.email)

#instant vars contain data unique to each instant 
"""
emp_1.first = 'Corey'
emp_1.last = '_shafer_'
emp_1.email = 'corey@gmail.com'
emp_1.pay = 50000


emp_2.first = 'bob'
emp_2.last = 'cunt'
emp_2.email = 'bob@gmail.com'
emp_2.pay = 50000
"""


