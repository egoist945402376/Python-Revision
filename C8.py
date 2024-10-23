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