from dao import ModelDAO
from model.CategoryM import Category

class CategoryDAO(ModelDAO.modeleDAO):

    def __init__(self):
        '''
        Initialize the CategoryDAO object by establishing a database connection.
        -----------------------------------------------------------------------
        '''
        params = ModelDAO.modeleDAO.connect_object
        self.cur = params.cursor()

    def create(self, category: Category) -> int:
        '''
        Create a new category in the database.
        ---------------------------------------------------------------------

        parameters :
            category: Category object containing category_id and category_name.
        ----------------------------------------------------------------------
        return: The number of affected rows (1 if successful, 0 otherwise).
        ----------------------------------------------------------------------
        '''
        try:
            query = '''INSERT INTO categories (category_id, category_name) VALUES (%s, %s);'''
            self.cur.execute(query, (category.getCategoryId(), category.getCategoryName()))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount != 0 else 0
        except Exception as e:
            print(f"Error_CategoryDAO.create() ::: {e}")
            self.cur.connection.rollback()
        finally:
            self.cur.close()

    def findById(self, category_id: int) -> Category:
        '''
        Retrieve a category by its ID from the database.
        --------------------------------------------------------------------

        parameters :
            category_id: ID of the category to retrieve.
        --------------------------------------------------------------------
        return: Category object if found, None otherwise.
        --------------------------------------------------------------------
        '''
        try:
            query = '''SELECT * FROM categories WHERE category_id = %s;'''
            self.cur.execute(query, (category_id,))
            res = self.cur.fetchone() #take the first line from the request

            if res: #if the request return one line , then a new oject of category is created
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
        '''
        Retrieve categories by name from the database.
        ---------------------------------------------------------------------

        parameters :
            category_name: Name of the categories to retrieve.
        ---------------------------------------------------------------------
        return: List of Category objects if found, None otherwise.
        ---------------------------------------------------------------------
        '''
        try:
            query = '''SELECT * FROM categories WHERE category_name = %s;'''
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

    def update(self, category: Category) -> int:
        '''
        Update a category's name in the database.
        -------------------------------------------------------------------

        parameters :
            category: Category object with updated category_name.
        -------------------------------------------------------------------
        return: The number of affected rows (1 if successful, 0 otherwise).
        -------------------------------------------------------------------
        '''
        try:
            query = '''UPDATE categories SET category_name = %s WHERE category_id = %s;'''
            self.cur.execute(query, (category.getCategoryName(), category.getCategoryId()))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount != 0 else 0
        except Exception as e:
            print(f"Error_CategoryDAO.update() ::: {e}")
            self.cur.connection.rollback()
        finally:
            self.cur.close()

    def deleteById(self, category_id: int) -> int:
        '''
        Delete a category by its ID from the database.
        --------------------------------------------------------------------

        parameters :
            category_id: ID of the category to delete.
        --------------------------------------------------------------------
        return: The number of affected rows (1 if successful, 0 otherwise).
        --------------------------------------------------------------------
        '''
        try:
            query = '''DELETE FROM categories WHERE category_id = %s;'''
            self.cur.execute(query, (category_id,))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount != 0 else 0
        except Exception as e:
            print(f"Error_CategoryDAO.deleteById() ::: {e}")
            self.cur.connection.rollback()
        finally:
            self.cur.close()

    def deleteAll(self) -> int:
        '''
        Delete all categories from the database.
        --------------------------------------------------------------------

        return: The number of affected rows.
        --------------------------------------------------------------------
        '''
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
