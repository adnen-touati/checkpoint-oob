#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Parrot:
    # class attribute
    species = "bird"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

# instantiate the Parrot class
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

# access the class attributes
print("Blu is a {}".format(blu.__class__.species))
print("Woo is also a {}".format(woo.__class__.species))

# access the instance attributes
print("{} is {} years old".format( blu.name, blu.age))
print("{} is {} years old".format( woo.name, woo.age))


# In[2]:


class Parrot:
    
    # instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # instance method
    def sing(self, song):
        return "{} sings {}".format(self.name, song)

    def dance(self):
        return "{} is now dancing".format(self.name)

# instantiate the object
blu = Parrot("Blu", 10)
my_point=point3D(1,2,3)

# call our instance methods
print(blu.sing("'Happy'"))
print(blu.dance())


# In[10]:


# parent class
class Bird:
    
    def __init__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")


    def swim(self):
        print("Swim faster")

# child class
class Penguin(Bird):

    def __init__(self):
# call super() function
        super().__init__()
        print("Penguin is ready")

    def whoisThis(self):
        print("Penguin")

    def run(self):
        print("Run faster")

peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()


# In[18]:


#Write a python class named Point3D defined by x, y, and z. Define a method that returns (x, y ,z). 
#This tells Python to represent this object in the following format: (x, y, z).
#then create a variable named my_point containing a new instance of Point3D with x=1, y=2, and z=3 and print it.

class point3D:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def afficher(self):
        print (self.x,self.y,self.z)
    
        
my_point=point3D(1,2,3)
my_point.afficher()
       
    
        
    


# In[30]:


#Write a Python class named Rectangle constructed by a length and width. 
#Define two methods area and perimeter which will compute the area and the perimeter of the rectangle. 
#Then create a variable named my_rectangle containing a new instance of Rectangle with width=3 and length = 4 
#compute both of area and perimeter ( the area is expected to be 3*4=12 and perimeter 2*(3+4)=14)


class rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        area_1=self.length*self.width
        print(area_1)
    def perimeter(self):
        perimeter_1=(self.length+self.width)*2
        print(perimeter_1)

        
        
rectangle_1=rectangle(3,4)
rectangle_1.perimeter()
rectangle_1.area()
    
    


# In[3]:


#Write a Python  class named Circle constructed by its center O and radius r.
#Define two methods area and perimeter which will compute the area and the perimeter of the circle, 
#and isInside() method of the class which allows to test whether a point A(x, y) belongs to the circle C(O, r) or not.
#perim=Diamètre x π 
#A = π r2.
# (x - h) 2 + (y - k) 2 = r 2
from math import pi    
class circle:
    def __init__(self,center, radius):
        self.center = center
        self.radius = radius
    def perim(self):
        perim_1=self.radius*2*pi 
        print(perim_1)
        
    def area(self):
        area_1=(self.radius**2)*pi
        print(area_1)
    def belong (self):
        x=int(input())
        y=int(input())
        if ((x - self.center)**2 + (y - self.center)**2 <= self.radius**2):
            print("C",(x,y),"belong to the circle")
        else:
            
            print("it doesen't belong to the cirlce")

circle_1=circle(0,3)
circle_1.area()

circle_1.perim()
circle_1.belong()



         
        


# In[5]:


#Suppose we want to model a bank account with support for deposit and withdraw operations. 
#Let’s create a python class named bank defined by its balance. 
#Define two methods deposit and withdraw to compute the new amount of each operation.


class bank:
    def __init__(self,balance):
        self.balance = balance
    def withdraw(self):
        x=int(input())
        balance_1= (self.balance - x)
        print(balance_1)
    def deposit (self):
        y=int(input())
        balance_2 = (self.balance - y) 
        print(balance_2)  
        
bank_1 = bank(30)
bank_1.withdraw()        
bank_1.deposit()        
    



# In[ ]:




