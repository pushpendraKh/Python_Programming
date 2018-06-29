# Functional Programming Language

# 1. you can assign it to other variables E.g. x = 10
# 2. you can pass it to other functions E.g. foo(10)
# 3. you can return it from a function E.g. return 10

# All of above 3 properties, are for first class. For Eg Number are first class


# for a function, variable is the name of function and value is the function body, in the sense if we compare it with number where x is the variable and value is the constant.

# Example for Point 1 -
print("\n"+'-'*20+" First Class Function Property "+'-'*20+"")

def sum(number1, number2):
    return number1 + number2

add = sum
print('point 1 - you can assign it to other variables')
add(4,4)

# Example For Point 2 -
def fooCaller(foo):
    foo()

def bar():
    print('point 2 - you can pass it to other functions')

fooCaller(bar)



# Example For Point 3 -

def foo():
    def bar():
        print 'Point 3 - you can return it from a function'
    return bar

x = foo()
x()

print("\n"+'-'*30+" Data Transform "+'-'*30+"")

print 'lambda function is a function without a name'
print 'lambda function has only one statement, so no need to write return too'
print 'replace def with lambda'

print("\n"+'<'*10+" My Map "+'>'*10+"")

def square(number):
    return number ** 2

def myMap(operation, l):
    ol = []
    for item in l:
        ol.append(operation(item))
    return ol

l = [4,5,6]
sl = myMap(square, l) # short
ol = map(lambda number: number**2, l) # shorter
shortSl = [square(x) for x in l]  # shortest
print shortSl
# shortest

print("\n"+'<'*10+" Reduce "+'>'*10+"")
sumOfAllSquares = reduce(sum,(square(x) for x in l))
print sumOfAllSquares

print("\n"+'<'*10+" Filter "+'>'*10+"")
oddNumber = filter(lambda number: number % 2 == 1, l)
oddNumber1 = [num for num in l if num % 2 == 1] #comprehensive
print oddNumber1

