'''
Created on 31 Mar 2015

@author: WMOORHOU
'''
from ProjectScraper import ProjectScraper
from src.PomParser import PomParser

class ProjectActions(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def visualiseProject(self, loc):
        
        ''' Get poms in project'''
        scraper = ProjectScraper()
        pomLocs = scraper.getProjectPomList(loc)
        
        ''' Parse XML into some Pom POPOs'''
        pomparser = PomParser()
        pomPOPOs = pomparser.parseFilesToPomPOPO(pomLocs)
        ''' Process POPOs to determine dependencies '''
        
        ''' Create POPO structure '''
        
        ''' Pass POPO structure to visualiser '''