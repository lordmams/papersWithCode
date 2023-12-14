from dao.CategoryDAO import *
from model import *

class Category:

    @staticmethod
    def getCategories():
        """
        Retrieve all categories.
        ----------------------------------------------------------
        return: List of Category objects if found, None otherwise.
        ----------------------------------------------------------
        """
        try:
            category_dao = CategoryDAO()
            categories = category_dao.findAll()
            return categories
        except Exception as e:
            print(f'Error_Publications.getCategories() ::: {e}')


    @staticmethod
    def getCategory(self,categoryId):
        """
        Retrieve a category by its ID.
        -----------------------------------------------------

        parameters
            categoryId: ID of the category to retrieve.
        -----------------------------------------------------
        return: Category object if found, None otherwise.
        -----------------------------------------------------
        """
        try:
            category_dao = CategoryDAO()
            category = category_dao.findById(categoryId)
            return category
        except Exception as e:
            print(f'Error_Publications.getCategory() ::: {e}')

    @staticmethod
    def addCategory(self,name):
        """
        Add a new category.
        ----------------------------------------------------------

        parameters
            name: Name of the new category.
        ----------------------------------------------------------
        return: Status of the addition (success message or error).
        ----------------------------------------------------------
        """
        try:
            category_dao = CategoryDAO()
            new_category = Category()
            new_category.setCategorytName(name)
            result = category_dao.create(new_category)

            if result != 0:
                return "Category added successfully"
            else:
                return "Error adding category"

        except Exception as e:
            print(f'Error_Publications.addCategory() ::: {e}')


    @staticmethod
    def addCategories(self,categoriesList):
        """
        Add multiple categories
        -----------------------------------------------------

        parameters
            categoriesList: List of category names to add
        -----------------------------------------------------
        """
        try:
            category_dao = CategoryDAO()

            for category_name in categoriesList:
                new_category = Category()
                new_category.setCategorytName(category_name)
                category_dao.create(new_category)

        except Exception as e:
            print(f'Error_Publications.addCategories() ::: {e}')

    @staticmethod
    def updateCategory(self,categoryId, nameCategory):
        """
        Update the name of a category
        ------------------------------------------------------

        parameters
            categoryId: ID of the category to update.
            nameCategory: New name for the category
        -------------------------------------------------------
        return: Status of the update (success message or error)
        --------------------------------------------------------
        """
        try:
            category_dao = CategoryDAO()
            existing_category = category_dao.findById(categoryId)

            if existing_category:
                existing_category.setCategorytName(nameCategory)
                result = category_dao.update(existing_category)

                if result != 0:
                    return "category updated successfully"
                else:
                    return "error updating category"
            else:
                return "category not found"

        except Exception as e:
            print(f'Error_Publications.updateCategory() ::: {e}')

    @staticmethod
    def deleteCategory(self,categoryId):
        """
        Delete a category by its ID
        -----------------------------------------------------------

        parameters :
            categoryId: ID of the category to delete
        -----------------------------------------------------------
        return: Status of the deletion (success message or error)
        -----------------------------------------------------------
        """
        try:
            category_dao = CategoryDAO()
            result = category_dao.deleteById(categoryId)

            if result != 0:
                return "category deleted successfully"
            else:
                return "error deleting category"

        except Exception as e:
            print(f'Error_Publications.deleteCategory() ::: {e}')

    """
def addCategories(self,categoriesList):
        for publication in categoriesList :
            self.addPublication(publication.link , publication.city)
    """

