import os
from flask import Flask, render_template, request
from flask_cors import CORS #gestion des accès au w.s.
from datetime import datetime
from functools import wraps
from controller import CategoryC, CitationC, PublicationC, ReferenceC

from model import CategoryM, CitationM, PublicationM, ReferenceM

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

# Citations Routes
@app.route('/api/paperWithCode/citations', methods=['GET'])
def getCitations():
    citationC = CitationC.Citations.getCitations()
    print(citationC)
    
    liste_citation = []

    if type(citationC)==list:
        for c in citationC:

            citation = {
                "citation_id" : c.getCitationId(),
                "citation_publication" : c.getCitationPublication(),
                "citation_value" : c.getCitationValue()
            }

            liste_citation.append(citation)

        return {'response':liste_citation}

    return {'response':"Aucune citation trouvée"}

@app.route('/api/paperWithCode/citation/<int:id>', methods=['GET'])
def getCitation(id):
    print(id)
    citation = CitationC.Citations.getCitation(citationId=id)
    if isinstance(citation, CitationM.Citation):
        return {'response': {
            "citation_id" : citation.getCitationId(),
            "citation_publication" : citation.getCitationPublication(),
            "citation_value" : citation.getCitationValue()
        }}
    
    return {'response': "La citation n'existe pas"}

@app.route('/api/paperWithCode/citation/add', methods=['Post'])
def addCitation():
    publication = request.json.get('publication')
    value = request.json.get('value')
    if  publication is not None and value is not None:
        response = CitationC.Citations.addCitation(publication)
        return  {'response': response}
    else:
        return {'response': "Veuillez renseigner la publication de la citation"}
    
@app.route('/api/paperWithCode/citation/update/<int:id>', methods=['POST'])
def updateCitation(id):
    publication = request.json.get('publication')
    value = request.json.get('value')
    if  publication is not None and value is not None:
        response = CitationC.Citations.updateCitation(id, publication)
        return  {'response': response}
    else:
        return {'response': "Veuillez renseigner la publication de la citation"}

@app.route('/api/paperWithCode/citation/delete/<int:id>', methods=['POST'])
def deleteCitation(id):
    response = CitationC.Citations.deleteCitation(id)
    return  {'response': response}
@app.route('/api/paperWithCode/citations/nodes/<int:id>', methods=['GET'])
def getCitationsNodes(id):
    print(id)
    citationC = CitationC.Citations.getCitationsNodes(citationId=id)

    if type(citationC)==list:
        liste_citation = []
        for c in citationC:

            citation = {
                "citation_id" : c.getCitationId(),
                "citation_publication" : c.getCitationPublication(),
                "nb_node" : c.getCitationValue()
            }

            liste_citation.append(citation)

        return {'response':liste_citation}

    return {'response':"Aucune citation trouvée"}

@app.route('/api/paperWithCode/citations/compare/<int:id>/<int:oid>', methods=['GET'])
def getCitationsEdges(id,oid):
    print(id,oid)
    citation = CitationC.Citations.getCompareCitation(citationId=id,compareCitationId=oid)

    if isinstance(citation, CitationM.Citation):
        return {'response': {
            "citation_id" : citation.getCitationId(),
            "citation_publication" : citation.getCitationPublication(),
            "nb_node" : citation.getCitationValue()
        }}

    return {'response':"Aucune citation trouvée"}

#References Routes


@app.route('/api/paperWithCode/references', methods=['GET'])
def getReferences():
    referenceC = ReferenceC.References.getReferences()
    
    liste_reference = []

    if type(referenceC)==list:
        for c in referenceC:

            reference = {
                "id": c.getId(),
                "reference" : c.getReference(),
                "publication" : c.getPublication()
            }

            liste_reference.append(reference)

        return {'response':liste_reference}

    return {'response':"Aucune reference trouvée"}


@app.route('/api/paperWithCode/reference/<int:id>', methods=['GET'])
def getReference(id):

    reference = ReferenceC.References.getReference(referenceId=id)
    if isinstance(reference, ReferenceM.Reference):
        return {'response': {
            "id": reference.getId(),
            "reference" : reference.getReference(),
            "publication" : reference.getPublication()
        }}
    
    return {'response': "La reference n'existe pas"}


@app.route('/api/paperWithCode/reference/add', methods=['Post'])
def addReference():
    reference = request.json.get('reference')
    publication = request.json.get('publication')
    if  reference is not None and publication is not None:
        response = ReferenceC.References.addReference(reference,publication)
        return  {'response': response}
    else:
        return {'response': "Veuillez renseigner la publication de la reference"}

@app.route('/api/paperWithCode/reference/update/<int:id>', methods=['POST'])
def updateReference(id):
    reference = request.json.get('reference')
    publication = request.json.get('publication')
    if  reference is not None and publication is not None:
        response = ReferenceC.References.update(id,reference)
        return  {'response': response}
    else:
        return {'response': "Veuillez renseigner la publication de la reference"}

@app.route('/api/paperWithCode/reference/delete/<int:id>', methods=['POST'])
def deleteReference(id):
    response = ReferenceC.References.deleteReference(id)
    return  {'response': response}



if __name__=='__main__':

    # Run flask with the following defaults
    app.run(debug=True, port=5000, host='0.0.0.0', )