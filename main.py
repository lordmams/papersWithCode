import os
from flask import Flask, render_template, request
from flask_cors import CORS #gestion des accès au w.s.
from datetime import datetime
from functools import wraps
from controller import *

from model import CategoryM, CitationsM, PublicationM, ReferenceM

app = Flask(__name__)


CORS(app, resources={fr"api/paperWithCode/*": {"origins": "*"}})

@app.route('/', methods=['GET'])
def start():
    return {'Notice': "The api is protected, you could not do anything.",
            'A message for you ':"Hello dear dev./user WELCOME TO the Privacy Policy lvmh_sephora",
            'Pay attention':"We collect certain information, including your IP address and MAC address, for troubleshooting purposes. This information is collected automatically and anonymously and is not used to personally identify you unless there is a technical issue.",
            'Privacy Policy':'Hello world'}

if __name__=='__main__':

    # Run flask with the following defaults
    app.run(debug=True, port=5000, host='0.0.0.0', )