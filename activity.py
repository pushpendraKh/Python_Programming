# Given a list of number

l = [1,2,3,4,4,1]

dictionary = {}
for item in l:
    if item in dictionary:
        dictionary[item] = dictionary[item] + 1
    else :
        dictionary[item] = 1

duplicates = []
non_duplicate = []
for key, value in dictionary.iteritems():
    if value > 1:
        duplicates.append(key)
    else:
        non_duplicate.append(key)


print("duplicate:")
print(duplicates)
print("Non-duplicate:")
print(non_duplicate)
