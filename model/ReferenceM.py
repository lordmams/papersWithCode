class Reference:

    def __init__(self):
        self.__reference_id: int = None
 

    def setReferenceId(self, categoryId: int) -> None:

        self.__reference_id = categoryId

    def getReferenceId(self) -> int:

        return self.__reference_id

   