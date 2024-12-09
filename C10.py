# Object Oriented Programming

class Student(object):
    def __init__(self, name, age, grade, major = 'Computer Science'):
        # data encapsulation

        # private attributes
        # By adding two underscores in front of the attribute name,
        # we are telling Python to make the attribute private.
        # that means the attribute is only accessible within the class.
        # can not be accessed from outside the class.
        # This ensures that external code cannot modify the internal state of the object
        # at will. 
        self.__name = name
        self.__age = age
        self.major = major
        self.grade = grade
        
        # Single underscore indicates that the attribute is protected.
        # you can still access it from external code, but it is a signal
        # that asks you don't access it directly.
        self._level = 'Freshman'
    
    # Method
    def get_grade(self):
        print(f"{self.__name} has a grade of {self.grade} in {self.major}.")

    # If we want to access the private attribute from outside
    # we can use some getter methods.
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    
    # If we want to modify the private attributes from external code
    # we can use some setter methods
    def set_name(self, name):
        self.__name = name
    def set_age(self, age):
        if age > 0 and age < 100:
            self.__age = age
        else:
            print('Invalid age!')

class exercise_student(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender
    def get_gender(self):
        return self.__gender
    def set_gender(self, gender):
        self.__gender = gender




if __name__ == '__main__':
    bart = Student('Bart', 21, 90)
    lisa = Student('Lisa', 20, 95, 'Mathematics')
    bart.get_grade()
    lisa.get_grade()

print('-----------------')
bart = exercise_student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')