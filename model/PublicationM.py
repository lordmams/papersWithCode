class Publication:

    def __init__(self):
        self.__publication_id: int = None
        self.__publication_city: str = ""
        self.__publication_link: str = ""

    def setPublicationId(self, publicationId: int) -> None:
    
        self.__body_part_id = publicationId

    def getPublicationId(self) -> int:
        return self.__publication_id

    def setPublicationCity(self, city: str) -> None:
        self.__publication_city = city

    def getPublicationCity(self) -> str:
        return self.__publication_city
    
    def setPublicationLink(self, link: str) -> None:
        self.__publication_city = city

    def getPublicationLink(self) -> str:
        return self.__publication_link