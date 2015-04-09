'''
Created on 9 Apr 2015

@author: WMOORHOU
'''

from display.DisplayFactory import DisplayFactory

class WindowManager(object):
    '''
    classdocs
    '''
    rendered=dict()

    def __init__(self):
        self._display = DisplayFactory.getDisplayMechanism()
        '''
        Constructor
        '''
    
    def drawNode(self, level, node):
        self.rendered[node] = self._display.drawCircle(0, (level+1)*120, 100, 100)
        pass
    
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