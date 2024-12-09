# Inheritance and Polymorphism
class Animal(object):
    def run(self):
        print('Animal is running...')

# When both parent and child class have the same method
# the child class's method will override the parent class's method.
# This is called Polymorphism.

# When we define a class, we are actually defining a new data type.
class Dog(Animal):
    def run(self):
        print('Dog is running...')
    def eat(self):
        print('Dog is eating...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')
    def eat(self):
        print('Cat is eating...')

class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')

class Timer(object):
    def run(self):
        print('Start...')

# Polymorphism example
def run_twice(animal):
    animal.run()
    animal.run()

if __name__ == '__main__':
    dog = Dog()
    dog.run()
    print(isinstance(dog, Dog))

    cat = Cat()
    run_twice(cat)
    run_twice(dog)

    tortoise = Tortoise()
    run_twice(tortoise)
# No need to modify run_twice() function when we add a new class.
# A benefit of polymorphism is that when we need to pass an object, we only need to accept
# its parent class (Animal). Because Dog, Cat, and Tortoise are all type of Animal.
# Animal class has method run(), As long as it is an Animal class or subclass, 
# it will automatically call the run() method of the actual type, 
# which is what polymorphism means:

# Dynamic programming
# We dont have to pass Animal() class only, we can pass all classes that have run() method.
    clock = Timer()
    run_twice(clock)