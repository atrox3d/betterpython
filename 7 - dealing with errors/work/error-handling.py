from flask import Flask, jsonify, abort
from db import fetch_blogs, fetch_blog, NotFoundError, NotAuthorizedError
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

@app.route('/')
def hello_world():
    """
    homepage
    """
    return 'Hello, World!'

@app.route('/blogs')
def all_blogs():
    """
    list of blog entries
    """
    return jsonify(fetch_blogs())

@app.route('/blogs/<id>')
def get_blog(id):
    """
    single blog entry
    """
    try:
        return jsonify(fetch_blog(id))
    except NotFoundError:
        abort(404, description='resource not found')
    except NotAuthorizedError:
        abort(403, description='Access denied')    


app.run(debug=True)
