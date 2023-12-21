from abc import ABC, abstractmethod
from dao.ConnexionDAO import ConnexionBD

class modeleDAO(ABC):

    connect_object = ConnexionBD().getConnexion()
    user_connect = ConnexionBD().getUserConnection()
    token = ConnexionBD().getToken()
  
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

   

