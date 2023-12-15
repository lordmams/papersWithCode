from dao import ModelDAO
from model.CitationsM import Citation

class CitationDAO(ModelDAO.modeleDAO):
    def __init__(self):
        params=ModelDAO.modeleDAO.connect_object
        self.cur=params.cursor()

    # INSERT

    def create(self, citation)->int:
        try:
            query = '''INSERT INTO citation (citation_id, citation_value) 
                       VALUES (%s, %s);'''
            self.cur.execute(query, (citation.geCitationId(), citation.getCitationValue()))
            self.cur.connection.commit() #fin de la transaction
            #le nombre de lignes validé par la dernière opération SQL exécutée.
            return self.cur.rowcount if self.cur.rowcount!=0 else 0
        except Exception as e:
            print(f"Erreur_CitationDAO.create() ::: {e}")
            #annuler toutes les modifications non validées depuis le dernier appel à commit()
            self.cur.connection.rollback()
        finally:
            self.cur.close()
# return 0



    # SELECT
    def findById(self, citationId)->object:
        try:
            query = '''SELECT * FROM citation WHERE citation_id = %s;'''
            self.cur.execute(query, (citationId,))
            res = self.cur.fetchone()

            if res:

                b = Citation()

                b.setCitationId(res[0])


                return b
            else:
                return None
        except Exception as e:
            print(f"Erreur_CitationDAO.FindById() ::: {e}")
        finally:
            self.cur.close()


    def findAll(self)->list:
        try:
            query = '''SELECT * FROM citation;'''
            self.cur.execute(query)
            res = self.cur.fetchall()

            liste_b = [] # [Brands(brand_id=row[0], brand_name=row[1]) for row in res] if res else None

            if len(res)>0:

                for r in res:
                    b = Citation()

                    b.setCitationId(r[0])
                    b.setCitationCity(r[1])
                    b.setCitationLink(r[2])


                    liste_b.append(b)

                return liste_b

            else:

                return None

        except Exception as e:
            print(f"Erreur_CitationDAO.findAll() ::: {e}")
        finally:
            self.cur.close()

    # UPDATE


    def update(self, citModif, citation_id)->int:
        try:
            query = '''UPDATE publication SET citation_value = %s WHERE citation_id = %s;'''
            self.cur.execute(query, (citModif.getCitationValue(), citation_id))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount!=0 else 0
        except Exception as e:
            print(f"Erreur_CitationDAO.update() ::: {e}")
            self.cur.connection.rollback()
        finally:
            self.cur.close()

    # DELETE


    def deleteById(self, citationId)->int:
        try:
            query = f'''DELETE FROM citation WHERE citation_id = %s;'''
            self.cur.execute(query, (citationId,))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount!=0 else 0
        except Exception as e:
            print(f"Erreur_PublicationDAO.deleteById() ::: {e}")
            self.cur.connection.rollback()
        finally:
            self.cur.close()


    def deleteAll(self)->int:
        try:
            query = f'''DELETE FROM citation;'''
            self.cur.execute(query,)
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount!=0 else 0
        except Exception as e:
            print(f"Erreur_CitationDAO.deleteAll() ::: {e}")
            self.cur.connection.rollback()
        finally:
            self.cur.close()