import math

n1 = 255
n2 = 1000
n1_hex = hex(n1)
n2_hex = hex(n2)
print(n1_hex, n2_hex)


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

def quadratic(a, b, c):
    if b**2 - 4*a*c < 0:
        return 'No real root'
    else:
        x1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
        x2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)
        return x1, x2
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

def power(x , n = 2):
    result = 1
    while n > 0:
        n = n - 1
        result = result * x
    return result

def cals(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

# Variable keyword arguments
numbers = [1,2,3,4,5,6]
numbers2 = [2,3,4,5]
print(cals(1,2,3))

# use * before list or tuple to pass all elements of the list or tuple to the function
# as variable arguments
print(cals(*numbers))
print(cals(*numbers2))

# keyword arguments
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
# kw is a dictionary
person('Jack', '27', city='Tianjin', job='Engineer')

person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)

# use * to differentiate between positional arguments and keyword arguments
# * means that city and job parameters must be passed as keyword arguments
def person(name, age, *, city, job):
    print(name, age, city, job)

try:
    # Wrong call
    person("Alice", 30, "New York", "Engineer")
except TypeError as e:
    print(f"Caught an exception: {e}")

# Right way to call person:
person("Alice", 30, city="New York", job="Engineer")



def mul(x, y):
    return x * y

def mul(*numbers):
    if numbers == ():
        print('No numbers')
    s = 1
    for number in numbers:
        s = s * number
    return s

# Recursion
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

# Hanoi Tower
def Hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
    else:
        Hanoi(n-1, source, auxiliary, target)
        print(f"Move disk {n} from {source} to {target}")
        Hanoi(n-1, auxiliary, target, source)
Hanoi(3, 'A', 'C', 'B')

# Climb stairs
def stairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        return stairs(n-1) + stairs(n-2)

# Dynamic programming
def dyn_stairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    a = 1
    b = 2
    for i in range(3, n+1):
        a, b = b, a + b
    return b

