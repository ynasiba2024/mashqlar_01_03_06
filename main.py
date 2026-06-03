class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

s1 = Student("Ali", 18)
print(s1.age)
s1.age = 20
print(s1.age)
