import json
from pymongo import errors
from pymongo.results import UpdateResult

from app.database.database import DataBase


class DataBaseDAO(DataBase):
    def create_document(self, document):
        status, msg = super().connect()
        if not status:
            return json.dumps({"Issue": msg}), 500
        try:
            status = super()._create_document(document)
            if status[0]:
                del (document["_id"])
                return json.dumps(document)
            else:
                return json.dumps({"Issue": status[1]}), 500
        except errors.ServerSelectionTimeoutError:
            return json.dumps(dict({"Issue": 'Failed to Connect DB'}))

    def find_document(self, doc: str):
        status, msg = super().connect()
        if not status:
            return json.dumps({"Issue": msg}), 500
        try:
            status = super()._find_document(doc)
            if status[0]:
                return str(status[2])
            else:
                return json.dumps({"Issue": status[1]}), 500
        except errors.ServerSelectionTimeoutError:
            return json.dumps(dict({"Issue": 'Failed to Connect DB'}))

    def update_document(self, key: str, new_val: str):
        status, msg = super().connect()
        if not status:
            return json.dumps({"Issue": msg}), 500
        try:
            status = super()._update_document(key, new_val)
            result: UpdateResult = status[2]
            if status[0]:
                return json.dumps(
                    {
                        "match_count": result.matched_count,
                        "modified_count": result.modified_count
                    }
                )
            else:
                return json.dumps({"Issue": status[1]}), 500
        except errors.ServerSelectionTimeoutError:
            return json.dumps(dict({"Issue": 'Failed to Connect DB'}))
