from dao import ModelDAO
from model.PublicationM import Publication

class PublicationDAO(ModelDAO.modeleDAO):

    def __init__(self,sercurity=1):
        if sercurity == 0:
            params = ModelDAO.modeleDAO.connect_object
        if sercurity == 1:
            params = ModelDAO.modeleDAO.user_connect
        self.cur=params.cursor()

      # INSERT

    def create(self, publication)->int:
        try:
            query = '''
                INSERT INTO publication  (city, link, category) VALUES (%s, %s, %s)
                       ;'''
            self.cur.execute(query, (
                publication.getPublicationCity(), 
                publication.getPublicationLink(), 
                publication.getPublicationCategory(),))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount!=0 else 0
        except Exception as e:
            print(f"Erreur_PublicationDAO.Create() ::: {e}")
           
            self.cur.connection.rollback()
        finally:
            self.cur.close()


    # SELECT
    def findById(self, publicationId)->Publication:
        try:
            query = '''SELECT
                            p.id,
                            p.link,
                            cat.name as categorie,
                            city.name as city
                        FROM
                            publication p
                            join categorie cat on p.category = cat.id
                            join city on p.city = city.id
                        WHERE
                            p.id = %s;'''
            self.cur.execute(query, (publicationId,))
            res = self.cur.fetchone()

            if res:

                p = Publication()

                p.setPublicationId(res[0])
                p.setPublicationLink(res[1])
                p.setPublicationCategory(res[2])
                p.setPublicationCity(res[3])
             

                return p
            else:
                return None
        except Exception as e:
            print(f"Erreur_PublicationDAO.FindById() ::: {e}")
        finally:
            self.cur.close()


    def findIds(self, publicationId)->Publication:
        try:
            query = '''SELECT
                            p.id,
                            p.link,
                            cat.id as categorie,
                            city.id as city
                        FROM
                            publication p
                            join categorie cat on p.category = cat.id
                            join city on p.city = city.id
                        WHERE
                            p.id = %s;'''
            self.cur.execute(query, (publicationId,))
            res = self.cur.fetchone()

            if res:

                p = Publication()

                p.setPublicationId(res[0])
                p.setPublicationLink(res[1])
                p.setPublicationCategory(res[2])
                p.setPublicationCity(res[3])
             

                return p
            else:
                return None
        except Exception as e:
            print(f"Erreur_PublicationDAO.FindIds() ::: {e}")

    def findAll(self)->list:
        try:
            query = '''select
                            p.id,
                            p.link,
                            cat.name as categorie,
                            city.name as city
                        From
                            publication p
                        Join 
                            categorie cat on p.category = cat.id
                        Join 
                            city on p.city = city.id
                        Group by
                        p.id,cat.name,city.name;'''
            self.cur.execute(query)
            res = self.cur.fetchall()

            liste_p = [] 
            if len(res)>0:

                for r in res:
            
                    p = Publication()

                    p.setPublicationId(r[0])
                    p.setPublicationLink(r[1])
                    p.setPublicationCategory(r[2])
                    p.setPublicationCity(r[3])
             

                    liste_p.append(p)

                return liste_p

            else:

                return None
        except Exception as e:
            print(f"Erreur_PublicationDAO.findAll() ::: {e}")
        finally:
            self.cur.close()
    
    def findByCity(self, city_id)->list:
        try:
            query = '''select
                            p.id,
                            p.link,
                            cat.name as categorie,
                            city.name as city
                        From
                            publication p
                        Join 
                            categorie cat on p.category = cat.id
                        Join 
                            city on p.city = city.id
                        WHERE p.city = %s
                        Group by
                        p.id,cat.name,city.name;'''
            self.cur.execute(query, (city_id,))
            res = self.cur.fetchall()

            liste_p = [] 

            if len(res)>0:

                for r in res:
                    p = Publication()

                    p.setPublicationId(r[0])
                    p.setPublicationLink(r[1])
                    p.setPublicationCategory(r[2])
                    p.setPublicationCity(r[3])

                    liste_p.append(p)

                return liste_p

            else:

                return None
        except Exception as e:
            print(f"Erreur_PublicationDAO.findByCity() ::: {e}")
        finally:
            self.cur.close()

    def findByCategory(self, category_id)->object:
        try:
            query = '''select
                            p.id,
                            p.link,
                            cat.name as categorie,
                            city.name as city
                        From
                            publication p
                        Join 
                            categorie cat on p.category = cat.id
                        Join 
                            city on p.city = city.id
                        WHERE p.category = %s
                        Group by
                        p.id,cat.name,city.name;'''
            self.cur.execute(query, (category_id,))
            res = self.cur.fetchall()

            liste_p = [] 

            if len(res)>0:

                for r in res:
                    p = Publication()

                    p.setPublicationId(r[0])
                    p.setPublicationLink(r[1])
                    p.setPublicationCategory(r[2])
                    p.setPublicationCity(r[3])

                    liste_p.append(p)
                return liste_p
            else:

                return None
        except Exception as e:
            print(f"Erreur_PublicationDAO.findByCity() ::: {e}")
        finally:
            self.cur.close()

        
    
    def findByLink(self, link)->object:
        try:
            query = '''SELECT
                            p.id,
                            p.link,
                            cat.name as categorie,
                            city.name as city
                        FROM
                            publication p
                            join categorie cat on p.category = cat.id
                            join city on p.city = city.id
                        WHERE
                            p.link ~ %s
                            group by
                            p.id,
                            cat.name,
                            city.name;'''
            self.cur.execute(query, (link,))
            res = self.cur.fetchall()
            
            liste_p = []
            if len(res)>0:

                for r in res:
                    p = Publication()

                    p.setPublicationId(r[0])
                    p.setPublicationLink(r[1])
                    p.setPublicationCategory(r[2])
                    p.setPublicationCity(r[3])

                    liste_p.append(p)
                return liste_p
            else:
                return None
        except Exception as e:
            print(f"Erreur_PublicationDAO.findByLink() ::: {e}")
        finally:
            self.cur.close()


    def update(self, publication)->int:
        try:
         
            query = '''UPDATE publication SET city = %s, link=%s, category = %s WHERE id = %s;'''
            self.cur.execute(query, (
                publication.getPublicationCity(), 
                publication.getPublicationLink(), 
                publication.getPublicationCategory(),
                publication.getPublicationId(),))
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
            query = f'''DELETE FROM publication WHERE id = %s;'''
            self.cur.execute(query, (publicationId,))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount!=0 else 0
        except Exception as e:
            print(f"Erreur_PublicationDAO.deleteById() ::: {e}")
            self.cur.connection.rollback()
        finally:
            self.cur.close()


    def findPublicationReference(self, publicationId):
        try:
            query = '''SELECT
                            p.id,
                            r.ref_publication as reference,
                            cat.name as categorie,
                            city.name as city
                        FROM
                            publication p
                            join reference r on r.publication = p.link
                            join publication p2 on r.publication = p2.link
                            join categorie cat on cat.id = p2.category
                            join city on city.id = p2.city
                        WHERE
                            p.id = %s;'''
                        
            self.cur.execute(query, (publicationId,))
            res = self.cur.fetchone()
            
            if res:
                p = Publication()

                p.setPublicationId(res[0])
                p.setPublicationLink(res[1])
                p.setPublicationCategory(res[2])
                p.setPublicationCity(res[3])
             

                return p
            else:
                return None
         
        except Exception as e:
            print(f"Erreur_PublicationDAO.findPublicationReference() ::: {e}")
        finally:
            self.cur.close()

    def findPublicationIsRefer(self,publicationId):
        try:
            query = '''SELECT
                            p.id,
                            r.publication as reference,
                            cat.name as categorie,
                            city.name as city
                        FROM
                            publication p 
                            join reference r on r.ref_publication = p.link
                            join publication p2 on r.publication = p2.link
                            join categorie cat on cat.id = p2.category
                            join city on city.id = p2.city
                        WHERE
                            p.id = %s;'''
                        
            self.cur.execute(query, (publicationId,))
            res = self.cur.fetchall()

            liste_p = [] 

            if len(res)>0:

                for r in res:
                    p = Publication()

                    p.setPublicationId(r[0])
                    p.setPublicationLink(r[1])
                    p.setPublicationCategory(r[2])
                    p.setPublicationCity(r[3])

                    liste_p.append(p)
                return liste_p
            else:

                return None
         
        except Exception as e:
            print(f"Erreur_PublicationDAO.findPublicationIsRefer() ::: {e}")
        finally:
            self.cur.close()

    def findPublicationCitations(self, publicationId):
        try:
            query = '''SELECT
                            p.id,
                            c.id as citation_id,
                            p.link as publication,
                            count_ones(c.value) as nodes
            
                        FROM
                            publication p 
                            join citation c on c.publication = p.link
                        WHERE
                            p.id = %s;'''
                        
            self.cur.execute(query, (publicationId,))
            res = self.cur.fetchall()

            liste_p = [] 

            if len(res)>0:

                for r in res:
                    p= { 
                        "id": r[0], 
                        "citation_id": r[1], 
                        "publication": r[2],
                        "nodes": r[3]}

                    liste_p.append(p)
                return liste_p
            else:

                return None
         
        except Exception as e:
            print(f"Erreur_PublicationDAO.findPublicationIsRefer() ::: {e}")
        finally:
            self.cur.close()