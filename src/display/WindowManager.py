'''
Created on 9 Apr 2015

@author: WMOORHOU
'''

from display.DisplayFactory import DisplayFactory
from array import array
from enum import Enum

class WindowManager(object):
    '''
    classdocs
    '''
    rendered=dict()
    
    spacing = 14
    baseSize = 10
    scale = 10
    levelCounter = dict()
    
    def __init__(self):
        self._display = DisplayFactory.getDisplayMechanism()
        self.spacing = self.scale * self.spacing
        self.baseSize = self.scale * self.baseSize
        '''
        Constructor
        '''
    
    def drawNode(self, level, node):
        
        print("Level :"+str(level))
        #if node is X make blue etc
        if level is 0:
            x_loc = 0
            y_loc = (level+1)*self.spacing
            width = self.baseSize
            self.rendered[node] = self._display.drawSquare(x_loc, y_loc, width, self.baseSize, "#FFFF00")
            self._display.drawText(x_loc, y_loc, width, self.concatNodeInfo(node))
            
        else:
            if level not in self.levelCounter:
                self.levelCounter[level] = 0
            else:
                self.levelCounter[level] = self.levelCounter[level] + 1
            x_loc = self.levelCounter[level]*self.spacing
            y_loc = (level+1)*self.spacing
            width = self.baseSize 
            self.rendered[node] = self._display.drawCircle(x_loc, y_loc, width, self.baseSize, node.getType().value)
            self._display.drawText(x_loc, y_loc, width, self.concatNodeInfo(node))
    
    def concatNodeInfo(self, node):
        content = node.getArtifactId() + "\n"
        content += node.getGroupId() + "\n"
        #content += node.getVersion()
        return content
    
    def connectNodes(self, master, slave):
        masterId = self.rendered.get(master)
        slaveId = self.rendered.get(slave)
        if masterId and slaveId:
            print(masterId)
            print(slaveId)
            lineval = self._display.connectIdWithLine(masterId, slaveId)
        else:
            print("Node values could not be extracted from render list, no joining will be done")        
        #could do with storing
        
    def finalise(self):
        self._display.runDisplay()
        pass




def nodeInformation(node):
    nodeStrings = []
    def nodeInfo():
        nodeStrings.append(node.getArtifactId())
    return nodeStrings