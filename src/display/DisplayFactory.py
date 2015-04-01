'''
Created on 31 Mar 2015

@author: WMOORHOU
'''
from os import name
from display.Win32Display import Win32Display

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
        
        
