import networkx as nx
import scipy as sp
import matplotlib.pylab as plt
import datetime

current_date = datetime.datetime.now()
print (current_date)




my_tupple= ("Aaron", "Matei", "Mwanzia")
iteration = iter(my_tupple)

# print (next(iteration))
# print (next(iteration))
# print (next(iteration))



# t=sp.linspace(0, 1, 100)
# plt.plot (t, t ** 3)
# plt.show()

class Dating(object):
	"""docstring for ClassName"""
	raise_amt = 1.20
	def __init__(self, first_name, last_name, age, pay):
		super(Dating, self).__init__()
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		# self.email = self.first_name + self.last_name + "@" + "gmail.com"
		self.pay = pay
	def fullname(self):
		return '{} {}'.format(self.first_name, self.last_name)
	def email(self):
		return '{}{}@gmail.com'.format(self.first_name, self.last_name)
	def apply_raise(self):
		return int(self.pay * self.raise_amt)
	def __repr__(self):
		return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)
	def __str__(self):
		return '{} - {}'.format(self.fullname(), self.email)
	def __add__(self, other):
		return self.pay + other.pay
	def __len__(self):
		return len(self.fullname())
	@staticmethod
	def is_it_a_working_day(day):
		if day.weekday() == 5 or day.weekday() == 6:
			return False
		return True

class Developer (Dating):
	raise_amt=1.45

	def __init__(self, first_name, last_name, age, pay,p_language):
		super().__init__(first_name, last_name, age, pay)
		self.p_language = p_language

class Manager(Dating):

    def __init__(self, first_name, last_name, age, pay, employees=None):
        super().__init__(first_name, last_name, age, pay)
        
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())



emp1 = Dating("Aaron", "Matei", 28, 9000)
dev1 = Developer("Sophie", "Matei", 21, 1500, "Python")
dev2 = Developer("Tash", "Tee", 25, 60000, "Java")
mgr_1 = Manager("Sue", "Smith", 30, 90000, [dev1])

print(mgr_1.email())
mgr_1.add_emp(dev2)
mgr_1.add_emp(dev1)
mgr_1.remove_emp(dev2)
print(mgr_1.print_emps())
print(len(mgr_1.email()))
print("The salary for " + emp1.fullname() + " and " + dev2.fullname()+ " is " + str(emp1 + dev2))





print(emp1.email())
print(emp1.first_name)
print(emp1.last_name)
print(emp1.age)
print(emp1.pay)
print(emp1.apply_raise())
print("Hey " + emp1.fullname() + ""+ ", Your original pay was " + str(emp1.pay) +" and your new pay is: " + str(emp1.apply_raise()) + " after the pay rise")

my_date = datetime.datetime.now()
print("It is " + str(emp1.is_it_a_working_day(my_date))+ " that today is a weekday")



print(dev1.first_name)
print(dev1.last_name)
print(dev1.email())
print(dev1.age)
print(dev1.pay)
print(dev1.apply_raise())

print("Hey " + dev1.fullname() + ""+ ", Your original pay was " + str(dev1.pay) +" and your new pay is: " + str(dev1.apply_raise()) + " after the pay rise")

my_date = datetime.datetime.now()
print("It is " + str(emp1.is_it_a_working_day(my_date))+ " that today is a weekday")



		