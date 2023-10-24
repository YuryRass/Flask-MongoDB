from pymongo import MongoClient, errors
from pymongo.results import UpdateResult
from pymongo.collection import Collection

from config import settings


class DataBase:
    def __init__(
        self, database_name: str, collection_name: str
    ) -> None:
        self.db_name: str = database_name
        self.coll_name: str = collection_name
        self.coll: Collection | None = None

    def connect(self):
        try:
            mongo_client: MongoClient = MongoClient(
                host=settings.MONGO_HOST,
                port=settings.MONGO_PORT,
                username=settings.MONGO_USER,
                password=settings.MONGO_PASS,
            )
            if mongo_client.list_databases():
                mongo_client = mongo_client[self.db_name]
                self.coll = mongo_client[self.coll_name]
                return [True, 'Success']
        except errors.ServerSelectionTimeoutError:
            return [False, 'Failed to Connect DB']
        except errors.ConnectionFailure:
            return [False, 'Connection Failure']
        except errors.ConfigurationError:
            return [False, 'Configurarion Error']

    def _create_document(self, document: dict):
        try:
            self.coll.insert_one(document)
            return [True, "Success"]
        except errors.DuplicateKeyError:
            return [False, 'The config name is already exist']

    def _find_document(self, doc: str):
        try:
            cursor = self.coll.find_one({"user": doc}, {'_id': False})
            if cursor is not None:
                return [True, "Success", cursor]
            else:
                return [False, "No document found"]
        except Exception:
            return [False, "Internal Error"]

    def _update_document(self, key: str, new_val: str):
        try:
            result: UpdateResult = self.coll.replace_one(
                {"user": key}, {"user": key, "password": new_val}
            )
            if result.acknowledged:
                return [True, "Success", result]
            else:
                raise Exception
        except Exception:
            return [False, "Internal Error"]
