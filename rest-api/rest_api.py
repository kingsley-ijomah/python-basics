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
                result = [user for user in self.database['users'] if user["name"] in payload["users"]]
                return json.dumps({ "users": result })

    def post(self, url, payload=None):
        payload = json.loads(payload)
        
        if url == '/add':
            return json.dumps({"name": payload["user"], "owes": {}, "owed_by": {}, "balance": 0.0})
        if url == '/iou':
            lender = list(filter(lambda x: x['name'] == payload['lender'], self.database['users']))[0]
            borrower = list(filter(lambda x: x['name'] == payload['borrower'], self.database['users']))[0]

            lender['balance'] += payload['amount']
            lender['owed_by'][borrower['name']] = payload['amount']

            borrower['balance'] -= payload['amount']
            borrower['owes'][lender['name']] = payload['amount']

            return json.dumps({'users': [lender, borrower]})

database = {
    "users": [
        {"name": "Adam", "owes": {}, "owed_by": {}, "balance": 0.0},
        {"name": "Bob", "owes": {}, "owed_by": {}, "balance": 0.0},
    ]
}
api = RestAPI(database)
payload = json.dumps({"lender": "Adam", "borrower": "Bob", "amount": 3.0})
print(api.post("/iou",payload))



