'''
Created on 30 Mar 2015

@author: WMOORHOU
'''
from ProjectScraper import ProjectScraper
from display.DisplayFactory import DisplayFactory

def run():
    scraper = ProjectScraper()
    ''' gets all poms in project'''
    for loc in scraper.getProjectPomList(r"D:\Users\wmoorhou\Documents\workspace"):
        print(loc)

    display = DisplayFactory.getDisplayMechanism()
    display.drawSquare(20, 40, 20, 20)
    display.runDisplay()
    
if __name__ == '__main__':
    run()