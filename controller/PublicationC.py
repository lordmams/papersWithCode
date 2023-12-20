from dao.PublicationDAO import *
from model import PublicationM
from controller import CategoryC, CityC

class Publications:

    @staticmethod
    def getPublications():
        try:
            publication_dao = PublicationDAO()
            publications = publication_dao.findAll()
            return publications
        except Exception as e:
            print(f'Error_Publications.getPublications() ::: {e}')
    @staticmethod
    def getPublication(publicationId):
        try:
            publication_dao = PublicationDAO()
            publication = publication_dao.findById(publicationId)
            return publication
        except Exception as e:
            print(f'Error_Publications.getPublication() ::: {e}')
    @staticmethod
    def addPublication(link, city,category):
        try:
            publication_dao = PublicationDAO()

            
            cityId = Publications.checkCity(city)
            categoryId = Publications.checkCategory(category)
            
            new_publication = PublicationM.Publication()
            new_publication.setPublicationLink(link)
            new_publication.setPublicationCity(cityId)
            new_publication.setPublicationCategory(categoryId)
            result = publication_dao.create(new_publication)

            if result!= 0:
                return "Publication added successfully"
            else:
                return "Error adding publication"
        except Exception as e:
            print(f'Error_Publications.addPublication() ::: {e}')
    @staticmethod     
    def updatePublication(publicationId, changeList):
        try:
            publication = PublicationDAO().findIds(publicationId)
            if publication is not None:
                if changeList['link'] is not None:
                  
                    publication.setPublicationLink(changeList['link'])
                    
                if changeList['category'] is not None:
                    categoryId = Publications.checkCategory(changeList['category'] )
                    publication.setPublicationCategory(categoryId)

                if changeList['city'] is not None:
                    cityId = Publications.checkCity(changeList['city'])
                    publication.setPublicationCity(cityId)

                print(publication.getPublicationCity())
                PublicationDAO().update(publication)
                return "Publication updated successfully"
            else:
                return "Error updating publication"
        except Exception as e:
            print(f'Error_Publications.updatePublication() ::: {e}')
    @staticmethod
    def deletePublication(publicationId):
        try:
            publication_dao = PublicationDAO()
            publication = publication_dao.findById(publicationId)
            if publication is not None:
                PublicationDAO().deleteById(publicationId)
                return "Publication deleted successfully"
            else:
                return "Error deleting publication"
        except Exception as e:
            print(f'Error_Publications.deletePublication() ::: {e}')

    @staticmethod
    def getPublicationReference(publicationId):
        try:
            publication_dao = PublicationDAO()
            publication = publication_dao.findPublicationReference(publicationId)
            return publication
        except Exception as e:
            print(f'Error_Publications.findPublicationReference() ::: {e}')

    @staticmethod
    def getPublicationIsRefer(publicationId):
        try:
            publication_dao = PublicationDAO()
            publications = publication_dao.findPublicationIsRefer(publicationId)
            return publications
        except Exception as e:
            print(f'Error_Publications.findPublicationIsRefer() ::: {e}')

    @staticmethod
    def getPublicationCitations(publicationId):
        try:
            publication_dao = PublicationDAO()
            publicationCitations = publication_dao.findPublicationCitations(publicationId)
            return publicationCitations
        except Exception as e:
            print(f'Error_Publications.findPublicationCitations() ::: {e}')

    def checkCategory(categoryName):
        category = CategoryC.Category.getCategoryByName(categoryName)
        if category is None :
            CategoryC.Category.addCategory(categoryName)
            category = CategoryC.Category.getCategoryByName(categoryName)
        return category.getCategoryId()
    
    def checkCity(cityName):
        city = CityC.Cities.getCityByName(cityName)
        if city is None :
            CityC.Cities.addCity(cityName)
            city = CityC.Cities.getCityByName(cityName)
        return city.getCityId()