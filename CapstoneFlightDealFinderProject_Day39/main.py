#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
import datetime as dt

def main()->None:
    data = DataManager()
    today = dt.datetime.now().strftime("%Y-%m-%d")
    cities = data.get_codeList()
    for city in cities:
        flight_search = FlightSearch(city,today)
        print(flight_search.get_data())

if __name__ == "__main__":
    main()