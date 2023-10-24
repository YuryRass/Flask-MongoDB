"""Flask application"""
from flask import Flask
from flask import request
from app.database.dao import DataBaseDAO
from app.config import settings


db: DataBaseDAO = DataBaseDAO(
    database_name=settings.DB_NAME,
    collection_name=settings.COLLECTION_NAME
)

app: Flask = Flask(__name__)


@app.route('/documents/<key>', methods=['GET'])
def get_document_info(key):
    return db.find_document(key)


@app.route('/documents/', methods=['POST'])
def insert_document():
    return db.create_document(request.get_json(force=True))


@app.route('/documents/<key>', methods=['PUT'])
def change_value(key):
    return db.update_document(key, request.get_json(force=True))
