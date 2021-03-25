from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData

data_manager = DataManager()
flight = FlightSearch()


sheet_data = data_manager.get_destination_data()
flight_data = FlightData(sheet_data)

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight.get_flight_search(row["city"])
    #print(sheet_data)


    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()