import requests
from pprint import pprint
LINK = "https://api.sheety.co/58e36deebcd1bc3094d6c9bb62a05a92/flightDeals/prices"
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        link = LINK
        response = requests.get(url=link)
        data = response.json()
        self.destination_data = data["prices"]
        pprint(data)
        return self.destination_data

    def update_destination_code(self):
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


