import json

class RestAPI:
    def __init__(self, database=None):
        self.database = database

    def get(self, url, payload=None):
        if url == '/users':
            if payload == None:
                return json.dumps(self.database)
            else:
                payload = json.loads(payload)
                # return [user for user in self.database['users']]
                result = { "users": [user for user in self.database['users'] if user["name"] in payload["users"]] }
                return json.dumps(result)

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

database = {
    "users": [
        {"name": "Adam", "owes": {}, "owed_by": {}, "balance": 0.0},
        {"name": "Bob", "owes": {}, "owed_by": {}, "balance": 0.0},
    ]
}
api = RestAPI(database)
payload = json.dumps({"users": ["Bob"]})

print(api.get("/users",payload))



