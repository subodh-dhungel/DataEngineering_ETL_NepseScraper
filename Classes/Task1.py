# 1. Write a Python program to create an instance of a
#  specified class and display the namespace of the said instance.

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age


person1 = Person("Subin", 25)

# print namespace
print(Person.__dict__) #Person class ko methods dine vayo
print(person1.__dict__) #person instance ko methods dine vayo
