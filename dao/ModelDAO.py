from abc import ABC, abstractmethod
#from dao.ConnexionDAO import ConnexionBD

class modeleDAO(ABC):

    #connect_objet = ConnexionBD().getConnexion()

    ### CRUD

    # INSERT

    @abstractmethod
    def create(self, objIns)->int:
        pass


    # SELECT

    @abstractmethod
    def findById(self, cleTrouv)->object:
        pass

    @abstractmethod
    def findAll(self)->list:
        pass


    # UPDATE

    @abstractmethod
    def update(self,  objModif)->int:
        pass

    # DELETE

    @abstractmethod
    def deleteById(self, cleSup)->int:
        pass

    @abstractmethod
    def deleteAll(self)->int:
        pass

