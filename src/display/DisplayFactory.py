'''
Created on 31 Mar 2015

@author: WMOORHOU
'''
from os import name

from src.display.Win32Display import *

class DisplayFactory(object):
    '''
    classdocs
    '''
    @staticmethod
    def getDisplayMechanism():
        if name is "nt":
            display = Win32Display()
            return display
        else:
            '''Not nt therefore likely to be posix'''
            return
        
        
from abc import ABCMeta, abstractmethod

class Display:
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def drawSquare(self, x_loc, y_loc, width, height):
        pass
    
    @abstractmethod
    def drawCircle(self, x_loc, y_loc, width, height):
        pass
    
    @abstractmethod
    def drawLine(self):
        pass
    
    @abstractmethod
    def runDisplay(self):
        pass
        
    @abstractmethod    
    def remove(self, num):
        pass