from dao import ModelDAO
from model.CityM import City

class CityDAO(ModelDAO.modeleDAO):
    def __init__(self,sercurity=1):
        if sercurity == 0:
            params = ModelDAO.modeleDAO.connect_object
        if sercurity == 1:
            params = ModelDAO.modeleDAO.user_connect
        self.cur=params.cursor()

    def create(self, city)->int:
        try:
            query = '''INSERT INTO city (name) 
                       VALUES (%s);'''
            self.cur.execute(query, ( city.getCityName(),))
            self.cur.connection.commit() 
            return self.cur.rowcount if self.cur.rowcount!=0 else 0
        except Exception as e:
            print(f"Erreur_CityDAO.create() ::: {e}")

    def findById(self, cityId)->object:
        try:
            query = '''SELECT id,name FROM city WHERE id = %s;'''
            self.cur.execute(query, (cityId,))
            res = self.cur.fetchone()

            if res:

                c = City()

                c.setCityId(res[0])
                c.setCityName(res[1])

                return c
            else:
                return None
        except Exception as e:
            print(f"Erreur_CityDAO.FindById() ::: {e}")
        finally:
            self.cur.close()
        
    def findAll(self)->list:
        try:
            query = '''SELECT * FROM city;'''
            self.cur.execute(query)
            res = self.cur.fetchall()

            liste_c = [] # [Brands(brand_id=row[0], brand_name=row[1]) for row in res] if res else None

            if len(res)>0:

                for r in res:
                    c = City()

                    c.setCityId(r[0])
                    c.setCityName(r[1])


                    liste_c.append(c)

                return liste_c

            else:

                return None

        except Exception as e:
            print(f"Erreur_CityDAO.findAll() ::: {e}")
        finally:
            self.cur.close()

    def update(self, city)->int:
        try:
            query = '''UPDATE city SET name = %s WHERE id = %s;'''
            self.cur.execute(query, (city.getCityName(), city.getCityId()))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount!=0 else 0
        except Exception as e:
            print(f"Erreur_CityDAO.update() ::: {e}")
            self.cur.connection.rollback()
        finally:
            self.cur.close()
    
    def deleteById(self, cityId)->int:
        try:
            query = f'''DELETE FROM city WHERE id = %s;'''
            self.cur.execute(query, (cityId,))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount!=0 else 0
        except Exception as e:
            print(f"Erreur_CityDAO.deleteById() ::: {e}")
            self.cur.connection.rollback()
        finally:
            self.cur.close()

    def findByName(self, cityName)->object:
        try:
            query = '''SELECT id,name FROM city WHERE name = %s;'''
            self.cur.execute(query, (cityName,))
            res = self.cur.fetchone()

            if res:

                c = City()

                c.setCityId(res[0])
                c.setCityName(res[1])

                return c
            else:
                return None
        except Exception as e:
            print(f"Erreur_CityDAO.FindById() ::: {e}")
        finally:
            self.cur.close()
        