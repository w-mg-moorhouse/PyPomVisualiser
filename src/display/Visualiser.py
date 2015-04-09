'''
Created on 31 Mar 2015

@author: WMOORHOU
'''
from src.display.WindowManager import WindowManager

class Visualiser(object):
    '''
    classdocs
    '''
    

    def __init__(self):
        self.manager = WindowManager()
        '''
        Constructor
        '''
    
    def visualisePomStructure(self, rootNode):
        ''' calculate number of nodes '''
        if rootNode:
            self.extractNodes(rootNode, 0)
    
        self.manager.finalise()
    
        ''' iterate over pom dependency structure'''
    def extractNodes(self, node, level):
        
        self.manager.drawNode(level, node)
        ''' node.get name etc render at this level'''
        
        if node.getChildNodes():
            for child in node.getChildNodes():
                self.manager.drawNode(level+1, child)
                self.manager.connectNodes(node, child)
                
        if node.getDependencies():
            for child in node.getDependencies():
                self.manager.drawNode(level+1, child)
                self.manager.connectNodes(node, child)
