# def too(*args, **kwargs)

# host, port, user, user name and password to connect with data base

# def connect_to_db(host, port, user, username, password, **kwargs) - splat operator

# * is not a pointer like C

# reference is copy by value .i.e you are passing a referernce who is having copy of value

def swap(number1, number2):
    number2, number1 = number1, number2


def update(l,index,number):
    l[index] = number

l = [1,2,3]
update(l,0,6)


def empty_list(l):
    while(len(l)):   # l[:] = []
        l.pop() # del l[-1]

l = [1,2,3]
empty_list(l)
print l
