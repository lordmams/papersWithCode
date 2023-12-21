from dao.CategoryDAO import *
from model import CategoryM

class Category:

    @staticmethod
    def getCategories():

        try:
            category_dao = CategoryDAO()
            categories = category_dao.findAll()
            return categories
        except Exception as e:
            print(f'Error_Category.getCategories() ::: {e}')


    @staticmethod
    def getCategory(categoryId):

        try:
            category_dao = CategoryDAO()
            category = category_dao.findById(categoryId)
            return category
        except Exception as e:
            print(f'Error_Publications.getCategory() ::: {e}')

    @staticmethod
    def addCategory(name):
        try:
            category_dao = CategoryDAO()
            new_category = CategoryM.Category()
            new_category.setCategoryName(name)
            result = category_dao.create(new_category)

            if result != 0:
                return "Category added successfully"
            else:
                return "Error adding category"

        except Exception as e:
            print(f'Error_Publications.addCategory() ::: {e}')


    @staticmethod
    def addCategories(categoriesList):

        try:
            category_dao = CategoryDAO()

            for category_name in categoriesList:
                new_category = CategoryM.Category()
                new_category.setCategorytName(category_name)
                category_dao.create(new_category)

        except Exception as e:
            print(f'Error_Publications.addCategories() ::: {e}')

    @staticmethod
    def updateCategory(categoryId, nameCategory, token=None):
     
        try:
            category_dao = CategoryDAO()
            existing_category = category_dao.findById(categoryId)

            if existing_category and token == ModelDAO.modeleDAO.token:
                existing_category.setCategoryName(nameCategory)
                result = CategoryDAO(0).update(existing_category)

                if result != 0:
                    return "category updated successfully"
                else:
                    return "error updating category"
            else:
                return "category not found"

        except Exception as e:
            print(f'Error_Publications.updateCategory() ::: {e}')

    @staticmethod
    def deleteCategory(categoryId,token=None):
    
        try:
            if token == ModelDAO.modeleDAO.token: 
                result = CategoryDAO(0).deleteById(categoryId)

            if result != 0:
                return "category deleted successfully"
            else:
                return "error deleting category"

        except Exception as e:
            print(f'Error_Publications.deleteCategory() ::: {e}')

    @staticmethod
    def getCategoryByName(category_name)->object:
        try:
            category_dao = CategoryDAO()
            category = category_dao.findByName(category_name)

            return category
        except Exception as e:
            print(f'Error_Publications.getCategoryByName() ::: {e}')
        finally:
            category_dao.cur.close()
