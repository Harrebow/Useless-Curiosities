import timeit
import_module = "import random"
testcode = ''' 
def test():
    for i in range(0, 10001):
        if i % 2 != 0:
            print (i)
'''
print(timeit.timeit(stmt=testcode, setup=import_module))

import timeit
import_module = "import random"
testcode = ''' 
def test(): 
    x = 1
    while x < 10001:
        if x % 2 != 0:
            print(x)
        x += 1
'''
print(timeit.timeit(stmt=testcode, setup=import_module))
