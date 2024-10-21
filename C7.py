# slice
language = ['Chinese', 'English', 'Japanese', 'French', 'German']
# slice [x:y], start from x, end at y. y is exclusive.
print(language[1:3])

# slice[-x:] start from the last x elements
print(language[-2:])

L = list(range(100))
# slice[x:], start from x to the end
print(L[-10:])

# slice[:y], start from the beginning to y
print(L[:10])

print(L[10:20])

# slice[:y:z], start from the beginning to y, step z
print(L[:10:2])

# slice[x::z], start from x to the end, step z
print(L[::5])

# Reverse a list
L_reverse = L[::-1]

def trim(str):
    if str[:1] == ' ':
        return trim(str[1:])
    elif str[-1:] == ' ':
        return trim(str[:-1])
    else:
        return str
    

# Iteration
from collections.abc import Iterable
print(isinstance('abc', Iterable))

example_dict = {'a': 1, 'b': 2, 'c': 3}
# by default, iterate through keys
for key in example_dict:
    print(key)
# iterate through values
for value in example_dict.values():
    print(value)
# iterate through both keys and values
for k, v in example_dict.items():
    print(k, v)

# enumerate
# enumerate returns an index and the value
enumerate_list = ['A', 'B', 'C']
for i, value in enumerate(enumerate_list):
    print(f"{i}th value is {value}")


# List comprehensions
# Generate a list containing x^2
squares = [ x*x for x in range(1, 11)]
print(squares)
even_squares = [ x*x for x in range(1,11) if x % 2 == 0]
print(even_squares)

# Generate a list of all combinations of two lists of letters
combined_letters = [m + n for m in 'ABC' for n in 'XYZ']
print(combined_letters)

# there must be an equation before the for loop
l1 = [x if x % 2 == 0 else -x for x in range(1,11)]
print(l1)

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]

# Generator
# Generator is a way to generate a list without storing all the elements
# so that it can save memory.
# A simple way to generate a generator is to use () on list comprehension
g = (i * i for i in range(10))
print(g)
print(next(g))

# generator is also iterable
for i in g:
    print(i)

# Function way to define fibonacci
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n += 1
    return 'Exceed max'

# Generator way to define fibonacci
# "A normal function executes sequentially and returns when 
# it encounters a return statement or reaches the last line of the 
# function. In contrast, a function that becomes a generator 
# executes each time next() is called. It returns when it encounters 
# a yield statement, and the next time it is executed, it resumes 
# from where the previous yield statement left off."
def fib_gen(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1
    return 'Exceed max'

# Call a generator function will generate a generator
f = fib_gen(6)
for i in f:
    print(i)

def pascal_triangle():
    # Initilization
    a, b = [1], [1,1]
    while True:
        yield a
        a = b
        b = [1] + [a[i] + a[i+1] for i in range(len(a) - 1)] + [1]
n = 0
results = []
for t in pascal_triangle():
    results.append(t)
    n = n + 1
    if n == 10:
        break

for t in results:
    print(t)

if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('Pass the test!')
else:
    print('Fail to pass the test!')

# Iterator
# An object that can be called by the next() function and keeps 
# returning the next value is called an iterator: Iterator.

if __name__ == '__main__':
    print(trim('  hello  '))
    print(trim('  hello'))
    print(trim('hello  '))