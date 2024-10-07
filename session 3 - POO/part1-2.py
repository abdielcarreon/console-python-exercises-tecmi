

import random

class Person:
    __name = "No name catch"
    __age = 0
    __identification = 0
    __sex = 0
    __height = 1
    __weight = 1
    
    def __init__(self, name, age, identification, sex, height, weight):
        self.__name = name
        self.__age = age
        self.__identification = identification
        self.__sex = sex
        self.__height = height
        self.__weight = weight
        
    
    # def name(self, name):
    #     self.__name = name
    #     return self.__name 
 
    
    # def age(self, age):
    #     self.__age = age
    #     return self.__age
        
    
    # def identification(self, identification):
    #     self.__identification = identification
    #     return self.__identification 
    
    
    # def sex(self, sex):
    #     self.__sex = sex
    #     return self.__sex 
        
    
    # def height(self, height):
    #     self.__height = height
    #     return self.__height 
        
    
    # def weight(self, weight):
    #     self.__weight = weight
    #     return self.__weight 
        
    # Part 1
    # def calculate(self):
    #     ideal_weight = self.__weight / (self.__height ** 2)
    #     print(ideal_weight)
    #     if ideal_weight < 20:
    #         print("You are under your ideal weight")
    #     if ideal_weight > 19 and ideal_weight < 26:
    #         print("You are in your ideal weight")
    #     if ideal_weight > 25:
    #         print("You are over your ideal weight")
            
            
    def adult(self):
        return self.__age >= 18
    
    def validate_sex(self):
        if self.__sex.lower() != 'male' and self.__sex.lower() != 'female':
            self.__sex = 'undefined'
    
    def random(self):
        if self.__identification == "0" or self.__identification == '':
            self.__identification = int(random.random() * 1000)
             
    def prnt(self):
        print("The person with name:", self.__name,"(","id -",self.__identification,")", "- sex:", self.__sex, "it's", self.__age, "years old and", "whose height is", self.__height, "and weight to", self.__weight,"has been registered as")
        
        
name = input("Enter your name: ")
age = int(input('Enter your age: '))
identification = input('Enter your ID: ')
sex = input('Enter sex which you feel identification(male, female, other): ')
height = input('Enter your height: ')
weight = input('Enter your weight: ')

person1 = Person(name, age, identification, sex, height, weight)

if person1.adult():
    validingAge = 'Adult'
else:
    validingAge = 'Under-age'

print(name, "is", validingAge)

person1.validate_sex()
person1.random()
person1.prnt()

