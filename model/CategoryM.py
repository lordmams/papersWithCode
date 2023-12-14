class Category:



    def __init__(self):


        self.__category_id: int = None
        self.__category_name: str = ""

    def setCategoryId(self, categoryId: int) -> None:

        self.__category_id = categoryId

    def getCategoryId(self) -> int:

        return self.__category_id

    def setCategoryName(self, categoryName: str) -> None:

        self.__category_name = categoryName

    def getCategoryName(self) -> str:

        return self.__category_name