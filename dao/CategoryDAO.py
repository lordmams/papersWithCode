from dao import ModelDAO
from model.CategoryM import Category

class CategoryDAO(ModelDAO.modeleDAO):

    def __init__(self):

        params = ModelDAO.modeleDAO.connect_object
        self.cur = params.cursor()

    def create(self, category: Category) -> int:
       
        try:
            query = '''INSERT INTO categorie (name) VALUES (%s);'''
            self.cur.execute(query, ( category.getCategoryName(),))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount != 0 else 0
        except Exception as e:
            print(f"Error_CategoryDAO.create() ::: {e}")
            self.cur.connection.rollback()
        finally:
            self.cur.close()

    def findById(self, category_id: int) -> Category:
        try:
            query = '''SELECT * FROM categorie WHERE id = %s;'''
            self.cur.execute(query, (category_id,))
            res = self.cur.fetchone() 
            if res: 
                category = Category()
                category.setCategoryId(res[0])
                category.setCategoryName(res[1])
                return category
            else:
                return None
        except Exception as e:
            print(f"Error_CategoryDAO.findById() ::: {e}")
        finally:
            self.cur.close()

    def findByName(self, category_name: str) -> list:
        try:
            query = '''SELECT * FROM categorie WHERE name = %s;'''
            self.cur.execute(query, (category_name,))
            res = self.cur.fetchall()

            category_list = []

            if len(res) > 0:
                for r in res:
                    category = Category()
                    category.setCategoryId(r[0])
                    category.setCategoryName(r[1])
                    category_list.append(category)

                return category_list
            else:
                return None
        except Exception as e:
            print(f"Error_CategoryDAO.findByName() ::: {e}")
        finally:
            self.cur.close()

    def findAll(self)->list:
        try:
            query = '''SELECT * FROM categorie;'''
            self.cur.execute(query)
            res = self.cur.fetchall()

            liste_c = [] 

            if len(res)>0:

                for r in res:
                    c = Category()

                    c.setCategoryId(r[0])
                    c.setCategoryName(r[1])
                    liste_c.append(c)

                return liste_c

            else:

                return None

        except Exception as e:
            print(f"Erreur_CategorieDAO.findAll() ::: {e}")
        finally:
            self.cur.close()
    def update(self, category: Category) -> int:

        try:
            query = '''UPDATE categorie SET name = %s WHERE id = %s;'''
            self.cur.execute(query, (category.getCategoryName(), category.getCategoryId()))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount != 0 else 0
        except Exception as e:
            print(f"Error_CategoryDAO.update() ::: {e}")
            self.cur.connection.rollback()
        finally:
            self.cur.close()

    def deleteById(self, category_id: int) -> int:
      
        try:
            query = '''DELETE FROM categorie WHERE id = %s;'''
            self.cur.execute(query, (category_id,))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount != 0 else 0
        except Exception as e:
            print(f"Error_CategoryDAO.deleteById() ::: {e}")
            self.cur.connection.rollback()
        finally:
            self.cur.close()

    def deleteAll(self) -> int:
     
        try:
            query = '''DELETE FROM categories;'''
            self.cur.execute(query)
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount != 0 else 0
        except Exception as e:
            print(f"Error_CategoryDAO.deleteAll() ::: {e}")
            self.cur.connection.rollback()
        finally:
            self.cur.close()
