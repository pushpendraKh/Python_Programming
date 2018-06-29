print("\n"+'-'*20+" MODULES "+'-'*20+"")

print '''
# Built-in
# My Own
# 3rd Party
'''

print("\n"+'-'*20+" USES "+'-'*20+"")

print 'import <module_name e.g. math>'

# Refering -> math.pi, math.sqrt(5)

import sys
print sys.path  # places, python looks for imported module, prints a list which can be modified

# 'Alias in python -> import math as m'
# If you want to import only some fields from a module, write like - from math import sqrt, pi etc

# mymath.trig.tan mymath - directory, trig - .py file, tan - method
# inside directory if you put __init__.py.. that will work as module. so mymath can also work as directry

import mymath
print mymath.pi
print mymath.power(3,4)


# 3rd party module -> pip install <Name>
