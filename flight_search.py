import requests

flight_endpoint = "https://tequila-api.kiwi.com"

flight_search_endpoint = f"{flight_endpoint}/locations/query"

API_KEY = "dzfBxZUazLmMCXmClcHYd8TJzk4e6B7L"

class FlightSearch:
    def get_flight_search(self,destination_name):
        headers = {
            "apiKey":API_KEY,
            "Content-Type":"application/json"
        }
        params = {
            "term": destination_name,
            "location_types": "city"

        }
        response = requests.get(url=flight_search_endpoint,params=params,headers=headers)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code


