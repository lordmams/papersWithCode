from dao.PublicationDAO import *
from model import *

class Publications:

    def getPublications():
        pass

    def getPublication(self, publicationId):
        pass

    def addPublication(self, link, city):
        pass

    def addPublications(self,publicationList):
        for publication in publicationList :
            self.addPublication(publication.link , publication.city)

    def updatePublication(self, publicationId, changeList):
        pass

    def deletePublication(self, publicationId):
        pass