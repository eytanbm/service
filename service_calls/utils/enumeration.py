'''
Created on Apr 18, 2015

@author: eytan

Immutable enum class

Usage example:
e = Enumeration('A', 'B', 'C')

e.A returns 1
e.B returns 2
e.C returns 3

e.to_choices returns ((1, 'A'), (2, 'B'), (3, 'C'))

e.before(e.B) returns e.A
e.after(e.B) returns e.C

e.after(e.C) returns None
e.before(e.A) returns None

e.name(e.A) returns 'A' 
e.name(1) returns 'A'

'''

class  Enumeration(dict):
    __getattr__= dict.__getitem__
    __setattr__= dict.__setitem__
    __delattr__= dict.__delitem__
    
    def __init__(self, *args):
        self.clear()
        self.choices = tuple([(x[0] + 1, (x[1] if isinstance(x[1], basestring) else x[1][1])) for x in enumerate(args)])
        real_args = [(x[0] + 1, (x[1] if isinstance(x[1], basestring) else x[1][0])) for x in enumerate(args)]
        self.update({x[1]:x[0] for x in real_args})
        self.update({x[0]:x[1] for x in real_args})
        
    def to_choices(self):
        return self.choices
    
    def after(self, val):
        return self[self[val + 1]] if val + 1 in self.keys() else None
    
    def before(self, val):
        return self[self[val - 1]] if val - 1 in self.keys() else None
    
    def name(self, val):
        return self[val] if val in self.keys() else None
    
#    Ensure immutability
    
    def __setitem__(self, i, y):
        raise Exception("Enumeration is immutable!")
       
    def __delitem__(self, i, y):
        raise Exception("Enumeration is immutable!")
    
    def __delattr__(self, y):
        raise Exception("Enumeration is immutable!")
    