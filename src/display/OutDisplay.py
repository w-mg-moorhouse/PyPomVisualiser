'''
Created on 31 Mar 2015

@author: WMOORHOU
'''
from abc import ABCMeta, abstractmethod

class OutDisplay:
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def drawSquare(self, x_loc, y_loc, width, height):
        return
    
    @abstractmethod
    def drawCircle(self, x_loc, y_loc, width, height):
        return
    
    @abstractmethod
    def runDisplay(self):
        return