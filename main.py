import os
from flask import Flask, render_template, request
from flask_cors import CORS #gestion des accès au w.s.
from datetime import datetime
from functools import wraps
from controller import CategoryC, CitationC, PublicationC, ReferenceC, CityC

from model import CategoryM, CitationM, PublicationM, ReferenceM, CityM

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
  

@app.route('/api/paperWithCode/category/<int:id>/update', methods=['POST'])
def updateCategory(id):
    name = request.json.get('name')
    token = request.json.get('token')
    if  name is not None:
        response = CategoryC.Category.updateCategory(id, name,token)
        return  {'response': response}
    else:
        return {'response': "Veuillez renseigner le nom de la catégorie"}
    
@app.route('/api/paperWithCode/category/<int:id>/delete', methods=['POST'])
def deleteCategory(id):
    token = request.json.get('token')
    response = CategoryC.Category.deleteCategory(id,token)
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
    
@app.route('/api/paperWithCode/citation/<int:id>/update', methods=['POST'])
def updateCitation(id):
    publication = request.json.get('publication')
    value = request.json.get('value')
    token = request.json.get('token')
    if  publication is not None and value is not None:
        response = CitationC.Citations.updateCitation(id, publication,token)
        return  {'response': response}
    else:
        return {'response': "Veuillez renseigner la publication de la citation"}

@app.route('/api/paperWithCode/citation/<int:id>/delete', methods=['POST'])
def deleteCitation(id):
    token = request.json.get('token')
    response = CitationC.Citations.deleteCitation(id,token)
    return  {'response': response}

@app.route('/api/paperWithCode/citation/<int:id>/nodes', methods=['GET'])
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

@app.route('/api/paperWithCode/citation/<int:id>compare/<int:oid>', methods=['GET'])
def getCitationsEdges(id,oid):
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

@app.route('/api/paperWithCode/reference/<int:id>/update', methods=['POST'])
def updateReference(id):
    reference = request.json.get('reference')
    token = request.json.get('token')
    if  reference is not None:
        response = ReferenceC.References.update(id,reference,token)
        return  {'response': response}
    else:
        return {'response': "Veuillez renseigner la publication de la reference"}

@app.route('/api/paperWithCode/reference/<int:id>/delete', methods=['POST'])
def deleteReference(id):
    token = request.json.get('token')
    response = ReferenceC.References.deleteReference(id,token)
    return  {'response': response}

# City Routes

@app.route('/api/paperWithCode/cities', methods=['GET'])
def getCities():
    cityC = CityC.Cities.getCities()
    
    liste_city = []

    if type(cityC)==list:
        for c in cityC:

            city = {
                "id": c.getCityId(),
                "city" : c.getCityName()
            }

            liste_city.append(city)

        return {'response':liste_city}

    return {'response':"Aucune ville trouvée"}

@app.route('/api/paperWithCode/city/<int:id>', methods=['GET'])
def getCity(id):
    city = CityC.Cities.getCity(cityId=id)
    if isinstance(city, CityM.City):
        return {'response': {
            "id": city.getCityId(),
            "city" : city.getCityName()
        }}
    
    return {'response': "La ville n'existe pas"}

@app.route('/api/paperWithCode/city/add', methods=['Post'])
def addCity():
    city = request.json.get('city')
    if  city is not None:
        response = CityC.Cities.addCity(city)
        return  {'response': response}
    else:
        return {'response': "Veuillez renseigner le nom de la ville"}
    


@app.route('/api/paperWithCode/city/<int:id>/update', methods=['POST'])
def updateCity(id):
    city = request.json.get('city')
    token = request.json.get('token')
    if  city is not None:
        response = CityC.Cities.updateCity(id,city,token)
        return  {'response': response}
    else:
        return {'response': "Veuillez renseigner le nom de la ville"}
    

@app.route('/api/paperWithCode/city/<int:id>/delete', methods=['POST'])
def deleteCity(id):
    token = request.json.get('token')
    response = CityC.Cities.deleteCity(id, token)
    return  {'response': response}

# Publications Routes

@app.route('/api/paperWithCode/publications', methods=['GET'])
def getPublications():
    publicationC = PublicationC.Publications.getPublications()
    
    liste_publication = []

    if type(publicationC)==list:
        for p in publicationC:

            publication = {
                "id": p.getPublicationId(),
                "link" : p.getPublicationLink(),
                "category" : p.getPublicationCategory(),
                "city" : p.getPublicationCity(),
            }

            liste_publication.append(publication)

        return {'response':liste_publication}

    return {'response':"Aucune publication trouvée"}

