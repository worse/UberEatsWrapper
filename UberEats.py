import requests

session = requests.session()


class UberEats:

    def __init__(self, client_secret, client_id):
        self.client_secret = client_secret
        self.client_id = client_id
        self.url = "https://login.uber.com/oauth/v2/token"

    def get_client_token(self):
        client_id = self.client_id
        client_secret = self.client_secret

        request = session.post(url=self.url, data={})

