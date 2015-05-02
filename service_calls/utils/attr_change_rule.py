'''
Created on Apr 25, 2015

@author: eytan
'''

class AttrChangeRule(object):
    
    def __init__(self, role, attr, from_value, to_value):
        self.role = role
        self.attr = attr
        self.from_value = from_value
        self.to_value = to_value
        
    def apply(self, user, request):
        if user.role != self.role: return False
        if request.get('attr') != self.attr: return False
        if request.get('from_value') != self.from_value: return False
        if request.get('to_value') != self.to_value: return False
        return True
