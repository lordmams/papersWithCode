from dao import ModelDAO
from model.ReferencesM import References

class ReferencesDAO(ModelDAO.modeleDAO):
    def __init__(self):

        params = ModelDAO.modeleDAO.connect_objet
        self.cur = params.cursor()

    def add_reference(self):
        pass


    def insert_reference(self, objIns: References) -> int:

        pass

    def insert_multiple_references(self, objInsList: list[References]) -> int:

        pass

    def find_one(self, reference_id) -> References:

        pass

