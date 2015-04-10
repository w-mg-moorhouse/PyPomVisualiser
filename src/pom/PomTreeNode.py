'''
Created on 10 Apr 2015

@author: WMOORHOU
'''
class PomTreeNode(object):

    def __init__(self, artId, groupId, nodeType, data):
        self.artifactId = artId
        self.groupId = groupId
        self.parentNode = None
        self.dependencyNodes = []
        self._reverseDependencies = []
        self.childnodes = []
        if len(self.childnodes) != 0:
            raise Exception
        self.data = data
        self.type = nodeType
    
    def getGroupId(self):
        return self.groupId
    
    def getArtifactId(self):
        return self.artifactId

    def setData(self, data):
        self.data = data
    
    def getData(self):
        return self.data
    
    def getParent(self):
        return self.parentNode
    
    def setParentNode(self, thisnode):
        assert type(thisnode) is PomTreeNode
        self.parentNode = thisnode

    def getType(self):
        return self.type

    # reverse parent idea
    def addChildNodes(self, node):
        if node not in self.childnodes:
            self.childnodes.append(node)
            pass
        
    def getChildNodes(self):
        return self.childnodes
    
    def getDependencies(self):
        for each in self.dependencyNodes:
            print("dep " + each.getArtifactId())
            
        return self.dependencyNodes
    
    def addDependencyNode(self, node):
        assert type(node) is PomTreeNode
        for each in self.dependencyNodes:
            print("dep " + each.getArtifactId())
        if node not in self.dependencyNodes:
            self.dependencyNodes.append(node)
    
    def getReverseDependencyNodes(self):
        return self._reverseDependencies
    
    def addReverseDependencyNode(self, node):
        assert type(node) is PomTreeNode
        if node not in self._reverseDependencies:
            self._reverseDependencies.append(node)
    
