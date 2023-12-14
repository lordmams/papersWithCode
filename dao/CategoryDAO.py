from dao import ModelDAO
from model.CategoryM import Category

class CategoryDAO(ModelDAO.modeleDAO):

    def __init__(self):

        params=ModelDAO.modeleDAO.connect_object
        self.cur=params.cursor()

      # INSERT

    def create(self, category)->int:
        pass


    # SELECT
    def findById(self, category)->object:
        try:
            query = '''SELECT * FROM category where category_id=%s;'''
            self.cur.execute(query, (category,))
            res = self.cur.fetchone()

            if res:

                r = Category()

                b.setCategoryId(res[0])


                return b
            else:
                return None
    except Exception as e:
        print(f"Erreur_CategoryDAO.findById() ::: {e}")
    finally:
        self.cur.close()

        pass


    def findByName(self)->list[Category]:

            try:
                query = '''SELECT * FROM category where category_name=%s;'''
                self.cur.execute(query)
                res = self.cur.fetchall()
                liste_c=[]

                if len(res)>0:
                    for r in res:
                        c = Category()

                        b.setCategoryIdId(r[0])
                        b.setCategoryName(r[1])

                        liste_c.append(c)

                    return liste_c
                else:
                    return None
            except Exception as e:
                print(f"Erreur_CustomersDAO.FindByName() ::: {e}")
            finally:
                self.cur.close()


    # UPDATE


    def update(self, category)->int:
        try:
            query = '''UPDATE Category SET Category_name = %s, WHERE category_id = %s;'''
            self.cur.execute(query, (objModif.getCategoryName(), cleAnc))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount!=0 else 0
        except Exception as e:
            print(f"Erreur_CategoryDAO.update() ::: {e}")
            self.cur.connection.rollback()
        finally:
            self.cur.close()
        pass

    # DELETE


    def deleteById(self, category)->int:
        try:
            query = f'''DELETE FROM category WHERE category_id = %s;'''
            self.cur.execute(query, (cleSup,))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount!=0 else 0
        except Exception as e:
            print(f"Erreur_CategoryDAO.deleteById() ::: {e}")
            self.cur.connection.rollback()
        finally:
            self.cur.close()
        pass


    def deleteAll(self)->int:
        try:
            query = f'''DELETE FROM category WHERE category_id = %s;'''
            self.cur.execute(query, (cleSup,))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount!=0 else 0
        except Exception as e:
            print(f"Erreur_CategoryDAO.deleteById() ::: {e}")
            self.cur.connection.rollback()
        finally:
            self.cur.close()
