from dao import ModelDAO
from model.CitationsM import Citation

class CitationDAO(ModelDAO.modeleDAO):
    def __init__(self):
        params=ModelDAO.modeleDAO.connect_object
        self.cur=params.cursor()

    # INSERT

    def create(self, citation)->int:
        pass


    # SELECT
    def findById(self, citationId)->object:
        pass


    def findAll(self)->list:
        pass

    # UPDATE


    def update(self, citationId)->int:
        pass

    # DELETE


    def deleteById(self, citationId)->int:
        pass


    def deleteAll(self)->int:
        pass