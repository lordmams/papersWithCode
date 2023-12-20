class City:
    def __init__(self):
        self.__city_id: int = None
        self.__city_name: str = ""

    def setCityId(self, cityId: int) -> None:
        self.__city_id = cityId

    def getCityId(self) -> int:
        return self.__city_id
    
    def setCityName(self, cityName: str) -> None:
        self.__city_name = cityName

    def getCityName(self) -> str:
        return self.__city_name