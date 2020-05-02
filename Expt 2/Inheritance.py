# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 16:04:13 2020

@author: centeno
"""

class A:
    def __init__(self, age=12):
       self.age = age
      
          
class B(A):
    age = 20
    def __str__(self, age):
        return "Age: " + str(self.age)
    
b1 = B()

print(b1.__str__(20))
