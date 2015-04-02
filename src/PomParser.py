'''
Created on 31 Mar 2015

@author: WMOORHOU
'''

from xml.dom.minidom import parse
from src.pom.Pom import PomDependency, Pom
from ctypes import cast

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
    
class TreeNode(object):

    parentNode = None
    data = None
    _childNodes = []
    
    def __init__(self, data, childnodes = [], parent = None):
        self.parentNode = parent
        self._childNodes = childnodes
        self.data = data
    
    def getData(self):
        return self.data
    
    def getParent(self):
        return self.parentNode
    
    def getChildNodes(self):
        return self._childNodes
    
    def addChildNode(self, node):
        assert type(node) is TreeNode
        assert type(node.getData) is Pom
        self._childNodes.append(node)
    
    def addParentNode(self, node):
        self.parentNode = node
        
class TreeCreation(object):
    
    rootNode = None
    nodes = []
    
    def __init__(self, listOfPoms):
        arts = {}
        for pom in listOfPoms:
            
            
            
            arts[pom.getArtifactId()] = pom
        self.findRootParent(arts)
        ''' '''
        
        
    def findRootParent(self, arts):
        for val in arts.itervalues():
            assert type(val) is Pom
            par = val.getParent()
            assert type(par) is Pom
            if par:
                par.getArtifactId()
    
    def getRootNode(self):
        return self.rootNode    
