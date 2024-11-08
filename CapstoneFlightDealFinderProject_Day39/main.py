
from data_manager import DataManager
from flight_search import FlightSearch

def main()->None:
    data = DataManager()
    sheet_data = data.get_data()
    print(sheet_data)

    for flight in sheet_data:
        if(flight['iataCode'] == ''):
            flight_search = FlightSearch(flight['city'])
            code = flight_search.set_code()
            data.set_code(code,flight['id'])

if __name__ == "__main__":
    main()