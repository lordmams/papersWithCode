from dao import ModelDAO
from model.PublicationM import Publication

class PublicationDAO(ModelDAO.modeleDAO):

    def __init__(self):

        params=ModelDAO.modeleDAO.connect_object
        self.cur=params.cursor()

      # INSERT

    def create(self, publication)->int:
        try:
            query = '''INSERT INTO  (publication_id, publication_city, publication_link) 
                       VALUES (%s, %s, %s);'''
            self.cur.execute(query, (objIns.getPublicationId(), objIns.getPublicationCity(), objIns.getPublicationLink()))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount!=0 else 0
        except Exception as e:
            print(f"Erreur_PublicationDAO.Create() ::: {e}")
            #annuler toutes les modifications non validées depuis le dernier appel à commit()
            self.cur.connection.rollback()
        finally:
            self.cur.close()


    # SELECT
    def findById(self, publicationId)->object:
        try:
            query = '''SELECT * FROM publication WHERE publication_id = %s;'''
            self.cur.execute(query, (cleTrouv,))
            res = self.cur.fetchone()

            if res:

                b = Publication()

                b.setPublicationId(res[0])


                return b
            else:
                return None
        except Exception as e:
            print(f"Erreur_PublicationDAO.FindById() ::: {e}")
        finally:
            self.cur.close()



    def findAll(self)->list:
        try:
            query = '''SELECT * FROM publication;'''
            self.cur.execute(query)
            res = self.cur.fetchall()

            liste_b = [] # [Brands(brand_id=row[0], brand_name=row[1]) for row in res] if res else None

            if len(res)>0:

                for r in res:
                    b = Publication()

                    b.setPublicationId(r[0])
                    b.setPublicationCity(r[1])
                    b.setPublicationLink(r[2])


                    liste_b.append(b)

                return liste_b

            else:

                return None
        except Exception as e:
            print(f"Erreur_PublicationDAO.findAll() ::: {e}")
        finally:
            self.cur.close()
    
    def findByCity(self, city)->list:
        try:
            query = '''SELECT * FROM publication where publication_city=%s;'''
            self.cur.execute(query)
            res = self.cur.fetchall()

            liste_b = [] # [Brands(brand_id=row[0], brand_name=row[1]) for row in res] if res else None

            if len(res)>0:

                for r in res:
                    b = Publication()


                    b.setPublicationCity(r[1])



                    liste_b.append(b)

                return liste_b

            else:

                return None
        except Exception as e:
            print(f"Erreur_PublicationDAO.findByCity() ::: {e}")
        finally:
            self.cur.close()

    def findByCategory(self, category)->object:
        pass
    
    def findByLink(self, link)->object:
        try:
            query = '''SELECT * FROM publication WHERE publication_link = %s;'''
            self.cur.execute(query, (publication_link,))
            res = self.cur.fetchone()

            if res:

                b = Publication()

                b.setPublicationId(res[0])
                b.setPublicationCity(res[1])
                b.setPublicationLink(res[2])

                return b
            else:
                return None
        except Exception as e:
            print(f"Erreur_PublicationDAO.findByLink() ::: {e}")
        finally:
            self.cur.close()



    # UPDATE


    def update(self, publication)->int:
        try:
            query = '''UPDATE publication SET publication_city = %s, publication_link='%s' WHERE brand_id = %s;'''
            self.cur.execute(query, (objModif.getPublicationCity(), cleAnc))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount!=0 else 0
        except Exception as e:
            print(f"Erreur_PublicationDAO.update() ::: {e}")
            self.cur.connection.rollback()
        finally:
            self.cur.close()

    # DELETE


    def deleteById(self, publicationId)->int:
        try:
            query = f'''DELETE FROM publication WHERE publication_id = %s;'''
            self.cur.execute(query, (cleSup,))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount!=0 else 0
        except Exception as e:
            print(f"Erreur_PublicationDAO.deleteById() ::: {e}")
            self.cur.connection.rollback()
        finally:
            self.cur.close()


    def deleteAll(self)->int:
        try:
            query = f'''DELETE FROM publication;'''
            self.cur.execute(query, (cleSup,))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount!=0 else 0
        except Exception as e:
            print(f"Erreur_PublicationDAO.deleteAll() ::: {e}")
            self.cur.connection.rollback()
        finally:
            self.cur.close()