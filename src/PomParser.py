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
    
class PomStructure(object):

    def __init__(self):
        ''''''
    
        