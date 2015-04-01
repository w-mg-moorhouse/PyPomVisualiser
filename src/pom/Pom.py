'''
Created on 31 Mar 2015

@author: WMOORHOU
'''

class Pom(object):
    '''
    classdocs
    '''
    _groupId = None
    _artifactId = None
    _version = None
    _fileLoc = None
    _dependencies = []
    _modules = []
    _parent = None

    def __init__(self, groupId, artifactId, version, fileLoc, parent=None, dependencies=None, modules=None):
        self._groupId = groupId
        self._artifactId = artifactId
        self._version = version
        self._fileLoc = fileLoc
        if parent:
            self._parent = parent
        if dependencies:
            self._dependencies = dependencies
        
        if modules:
            self._modules = modules
        '''
        Constructor
        '''
    
    def getGroupId(self):
        return self._groupId
    
    def getArtifactId(self):
        return self._artifactId
    
    def getVersion(self):
        return self._version
    
    def getFileLocation(self):
        return self._fileLoc
    
    def getDependencies(self):
        return self._dependencies
    
    def getModules(self):
        return self._modules

    
class PomDependency(object):
    
    _groupId = None
    _artifactId = None
    _version = None
    
    def __init__(self, groupId, artifactId, version):
        self._groupId = groupId
        self._artifactId = artifactId
        self._version = version
        
    def getGroupId(self):
        return self._groupId
    
    def getArtifactId(self):
        return self._artifactId
    
    def getVersion(self):
        return self._version    
    
    
