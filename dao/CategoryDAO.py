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
    def findById(self, category_id)->Category:
        try:
            query = '''SELECT * FROM category where category_id=%s;'''
            self.cur.execute(query, (category_id,))
            res = self.cur.fetchone()

            if res:

                r = Category()
                print(res)
                r.setCategoryId(res[0].id)
                r.setCategoryName(res[0].name)


                return r
            else:
                return None
        except Exception as e:
            print(f"Erreur_CategoryDAO.findById() ::: {e}")
        finally:
            self.cur.close()

        pass


    def findByName(self)->Category:

            try:
                query = '''SELECT * FROM category where category_name=%s;'''
                self.cur.execute(query)
                res = self.cur.fetchall()
         

                if res:
                    for r in res:
                        c = Category()

                        c.setCategoryId(res[0])
                        c.setCategoryName(res[1])



                    return c
                else:
                    return None
            except Exception as e:
                print(f"Erreur_CustomersDAO.FindByName() ::: {e}")
            finally:
                self.cur.close()


    # UPDATE


    def update(self, catModif,category_id)->int:
        try:
            query = '''UPDATE Category SET Category_name = %s, WHERE id = %s;'''
            self.cur.execute(query, (catModif.getCategoryName(), category_id))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount!=0 else 0
        except Exception as e:
            print(f"Erreur_CategoryDAO.update() ::: {e}")
            self.cur.connection.rollback()
        finally:
            self.cur.close()
        pass

    # DELETE


    def deleteById(self, category_id)->int:
        try:
            query = f'''DELETE FROM category WHERE id = %s;'''
            self.cur.execute(query, (category_id,))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount!=0 else 0
        except Exception as e:
            print(f"Erreur_CategoryDAO.deleteById() ::: {e}")
            self.cur.connection.rollback()
        finally:
            self.cur.close()
        pass


    def deleteAll(self,category_id)->int:
        try:
            query = f'''DELETE FROM category;'''
            self.cur.execute(query, (category_id,))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount!=0 else 0
        except Exception as e:
            print(f"Erreur_CategoryDAO.deleteById() ::: {e}")
            self.cur.connection.rollback()
        finally:
            self.cur.close()
