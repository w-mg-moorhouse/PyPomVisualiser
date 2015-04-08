'''
Created on 31 Mar 2015

@author: WMOORHOU
'''

from xml.dom.minidom import parse
from src.pom.Pom import PomDependency, Pom

class PomParser(object):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
        
    def parseFilesToPomPOPO(self, listOfFileLocs):
        popos = []
        for file in listOfFileLocs:
            tmpDom = parse(file)
            popos.append(self.DomToPOPO(tmpDom, file))
            tmpDom.unlink()
        return popos   
    
    def DomToPOPO(self, dom, file):
        pomDeps = []
        
        par = dom.getElementsByTagName("parent")
        grp = par.getAttribute("groupId")
        art = par.getAttribute("artifactId")
        ver = par.getAttribute("version")
        relPath = par.getAttribute("relativePath")
        parent = Pom(grp, art, ver, relPath)
            
        pomGrp = dom.getElementsByTagName("groupId")
        pomArt = dom.getElementsByTagName("artifactId")
        pomVer = dom.getElementsByTagName("version")
        
        depMan = dom.getElementsByTagName("dependencyManagement")
        if depMan:
            deps = depMan.getElementsByTagName("dependencies")
        else:
            deps = dom.getElementsByTagName("dependencies")
            
        for dep in deps:
            depGrp = dep.getAttribute("groupId")
            depArt = dep.getAttribute("artifactId")
            depVer = dep.getAttribute("version")
            pomDeps.append(PomDependency(depGrp, depArt, depVer))
        
        mods = dom.getElementsByTagName("modules")
        pomMods = []
        for mod in mods:
            pomMods.append(mod.getAttribute("module"))
            
        return Pom(pomGrp, pomArt, pomVer, file, parent, pomDeps, pomMods)
    
class PomTreeNode(object):

    parentNode = None
    data = None
    artifactId = None
    groupId = None
    ''' stores a set of keys'''
    _childNodes = []
    _reverseChildren = []
    
    def __init__(self, artId, groupId, data=None, childnodes=[], parent=None):
        self.artifactId = artId
        self.groupId = groupId
        self.parentNode = parent
        self._childNodes = childnodes
        self.data = data
    
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
    
    def setParentNode(self, node):
        self.parentNode = node

    def getChildNodes(self):
        return self._childNodes
    
    def addChildNode(self, node):
        assert type(node) is PomTreeNode
        self._childNodes.append(node)
    
    def getReverseChildNodes(self):
        return self._reverseChildren
    
    def addReverseChildNode(self, node):
        assert type(node) is PomTreeNode
        self._reverseChildren.append(node)
    
        
class TreeCreation(object):
    
    rootNode = None
    nodeList = []
    
    def __init__(self, listOfPoms):
        ''' '''
        self.resolveTreeStructure(listOfPoms)
        
                
    def resolveTreeStructure(self, listOfPoms):
        nodeList = []
        for pom in listOfPoms:
            pomArt = pom.getArtifactId()
            pomGrp = pom.getGroupId()
            tmpnode = PomTreeNode(pomArt, pomGrp, pom)
            
            '''determines if pom has parent, if it does, determine if in nodeList and add as parentNode'''
            if pom.getParentPom():
                parPom = pom.getParentPom()
                parPomNode = PomTreeNode(parPom.getArtifactId(), parPom.getGroupId())
                par = self.inNodeList(parPomNode)
                if not par:
                    par = parPomNode
                nodeList.append(par)
                tmpnode.setParentNode(par)
            ''' #################### '''
                
            ''' If node is in found list then use that, if not make a new one'''
            found = self.inNodeList(tmpnode)
            if found:
                tmpnode = found
                if not tmpnode.getData():
                    tmpnode.setData(pom)
            ''' #################### '''
            
            ''' determine if any nodes match the dependencies and then add child nodes accordingly'''
            for dep in pom.getDependencies():
                for inner in listOfPoms:
                    if (inner.getGroupId() is dep.getGroupId()) and (inner.getArtifactId() is dep.getArtifactId()):                        
                        ''' inner is dependency, make node which refers to this.'''
                        innerNode = PomTreeNode(inner.getArtifactId, inner.getGroupId())
                        foundNode = self.inNodeList(nodeList, innerNode)
                        if not foundNode:
                            nodeList.append(innerNode)
                            foundNode = innerNode    
                        # Add reverse dependency assignment
                        tmpnode.addChildNode(foundNode)
                        foundNode.addReverseChildNode(tmpnode)
                        break
                # TODO cater for external dependencies
                
            ''' ################### '''
            nodeList.append(tmpnode)
        self.nodeList = nodeList
    
    def inNodeList(self, nodeList, nodeToFind):
        for node in nodeList:
            if (node.getGroupId() is nodeToFind.getGroupId()) and (node.getArtifactId() is nodeToFind.getArtifactId()):
                return node
    
    def resolveRootNode(self):
        length = len(self.nodeList)
        if length > 0:
            if length is not 1:
                ''' more than 1 node'''
                active = self.nodeList[0]
                assert type(active) is PomTreeNode
                # May need more work
                self.resolveRootNode(active)    
            else:
                self.rootNode = self.nodeList[0]
                return                
        else:
            ''' throw exception'''
    
    def resolveNodeRelations(self, node):
        if node.getParent():
            self.amIRootNode(node.getParent)
        elif node.getReverseChildNodes():
            ''' Needs to follow these, maybe one, maybe all'''
        else:
            self.rootNode = node
            ''' Could be root node'''
            
    def getRootNode(self):
        return self.rootNode    
