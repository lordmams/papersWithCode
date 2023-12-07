from dao.CategoryDAO import *
from model import *

class Publications:

    def getCategories():
        pass

    def getCategory(self, categoryId):
        pass

    def addCategory(self, name):
        pass

    def addCategories(self,categoriesList):
        for publication in categoriesList :
            self.addPublication(publication.link , publication.city)

    def updateCategory(self, categoryId, nameCategory):
        pass

    def deleteCategory(self, categoryId):
        pass