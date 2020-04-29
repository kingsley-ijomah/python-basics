import json

class RestAPI:
    def __init__(self, database=None):
        self.database = database

    def get(self, url, payload=None):
        if url == '/users' and payload == None:
            return json.dumps(self.database)

    def post(self, url, payload=None):
        if url == '/add' and payload:
            return RestAPI.user_parser(payload)

    @classmethod
    def user_parser(cls, payload):
        payload = json.loads(payload)
        return json.dumps({
            "name": payload["user"], 
            "owes": {}, 
            "owed_by": {}, 
            "balance": 0.0
        })


database = {"users": []}
api = RestAPI(database)
payload = json.dumps({"user": "Adam"})

print(api.get("/users",payload))



