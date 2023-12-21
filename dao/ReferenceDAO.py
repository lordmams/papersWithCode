from dao import ModelDAO
from model.ReferenceM import Reference

class ReferencesDAO(ModelDAO.modeleDAO):
    def __init__(self,sercurity=1):
        if sercurity == 0:
            params = ModelDAO.modeleDAO.connect_object
        if sercurity == 1:
            params = ModelDAO.modeleDAO.user_connect
        self.cur = params.cursor()

    def create(self, reference: Reference) -> int:
        try:
            query = '''INSERT INTO reference (ref_publication, publication) VALUES (%s, %s)'''
            self.cur.execute(query, ( reference.getReference(),reference.getPublication(),))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount != 0 else 0
        except Exception as e:
            print(f"Error_ReferenceDAO.create() ::: {e}")
            self.cur.connection.rollback()
        finally:
            self.cur.close()
            


    def update(self, reference: Reference) -> int:
        try:
            query = '''UPDATE reference SET ref_publication = %s, publication = %s WHERE id = %s;'''
            self.cur.execute(query, (reference.getReference(), reference.getPublication(), reference.getId()))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount!= 0 else 0
    
        except Exception as e:
            print(f"Error_ReferenceDAO.update_reference() ::: {e}")
            self.cur.connection.rollback()
        finally:
            self.cur.close()

    def deleteById(self, reference_id: int) -> int:
        try:
            query = '''DELETE FROM reference WHERE id = %s;'''
            self.cur.execute(query, (reference_id,))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount!= 0 else 0
        except Exception as e:
            print(f"Error_ReferenceDAO.deleteReference() ::: {e}")
            self.cur.connection.rollback()
        finally:
            self.cur.close()
      
    def findById(self, reference_id) -> Reference:
        try:
            query = '''SELECT * FROM reference WHERE id = %s;'''
            self.cur.execute(query, (reference_id,))
            res = self.cur.fetchone() 
            if res: 
                reference = Reference()
                reference.setId(res[0])
                reference.setReference(res[2])
                reference.setPublication(res[1])
                return reference
            else:
                return None
        except Exception as e:
            print(f"Error_ReferenceDAO.findById() ::: {e}")
        finally:
            self.cur.close()

    def findAll(self) -> list:
        try:
            query = '''SELECT * FROM reference;'''
            self.cur.execute(query)
            res = self.cur.fetchall()

            reference_list = []

            if len(res) > 0:
                for r in res:
                    reference = Reference()
                    reference.setId(r[0])
                    reference.setReference(r[1])
                    reference.setPublication(r[2])
                    reference_list.append(reference)

                return reference_list
            else:
                return None
        except Exception as e:
            print(f"Error_ReferenceDAO.findAll() ::: {e}")
        finally:
            self.cur.close()

