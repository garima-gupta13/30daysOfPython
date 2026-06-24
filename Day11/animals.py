# class allows to have control of STATE
#classes allows to attach state like items to them
# a liittle bit better understadning about the classes like noise ,color...as below
# alos helps in proper clean and reusability increases
# STATE as in each object will ahve its own state -- like memory mai sepaarte location pe assign -- like saw in CLass -in JAVA in college - shantanu sir
# 
class Animal:
    noise ="Rrrr"
    color = "red"
    def make_noise(self):
        print("hello")
    
    def set_noise(self, new_noise):
        self.noise = new_noise
        return self.noise
    
    def set_color(self, new_color):
        self.color = new_color
        return self.color
    
    def rando():
        print("This")

#inheritance  -- all deafult methods and proeprty are inherited
class Wolf(Animal):
    noise = "grrr"

class BabyWolf(Wolf):
    color = "yellow"


#     PS D:\33_Fulltime-resume\1-Preparation\Data Engineer\Python_Learning\30daysOfPython\Day11> python -i animals.py
# >>> Animal
# <class '__main__.Animal'>
# >>> Animal() 
# <__main__.Animal object at 0x000001591D804830>
# >>> exit()
# PS D:\33_Fulltime-resume\1-Preparation\Data Engineer\Python_Learning\30daysOfPython\Day11> python -i animals.py
# >>> Animal.rando()
# This
# >>> Animal.make_noise()    --- 1st an instance has to be created for this to run,, as calling self, so needs object
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     Animal.make_noise()
#     ~~~~~~~~~~~~~~~~~^^
# TypeError: Animal.make_noise() missing 1 required positional argument: 'self'
# >>> Animal().make_noise()
# hello
# >>> 


##creating instance / instantiating the class
##  Animal()
## and can assign to a variable if needed -- obj = Animal()