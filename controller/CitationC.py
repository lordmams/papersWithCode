from dao.CitationDAO import *
from model import CitationM

class Citations:

    @staticmethod
    def getCitations():
        try:
            citation_dao = CitationDAO()
            citations = citation_dao.findAll()
            return citations
        except Exception as e:
            print(f'Error_Citations.getCitations() ::: {e}')
    @staticmethod
    def getCitation(citationId):
        try:
            citation_dao = CitationDAO()
            citation = citation_dao.findById(citationId)
            return citation
        except Exception as e:
            print(f'Error_Citations.getCitation() ::: {e}')
    @staticmethod
    def addCitation(citationPublication):
        try:
            citation_dao = CitationDAO()
            new_citation = CitationM.Citation()
            new_citation.setCitationPublication(citationPublication)
            result = citation_dao.create(new_citation)

            if result!= 0:
                return "Citation added successfully"
            else:
                return "Error adding citation"

        except Exception as e:
            print(f'Error_Citations.addCitation() ::: {e}')
    @staticmethod
    def updateCitation( citationPublication, citationId,token=None):
        try:
            citation = CitationDAO.findById(citationId)
            citation.setCitationPublication(citationPublication)
            if token == ModelDAO.modeleDAO.token:
                result = CitationDAO(0).update(citation)

            if result!= 0:
                return "Citation updated successfully"
            else:
                return "Error updating citation"

        except Exception as e:
            print(f'Error_Citations.updateCitation() ::: {e}')

    @staticmethod
    def deleteCitation(citationId, token=None):
        try:
            if token == ModelDAO.modeleDAO.token:
                result = CitationDAO(0).deleteById(citationId)

            if result!= 0:
                return "Citation deleted successfully"
            else:
                return "Error deleting citation"

        except Exception as e:
            print(f'Error_Citations.delateCitation() ::: {e}')

    @staticmethod
    def getCitationsNodes(citationId):
        try:
            citation_dao = CitationDAO()
            citations = citation_dao.findCitationsNodes(citationId)
            return citations
        except Exception as e:
            print(f'Error_Citations.getCitationsNodes() ::: {e}')

    @staticmethod
    def getCompareCitation(citationId,compareCitationId):
        try:
            citation_dao = CitationDAO()
            citation = citation_dao.findCompareCitations(citationId,compareCitationId)
            return citation
        except Exception as e:
            print(f'Error_Citations.getCompareCitations() ::: {e}')