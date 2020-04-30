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
                result = { "users": [user for user in self.database['users'] 
                            if user["name"] in payload["users"]] }
                return json.dumps(result)

    def post(self, url, payload=None):
        payload = json.loads(payload)

        if url == '/add':
            return RestAPI.user_parser(payload)
        if url == '/iou':
            lender = list(filter(lambda x: x['name'] == payload['lender'], self.database['users']))[0]
            borrower = list(filter(lambda x: x['name'] == payload['borrower'], self.database['users']))[0]

            lender['balance'] += payload['amount']
            lender['owed_by'][borrower['name']] = payload['amount']
            lender['owes'][borrower['name']] -= payload['amount']

            borrower['balance'] -= payload['amount']
            borrower['owes'][lender['name']] = payload['amount']

            return json.dumps({'users': [lender, borrower]})

    @classmethod
    def user_parser(cls, payload):
        return json.dumps({
            "name": payload["user"], 
            "owes": {}, 
            "owed_by": {}, 
            "balance": 0.0
        })

database = {
            "users": [
                {"name": "Adam", "owes": {}, "owed_by": {}, "balance": 0.0},
                {"name": "Bob", "owes": {"Chuck": 3.0}, "owed_by": {}, "balance": -3.0},
                {"name": "Chuck", "owes": {}, "owed_by": {"Bob": 3.0}, "balance": 3.0},
            ]
        }

api = RestAPI(database)
payload = json.dumps({"lender": "Bob", "borrower": "Adam", "amount": 3.0})

print(api.post("/iou",payload))



