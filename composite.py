#------------------------
# SEQUENCIAL - List, Tuple -> Operations -> create, add/update, get, remove, iterate
# Non-sequencial - Dict, Set

# SEQUENTIAL DATA TYPE
# 1. Create/Initialize
list = []
print(type(list))  # type - list

list = [14,2,'3']
print(len(list))  # number of items

# 2. get
print(list[0])

#3. Update/Add -> 'appende'
list[0] = 32
list.append(34)

#4. Delete
#del list[0]
#del list[-1]
#list.remove(3)

# 5. Iterate
for item in list:
    list.remove(item)

# list[x:y] gives values x to y-1 index
# list[x::y] gives values from x till end with increment of y
# list[::-1] -> print list in reverse way

# To concat, use + operator.
# 'a' * 3423 -> print a 3423 times


print('-'*50)

# Touple is read only list.
# touple with one value -> t = (5,) ends with comma


# Dictionary is created with {}, touple is with () and list via []
person = {'name': 'Pushpendra', age: '32'}

# check a key in dictionary -> 'name' in person -> True/False
# del person['age'] delete the key-value pair
# for key, value in person.items() // not efficient in python 2, for this we have iteritems() -> efficient with space
# person.items() gets list of touples


# Set is like a list, except values have to be unique
# 'in' operator
# s.add(10)
# s.remove(43)

#sorted(x)
