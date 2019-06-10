
import sys
from flask import Flask, request
from flask_restplus import Api, Resource, fields
import logging
import os

# Set the root to current working directory
os.chdir(os.path.dirname(os.path.realpath(__file__)))

app = Flask(__name__)

UPLOAD_FOLDER = '/tmp/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


api = Api(app, version='1.0', title='Supply chain app',
    description='visualize stock',
)

@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

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
