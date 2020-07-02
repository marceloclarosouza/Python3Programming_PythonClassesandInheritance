# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 09:23:47 2020

@author: mcsbi
"""
"""
Create a class called NumberSet that accepts 2 integers as input, and defines two instance variables: num1 and num2, which hold each of the input integers. Then, create an instance of NumberSet where its num1 is 6 and its num2 is 10. Save this instance to a variable t.
"""

class NumberSet:
    def __init__(self, init1, init2):
        self.num1 = init1
        self.num2 = init2
        
t = NumberSet(6,10)
        
        