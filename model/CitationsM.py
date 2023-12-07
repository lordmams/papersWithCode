class Citation:

    def __init__(self):
        self.__citation_id: int = None
        self.__citation_value: str = ""


    def setcitationId(self, citationId: int) -> None:
    
        self.__citation_id = citationId

    def getcitationId(self) -> int:
        return self.__citation_id

    def setcitationValue(self, citationvalue: str) -> None:
        self.__citation_value = citationvalue

    def getcitationValue(self) -> str:
        return self.__citation_value