@app.route('/api/paperWithCode/publication/<int:id>', methods=['GET'])
def getPublication(id):
    publication = PublicationC.Publications.getPublication(publicationId=id)
    if isinstance(publication, PublicationM.Publication):
        return {'response': {
            "id": publication.getPublicationId(),
            "link" : publication.getPublicationLink(),
            "category" : publication.getPublicationCategory(),
            "city" : publication.getPublicationCity()
        }}
    
    return {'response': "La publication n'existe pas"}

@app.route('/api/paperWithCode/publication/add', methods=['Post'])
def addPublication():
    link = request.json.get('link')
    city = request.json.get('city')
    category = request.json.get('category')

    if  link is not None and city is not None and category is not None:  
        response = PublicationC.Publications.addPublication(link,city,category)
        return  {'response': response}
    else:
        return {'response': "Veuillez renseigner le lien, la ville et la catégorie de la publication"}


@app.route('/api/paperWithCode/publication/<int:id>/update', methods=['POST'])
def updatePublication(id):
    link = request.json.get('link')
    city = request.json.get('city')
    category = request.json.get('category')
    token = request.json.get('token')

    if  link is not None or city is not None or category is not None:  
        publication = {
            "link" : link,
            "city" : city,
            "category" : category
        }
        response = PublicationC.Publications.updatePublication(id,publication,token)
        return  {'response': response}
    else:
        return {'response': "Veuillez au moins modifier l'un des champs le lien, la ville ou la catégorie de la publication"}
    

@app.route('/api/paperWithCode/publication/<int:id>/delete', methods=['POST'])
def deletePublication(id):
    token = request.json.get('token')
    response = PublicationC.Publications.deletePublication(id,token)
    return  {'response': response}

@app.route('/api/paperWithCode/publication/<int:id>/citations', methods=['GET'])
def getPublicationsCitations(id):
    publicationC = PublicationC.Publications.getPublicationCitations(publicationId=id)

    if type(publicationC)==list:   
        return {'response':publicationC}

    return {'response':"Aucune citation trouvée pour la publication"}

@app.route('/api/paperWithCode/publication/<int:id>/reference', methods=['GET'])
def getPublicationReference(id):
    publication = PublicationC.Publications.getPublicationReference(id)
    if isinstance(publication, PublicationM.Publication):
        return {'response': {
            "id": publication.getPublicationId(),
            "link" : publication.getPublicationLink(),
            "category" : publication.getPublicationCategory(),
            "city" : publication.getPublicationCity()
        }}
    
    return {'response': "La publication n'existe pas"}

@app.route('/api/paperWithCode/publication/<int:id>/isRefere', methods=['GET'])
def getPublicationIsReference(id):
    publicationC = PublicationC.Publications.getPublicationIsRefer(id)
    liste_publication = []

    if type(publicationC)==list:
        for p in publicationC:

            publication = {
                "id": p.getPublicationId(),
                "link" : p.getPublicationLink(),
                "category" : p.getPublicationCategory(),
                "city" : p.getPublicationCity(),
            }

            liste_publication.append(publication)

        return {'response':liste_publication}
    
    return {'response': "La publication n'a jamais été référencer"}

@app.route('/api/paperWithCode/publications/<int:id>/city', methods=['GET'])
def getPublicationCity(id):
    publicationC = PublicationC.Publications.getPublicationByCity(id)
    liste_publication = []
    if type(publicationC)==list:
        for p in publicationC:

            publication = {
                "id": p.getPublicationId(),
                "link" : p.getPublicationLink(),
                "category" : p.getPublicationCategory(),
                "city" : p.getPublicationCity(),
            }

            liste_publication.append(publication)

        return {'response':liste_publication}

    return {'response': "La ville ne possède pas de publication"}

@app.route('/api/paperWithCode/publications/<int:id>/category', methods=['GET'])
def getPublicationCategory(id):
    publicationC = PublicationC.Publications.getPublicationByCategory(id)
    liste_publication = []
    if type(publicationC)==list:
        for p in publicationC:

            publication = {
                "id": p.getPublicationId(),
                "link" : p.getPublicationLink(),
                "category" : p.getPublicationCategory(),
                "city" : p.getPublicationCity(),
            }

            liste_publication.append(publication)

        return {'response':liste_publication}
    
    return {'response': "La catégorie ne possède pas de publication"}

@app.route('/api/paperWithCode/publications/links', methods=['POST'])
def getPublicationByLink():
    link = request.json.get('link')
    publicationC = PublicationC.Publications.getPublicationByLink(link)
    liste_publication = []
    if type(publicationC)==list:
        for p in publicationC:

            publication = {
                "id": p.getPublicationId(),
                "link" : p.getPublicationLink(),
                "category" : p.getPublicationCategory(),
                "city" : p.getPublicationCity(),
            }

            liste_publication.append(publication)

        return {'response':liste_publication}
    
    return {'response': "Aucune publication trouvée"}

if __name__=='__main__':

    # Run flask with the following defaults
    app.run(debug=True, port=5000, host='0.0.0.0', )