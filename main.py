from UberEats import UberEats

if __name__ == "__main__":
    uber = UberEats(client_secret="", client_id="")

    uber.get_client_token()