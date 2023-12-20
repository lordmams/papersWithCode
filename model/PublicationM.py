class Publication:

    def __init__(self):
        self.__publication_id: int = None
        self.__publication_city: str = ""
        self.__publication_link: str = ""
        self.__publication_category: str = ""

    def setPublicationId(self, publicationId: int) -> None:
    
        self.__publication_id = publicationId

    def getPublicationId(self) -> int:
        return self.__publication_id

    def setPublicationCity(self, city: str) -> None:
        self.__publication_city = city

    def getPublicationCity(self) -> str:
        return self.__publication_city
    
    def setPublicationLink(self, link: str) -> None:
        self.__publication_link = link

    def getPublicationLink(self) -> str:
        return self.__publication_link
    
    def getPublicationCategory(self) -> str:
        return self.__publication_category
    
    def setPublicationCategory(self, category: str):
        self.__publication_category = category