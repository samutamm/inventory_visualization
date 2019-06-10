
import sys
from flask import Flask, request
from flask_restplus import Api, Resource, fields
from flask_restplus.reqparse import RequestParser
import logging
import os
import os.path
from generate_sample_data import generate_csv

import pandas as pd

# Set the root to current working directory
os.chdir(os.path.dirname(os.path.realpath(__file__)))

app = Flask(__name__)

UPLOAD_FOLDER = '/tmp/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

product_data_source = "products.csv"
if not os.path.exists(product_data_source):
    generate_csv()

api = Api(app, version='1.0', title='Supply chain app',
    description='visualize stock',
)

@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class ProductsDao:

    def __init__(self, resource_path):
        self.products = pd.read_csv(resource_path)
        self.columns =  ["product_id","product_name","dates","inventory_level"]

    def search(self, by=-1):
        return self.products[self.columns][self.products["product_id"] == by]

    def get_all(self):
        return self.products["product_id"].unique().tolist(), \
               self.products["product_name"].unique().tolist()

products_dao = ProductsDao(product_data_source)

@api.route('/api/products')
class ProductsListResource(Resource):

    def get(self):
        ids, names = products_dao.get_all()
        return {"ids":ids, "names":names}

@api.route('/api/products/<int:product_id>')
class ProductResource(Resource):

    def get(self, product_id):
        rows = products_dao.search(by=product_id)
        return {"rows":rows.values.tolist()}


@app.before_first_request
def setup_logging():
    if not app.debug:
        # In production mode, add log handler to sys.stderr.
        app.logger.addHandler(logging.StreamHandler())
        app.logger.setLevel(logging.INFO)

@app.before_request
def log_request_info():
    app.logger.debug('Headers: %s', request.headers)
    app.logger.debug('Body: %s', request.get_data())

@app.after_request
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
#    header['Access-Control-Allow-Methods'] = 'POST, GET'
    header['Access-Control-Allow-Headers'] = 'Content-Type'
    return response

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0', port=5000)

def get_app():
    return app
