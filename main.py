import os
from flask import Flask, render_template, request
from flask_cors import CORS #gestion des accès au w.s.
from datetime import datetime
from functools import wraps
from controller import CategoryC, CitationC, PublicationC, ReferenceC

from model import CategoryM, CitationsM, PublicationM, ReferenceM

app = Flask(__name__)


CORS(app, resources={fr"api/paperWithCode/*": {"origins": "*"}})

# Category Routes
@app.route('/api/paperWithCode/categories', methods=['GET'])
def getCategories():
    categoryC = CategoryC.Category.getCategories()
    print(list)
    
    liste_category = []

    if type(categoryC)==list:
        for c in categoryC:

            category = {
                "category_id" : c.getCategoryId(),
                "category_name" : c.getCategoryName()
            }

            liste_category.append(category)

        return {'response':liste_category}

    return {'response':"Aucune catégorie trouvée"}

@app.route('/api/paperWithCode/category/<int:id>', methods=['GET'])
def getCategory(id):
    print(id)
    category = CategoryC.Category.getCategory(categoryId=id)
    if isinstance(category, CategoryM.Category):
        return {'response': category.getCategoryName()}
    
    return {'response': "La catégorie n'existe pas"}

@app.route('/api/paperWithCode/category/add', methods=['Post'])
def addCategory():
    name = request.json.get('name')
    if  name is not None:
        response = CategoryC.Category.addCategory(name)
        return  {'response': response}
    else:
        return {'response': "Veuillez renseigner le nom de la catégorie"}
  

@app.route('/api/paperWithCode/category/update/<int:id>', methods=['POST'])
def updateCategory(id):
    name = request.json.get('name')
    if  name is not None:
        response = CategoryC.Category.updateCategory(id, name)
        return  {'response': response}
    else:
        return {'response': "Veuillez renseigner le nom de la catégorie"}
    
@app.route('/api/paperWithCode/category/delete/<int:id>', methods=['POST'])
def deleteCategory(id):
    response = CategoryC.Category.deleteCategory(id)
    return  {'response': response}

if __name__=='__main__':

    # Run flask with the following defaults
    app.run(debug=True, port=5000, host='0.0.0.0', )