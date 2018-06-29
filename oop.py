print("\n"+'-'*20+" COMMENTS "+'-'*20+"")

print '''
# new style classes take object as arg
# Every Oject has same state and behaviour is part of class <- Memory
# def __private2(self): # re-writing method name, c1.__private() won't work
# def _private(self): # supposed to be internal uses
# for private state, use closures
# meta programming, equivalant of reflection in java
# def __init__(self, **kwargs): like constructor, __erer__ are magic methods.
# Python allows multiple inheritance unlike Java, and first one is given preference over second to resolve dimond problem - MRO Algo is used to solve the multiple inheritance problem)
'''

print("\n"+'-'*20+" CLASS "+'-'*20+"")

class Car(object):
    wheel = 0 # state of the class...
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self,key,value) #meta programming, equivalant of reflection in java

    def drive(self):
        print 'The car is being driven'

    def _private(self): # supposed to be internal uses
        print 'Hello Pooja'

    def __private2(self):  # re-writing method name, c1.__private() won't work
        print 'Hello Again Pooja'


car1 = Car(wheels=4)
print car1.wheels
car1.drive()  # Car.drive(car1)

car1._private()
#car1.__private2()

print("\n"+'-'*20+" OPERATOR OVERLOADING "+'-'*20+"")

class Amount(object):
    def __init__(self,amt):
        self.amt = amt
    
    def __add__(self,other):
        return Amount(self.amt + other.amt)

a1 = Amount(50)
a2 = Amount(100)
a3 = a1 + a2  # read it as, a1.__add__(a2)
print a3.amt


print("\n"+'-'*20+" INHERITANCE "+'-'*20+"")

class Person(object):
    def print_name(self):
        print self.name

class Employee(Person):
    pass

e1 = Employee()
e1.name = 'Pooja'
e1.print_name()

print("\n"+'-'*20+" MULTIPLE INHERITANCE "+'-'*20+"")

print('In case of common method, E -> B1 -> B2 -> B')

class B1(object):
    def foo(self):
        print 'B1'

class B2(object):
    def foo(self):
        print 'B2'

class E(B1,B2):
    pass

e1 = E()
e1.foo()
