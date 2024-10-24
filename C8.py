# High-order functions
# Functions can be passed as arguments
# or returned as an output
# Variables can be assigned to functions
f = abs
print(f(-10))

# Pass functions as arguments
def add(x, y, f):
    return f(x) + f(y)

# When we call add(), x = -5, y = 6, f = abs
print(add(-5, 6, abs))

# map function
def f(x):
    return x * x
a = [1,2,3,4,5,6,7,8,9]
r = map(f, a)
print(list(r))

# reduce function
from functools import reduce
import time
def add(x,y):
    return x + y
a = reduce(add, [1,2,4,5,6])
print(a)

def normalize(name):
    return name.capitalize()
names = ['adam', 'LISA', 'barT']
names = list(map(normalize, names))
print(names)

def prod(x,y):
    return x * y
a = reduce(prod, [2,4,5,7,12])
print(a)

# filter function
# filter receives a function and a list
# The function returns True or False, and filter passes all
# elements of the list to the function, and returns a new list
# based on the function's return value for each element
def odd_number(n):
    return n % 2 == 1
a = filter(odd_number, [1,2,3,4,5,6,7,8,9])
print(list(a))

def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)

for n in primes():
    if n < 100:
        print(n)
    else:
        break

def is_palindrome(n):
    n = str(n)
    return n == n[::-1]
palindromes = filter(is_palindrome, range(1,1000))
print(list(palindromes))

# sorted
# sorted function can receive a key function
# then the function will sort the list based on the values
# returned by the key function
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0]
def by_score(t):
    return t[1]
l1 = sorted(L, key = by_name)
l2 = sorted(L, key = by_score)
print(l1)
print(l2)

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
# f is a function
f = lazy_sum(1,3,5,7,9)
# f() is the result of the function
print(f())

def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs
# fs is a list of functions containing 3 f()

# Assign these functions to f1, f2, f3
# it is my first time to know this syntax
# you can directly assign variables in the list to variables
f1, f2, f3 = count()
print(f2())
print(f3())

# nonlocal
def inc():
    x = 0
    def fn():
        nonlocal x
        x = x + 1
        return x
    return fn

f = inc()
print(f()) # 1
print(f()) # 2

def createCounter():
    x = 0
    def counter():
        nonlocal x
        x = x + 1
        return x
    return counter

# When you create an instance of the createCounter
# the x is initialized to 0
# If you call counter(), it will increment x (local variable in createCounter) by 1
# because it has nonlocal x and it increment x by 1
# This is forever for this single instance
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('Test success!')
else:
    print('Test failed!')


# lambda function
# lambda is a short function with no name, no return statement
# It has only one single expression, and the return values is the result of the expression
l1 = list(map(lambda x: x * x, [1,2,3,4,5,6,7,8,9]))
print(l1)

L = list(filter(lambda x: x % 2 == 1, range(1,20)))
print(L)

# decorator
# all function has a __name__ attribute


def log(func):
    def wrapper(*args, **kw):
        print(f"Call {func.__name__}")
        return func(*args, **kw)
    return wrapper
@log
def now():
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# After this, when you are calling now(), it is actually calling wrapper()
f = now
f()
print(f.__name__)