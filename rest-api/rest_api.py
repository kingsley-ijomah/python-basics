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
            result = []
            for user in self.database['users']:
                if user['name'] == payload['lender']:
                    user['balance'] += payload['amount']
                    user['owed_by'] = {payload['borrower']: payload['amount']}
                elif user['name'] == payload['borrower']:
                    user['balance'] -= payload['amount']
                    user['owes'] = { payload['lender']: payload['amount'] }
                result.append(user)
            return json.dumps({ 'users': result })
                    


            # get lender
            lender = [lender for lender in self.database['users']
                    if lender['name'] == payload['lender']]
            # get borrower
            borrower = [borrower for borrower in self.database['users']
                    if borrower['name'] == payload['borrower']]
            return borrower
            # deduct amount from borrower
            # add deducted abount to lender


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
        {"name": "Bob", "owes": {}, "owed_by": {}, "balance": 0.0},
    ]
}
api = RestAPI(database)
payload = json.dumps({"lender": "Adam", "borrower": "Bob", "amount": 3.0})

print(api.post("/iou",payload))



