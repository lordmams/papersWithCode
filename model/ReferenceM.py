class Reference:

    def __init__(self):
        self.__id: int = None
        self.__publication: str = None
        self.__reference: str = None
 

    def setId(self, id: int) -> None:
        self.__id = id
    
    def getId(self) -> int:
        return self.__id
    def setPublication(self, publication: str) -> None:
        self.__publication = publication

    def getPublication(self) -> str:
        return self.__publication
    
    def setReference(self, reference: str) -> None:

        self.__reference= reference

    def getReference(self) -> str:

        return self.__reference

   