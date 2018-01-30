# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 14:28:30 2018
@author: joshm
"""
class myDict(object):
    """ Implements a dictionary without using a dictionary """
    def __init__(self):
        """ initialization of your representation """
        self.dict = []
        
    def assign(self, k, v):
        """ k (the key) and v (the value), immutable objects  """
        if self.dict == []:
            self.dict.append([k, v])
        else:
            for tup in self.dict:
                if tup[0] == k:
                    tup[1] = v
                else:
                    self.dict.append([k, v])
        
    def getval(self, k):
        """ k, immutable object  """
        for tup in self.dict:
            if k == tup[0]:
                return tup[1]
            
        raise KeyError('boom goes the dynamite')
        
    def delete(self, k):
        """ k, immutable object """   
        for tup in self.dict:
            if k == tup[0]:
                self.dict.remove(tup)
                
                
        raise KeyError('boom goes the dynamite')

md = myDict()
md.assign(1,2)
md.assign(1,4)
md.assign(3,4)
md.assign(5,4)
md.delete(5)
print(md.dict)
print(md.getval(3))