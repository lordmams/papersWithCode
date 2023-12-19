class Citation:

    def __init__(self):
        self.__citation_id: int = None
        self.__citation_value: str = ""
        self.__citation_publication: str = None


    def setCitationId(self, citationId: int) -> None:
    
        self.__citation_id = citationId

    def getCitationId(self) -> int:
        return self.__citation_id

    def setCitationValue(self, citationvalue: str) -> None:
        self.__citation_value = citationvalue

    def getCitationValue(self) -> str:
        return self.__citation_value

    def setCitationPublication(self, citationpublication: str) -> None:
        self.__citation_publication = citationpublication

    def getCitationPublication(self) -> str:
        return self.__citation_publication
