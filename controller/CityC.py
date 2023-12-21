from dao.CityDAO import *
from model import CityM

class Cities:

    @staticmethod
    def getCities():
        try:
            city_dao = CityDAO()
            cities = city_dao.findAll()
            return cities
        except Exception as e:
            print(f'Error_Cities.getCities() ::: {e}')

    @staticmethod
    def getCity(cityId):
        try:
            city_dao = CityDAO()
            city = city_dao.findById(cityId)
            return city
        except Exception as e:
            print(f'Error_Cities.getCity() ::: {e}')

    @staticmethod
    def addCity(name):
        try:
            city_dao = CityDAO()
            new_city = CityM.City()
       
            new_city.setCityName(name)
            result = city_dao.create(new_city)

            if result!= 0:
                return "City added successfully"
            else:
                return "Error adding city"

        except Exception as e:
            print(f'Error_Cities.addCity() ::: {e}')

    @staticmethod
    def deleteCity(city_id,token=None):
        try:
            if token == ModelDAO.modeleDAO.token:
                result = CityDAO(0).deleteById(city_id)

            if result!= 0:
                return "city deleted successfully"
            else:
                return "error deleting city"

        except Exception as e:
            print(f'Error_Cities.delete_city() ::: {e}')

    @staticmethod
    def updateCity(city_id, name,token=None):
        try:
            city_dao = CityDAO()
            existing_city = city_dao.findById(city_id)

            if existing_city:
                existing_city.setCityName(name)
                if token == ModelDAO.modeleDAO.token:
                    result = CityDAO(0).update(existing_city)

                if result!= 0 :
                    return "city updated successfully"
                else:
                    return "error updating city"
            else:
                return "city not found"

        except Exception as e:
            print(f'Error_Cities.update_city() ::: {e}')
    
    @staticmethod
    def getCityByName(city_name)->object:
        try:
            city_dao = CityDAO()
            city = city_dao.findByName(city_name)

            return city
        except Exception as e:
            print(f'Error_Cities.getCityByName() ::: {e}')
        finally:
            city_dao.cur.close()