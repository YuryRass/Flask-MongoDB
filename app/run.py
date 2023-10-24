from flask import Flask
from flask import request
from database.dao import DataBaseDAO


db = DataBaseDAO(
    database_name='mafia',
    collection_name='users'
)


app = Flask(__name__)


@app.route('/documents/<key>', methods=['GET'])
def get_document_info(key):
    return db.find_document(key)


@app.route('/documents/', methods=['POST'])
def insert_document():
    return db.create_document(request.get_json(force=True))


@app.route('/documents/<key>', methods=['PUT'])
def change_value(key):
    return db.update_document(key, request.get_json(force=True))


if __name__ == "__main__":
    app.run(port=8080)
