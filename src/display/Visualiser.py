'''
Created on 31 Mar 2015

@author: WMOORHOU
'''
from src.display.DisplayFactory import DisplayFactory

class Visualiser(object):
    '''
    classdocs
    '''
    _display = None
    _rendered = []

    def __init__(self):
        self._display = DisplayFactory.getDisplayMechanism()
        '''
        Constructor
        '''
    
    def visualisePomStructure(self, rootNode):
        ''' calculate number of nodes '''
        
        ''' iterate over pom dependency structure'''
        
    def renderNode(self, node):
        self._display.drawSquare(x_loc, y_loc, width, height)
        
class RenderedObject(object):
    
    def __init__(self, x_pos, y_pos, width, height):
        self.x1_pos = x_pos
        self.x2_pos = y_pos
        self.width = width
        self.height = height
