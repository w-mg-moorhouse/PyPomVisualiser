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
        current = None
        try:
            for file in listOfFileLocs:
                current = file
                tmpDom = parse(file)
                if tmpDom:
                    popos.append(self.DomToPOPO(tmpDom, file))
                    tmpDom.unlink()
            return popos   
        except Exception:
            raise PomParseError("Parser was unable to parse from file location: " + current)
            
    
    def DomToPOPO(self, dom, file):
        pomDeps = []
        parent = None
        par = dom.getElementsByTagName("parent")
        if par:
            par = par[0]
            grp = self.getNodeValue(par.getElementsByTagName("groupId"))
            art = self.getNodeValue(par.getElementsByTagName("artifactId"))
            ver = self.getNodeValue(par.getElementsByTagName("version"))
            relPath = self.getNodeValue(par.getElementsByTagName("relativePath"))
            parent = Pom(grp, art, ver, relPath)
                
        pomGrp = self.getNodeValue(dom.getElementsByTagName("groupId"))
        pomArt = self.getNodeValue(dom.getElementsByTagName("artifactId"))
        pomVer = self.getNodeValue(dom.getElementsByTagName("version"))
        
        depMan = dom.getElementsByTagName("dependencyManagement")
        if depMan:
            deps = depMan.getElementsByTagName("dependencies")
        else:
            deps = dom.getElementsByTagName("dependencies")
        
        for no in deps:
            tmps = no.getElementsByTagName("dependency")
            for dep in tmps:
                #dep = tmp.getElementsByTagName("dependency")
                if dep:
                    depGrp = self.getNodeValue(dep.getElementsByTagName("groupId"))
                    depArt = self.getNodeValue(dep.getElementsByTagName("artifactId"))
                    depVer = self.getNodeValue(dep.getElementsByTagName("version"))
                    pomDeps.append(PomDependency(depGrp, depArt, depVer))
            
        mods = dom.getElementsByTagName("modules")
        pomMods = []
        for mod in mods:
            pomMods.append(self.getNodeValue(mod.getElementsByTagName("module")))
            
        return Pom(pomGrp, pomArt, pomVer, file, parent, pomDeps, pomMods)
    
    def getNodeValue(self, elementByTag):
        if elementByTag:
            if len(elementByTag) > 0:
                elementByTag = elementByTag[0]
                if len(elementByTag.childNodes) > 0:
                    elementByTag = elementByTag.childNodes[0]
                    return elementByTag.nodeValue
    
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
                par = self.inNodeList(nodeList, parPomNode)
                if not par:
                    par = parPomNode
                nodeList.append(par)
                tmpnode.setParentNode(par)
            ''' #################### '''
                
            ''' If node is in found list then use that, if not make a new one'''
            found = self.inNodeList(nodeList, tmpnode)
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
        self.resolveRootNode()
        ''' Count number of layers maybe?'''
    
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
                self.resolveNodeRelations(active)
            else:
                self.rootNode = self.nodeList[0]
                return                
        else:
            ''' throw exception'''
            raise PomParseError("Resolution of RootNode failed as the structure is empty")
    
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
    
class PomParseError(Exception):
    
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)