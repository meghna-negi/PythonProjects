from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
import datetime as dt

def main()->None:
    data = DataManager()
    sheet_data = data.get_data()

    #Traverse through all the destination cities in the sheet
    for flight in sheet_data:
        #If IATA Codes are empty search for them in city search API
        if(flight['iataCode'] == ''):
            flight_search = FlightSearch(flight['city'])
            code = flight_search.set_code()
            data.set_code(code,flight['id'])
        #If IATA code is anything except 'N/A' search for the lowest price
        #If found then send the mail
        elif(not (flight['iataCode'] == 'N/A')):
            presentday = dt.datetime.now()
            tomorrow = presentday + dt.timedelta(1)
            flight_data = FlightData(flight['iataCode'],tomorrow.strftime("%Y-%m-%d"),flight['lowestPrice'])
            price = flight_data.getLowest_price()
            data.set_price(price,flight['id'])
            if(price != flight['lowestPrice']):
                mail = NotificationManager()
                mail.send_mail("FRA",flight['iataCode'],price)
            else:
                print("Couldn't find the better deal")
        else:
            print("No data for this city")

if __name__ == "__main__":
    main()