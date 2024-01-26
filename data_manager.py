import requests
from pprint import pprint
LINK = "https://api.sheety.co/58e36deebcd1bc3094d6c9bb62a05a92/flightDeals/prices"
LINK1 = "https://api.sheety.co/58e36deebcd1bc3094d6c9bb62a05a92/flightDeals/users"
class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=LINK)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{LINK}/{city['id']}",
                json=new_data
            )
            print(response.text)

    def get_customer_emails(self):
        customers_endpoint = LINK1
        response = requests.get(url=customers_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data