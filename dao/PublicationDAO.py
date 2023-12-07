from dao import ModelDAO
from model.PublicationM import Publication

class PublicationDAO(ModelDAO.modeleDAO):

    def __init__(self):

        params=ModelDAO.modeleDAO.connect_object
        self.cur=params.cursor()

      # INSERT

    def create(self, publication)->int:
        pass


    # SELECT
    def findById(self, publicationId)->object:
        pass


    def findAll(self)->list:
        pass
    
    def findByCity(self, city)->list:
        pass

    def findByCategory(self, category)->object:
        pass
    
    def findByLink(self, link)->object:
        pass

    # UPDATE


    def update(self, publication)->int:
        pass

    # DELETE


    def deleteById(self, publicationId)->int:
        pass


    def deleteAll(self)->int:
        pass