from dao.ReferenceDAO import *
from model import ReferenceM

class References:
    @staticmethod
    def getReferences():
        try:
            reference_dao = ReferencesDAO()
            references = reference_dao.findAll()
            return references
        except Exception as e:
            print(f'Error_References.getReferences() ::: {e}')
    

    @staticmethod
    def getReference(referenceId):
        try:
            reference_dao = ReferencesDAO()
            reference = reference_dao.findById(referenceId)
            return reference
        except Exception as e:
            print(f'Error_References.getReference() ::: {e}')

    @staticmethod
    def update(referenceId,referencePublication):
        try:
            reference = ReferencesDAO().findById(referenceId)
            reference.setReference(referencePublication)
            result = ReferencesDAO().update(reference)

            if result!= 0:
                return "Reference updated successfully"
            else:
                return "Error updating reference"

        except Exception as e:
            print(f'Error_References.update() ::: {e}')

    @staticmethod
    def deleteReference(referenceId):
        try:
            result = ReferencesDAO().deleteById(referenceId)

            if result!= 0:
                return "Reference deleted successfully"
            else:
                return "Error deleting reference"

        except Exception as e:
            print(f'Error_References.delateReference() ::: {e}')
    
    
    @staticmethod
    def addReference(reference, publication):
        try:
            reference_dao = ReferencesDAO()
            new_reference = ReferenceM.Reference()
            new_reference.setReference(reference)
            new_reference.setPublication(publication)
            result = reference_dao.create(new_reference)

            if result!= 0:
                return "Reference added successfully"
            else:
                return "Error adding reference"

        except Exception as e:
            print(f'Error_References.addReference() ::: {e}')