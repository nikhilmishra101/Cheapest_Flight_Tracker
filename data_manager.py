from pprint import pprint
import requests

sheety_url = "https://api.sheety.co/1c897754ab0a366103580bda59de03dd/flightDeals/prices"


class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=sheety_url)
        data = response.json()
        # pprint(data)
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
                url=f"{sheety_url}/{city['id']}",
                json=new_data
            )

            print(response.text)
