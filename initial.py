# -----------------------------------
# INFO
# :set tabStop = 4 <- for VI
# :set expandtab = 4
# pip install <NAME - django>

#-----------------------------------
# CONDITION & FUNCTION
# KEYWORDS - if, elif, else, def, return, is, is not
# python does not have function overriding - same name with different type or number of arg
# All arguments are mandatory
difference = -1
def checkForAdult(age=18) :
    difference = -1
    if age >= 18 :
        print("you are an Adult")
    else :
        difference = abs(age - 18)
        print("you are "+str(difference)+" way to go")

x = checkForAdult(18)
print(x is not None)

# pass is dummy statement.

#------------------------
# RANGE
# range(5) -> [0,1,2,3,4]
# range(5,4) -> [-5,-4,-3...2,3,4]
# range(1, 11, 2) -> prints odd number -> [1,3,5,7,9]
# range(1,12,0) -> BAD
for i in range(10):
    pass


# ----------- EXAMPLE --------

#for i in range(1,101,1):
#    if i % 21 == 0 :
#        print("FAST CAR")
#    elif i % 7 == 0:
#        print("CAR")
#    elif i % 3 == 0 :
#        print("FAST")
#    else :
#        print(i)

checkForAdult()

def myRange(start,end=None, step=None):
    listOfItems = []
    if end is None:
        end, start = start, 0
        step = 1
    if step is None:
        step = 1
    while end > start or start > end:
        listOfItems.append(start)
        start += step
    return list

myRange(7,1,-1)

def fib(n):
    if n > 1:
        return fib(n-1) + fib(n-2)
    return n

# return n if n == 0 or n == 1 else fib(n-1) + fib(n-2)
#print(fib(4))

print('-'*40)

for item in myRange(5):
    print(item)

