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
        if rootNode:
            self.drawNode(rootNode, 0)
            
        ''' iterate over pom dependency structure'''
    def drawNode(self, node, level):
        
        ''' node.get name etc render at this level'''
        
        
        if node.getChildNodes():
            for child in node.getChildNodes():
                self.drawNode(child, level+1)
        
    def renderNode(self, node):
        #self._display.drawSquare(x_loc, y_loc, width, height)
        print(node.getArtifactId())
