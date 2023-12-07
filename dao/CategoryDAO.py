from dao import ModelDAO
from model.CategoryM import Category

class PublicationDAO(ModelDAO.modeleDAO):

    def __init__(self):

        params=ModelDAO.modeleDAO.connect_object
        self.cur=params.cursor()

      # INSERT

    def create(self, category)->int:
        pass


    # SELECT
    def findById(self, category)->object:
        pass


    def findByName(self)->list:
        pass
    # UPDATE


    def update(self, category)->int:
        pass

    # DELETE


    def deleteById(self, category)->int:
        pass


    def deleteAll(self)->int:
        pass