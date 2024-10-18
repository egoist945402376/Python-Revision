#list and tuple

#list
classmate = ['bob', 'jack', 'lily']
print(classmate)

for student in classmate:
    print(student)
    print(f"{student} is at index {classmate.index(student)}")

classmate.append('tom')
classmate.insert(1, 'jerry')
print(classmate)

student_take_a_leave = classmate.pop()
print(f"{student_take_a_leave} take a leave")

# changeble tuple
tu = (1, 2, [3, 4])
tu[2][0] = 5
tu[2][1] = 6
print(tu)

age = 12
match age:
    case x if x < 15:
        print("age is less than 15")
    case 15:
        print("Age is 15")
    case _:
        print("Age is not 15")

args = ['gcc', 'hello.c', '-o', 'hello']
match args:
    case['gcc']:
        print("gcc missing source file")
    case['gcc', file1, *file2]:
        print(f"compile {file1} and {file2}")
    case _:
        print("Invalid command")

class Circle:
    def __init__(self, radius):
        self.radius = radius

class rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

c1 = Circle(radius = 10)
r1 = rectangle(width = 10, height = 20)

def circleOrRectangle(obj):
    match obj:
        case Circle(radius = r):
            print(f"Circle with radius {r}")
        case rectangle(width = w, height = h):
            print(f"Rectangle with width {w} and height {h}")
        case _:
            print("Invalid shape")
circleOrRectangle(c1)

a = list(range(1,11))
print(a)
b = list(range(5,11))
print(b)
c = list(range(5))
print(c)


dict1 = {'a': 1, 'b': 2, 'c': 3}
del dict1['a']
dict1.pop('b')


# str is inmutable
a = 'abc'
b = a.replace('a', 'A')

print(a)
print(b)

# Explaination:
# a is just a reference to the string 'abc', not 'abc' itself
# replace method actually modify the string, and create a new string
# therefore, a still refer to 'abc', and we assign
# b to the new string 'Abc'
