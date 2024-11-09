import requests

AMADEUS_ENDPOINT = 'https://test.api.amadeus.com/v2/shopping/flight-offers'
ACCESS_TOKEN = ''

HEADERS = {
    "Authorization": f'Bearer {ACCESS_TOKEN}'
}
class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self,dest_code,today,price) -> None:
        self.FlightSearch_Parameters = {
            'originLocationCode': 'FRA',
            'destinationLocationCode': dest_code,
            'departureDate': today,
            'adults': 1,
            'nonStop': "true",
            'currencyCode': 'EUR'
        }
        self.response = requests.get(url=AMADEUS_ENDPOINT,headers=HEADERS,params=self.FlightSearch_Parameters)
        self.price = price

    def getLowest_price(self):
        try:
            price_data = self.response.json()['data']
            for prices in range(len(price_data)):
            
                if(float(price_data[prices]['price']['grandTotal']) < self.price):
                    self.price = float(price_data[prices]['price']['grandTotal'])
            
        except:
            print("No flight data available for tomorrow for this route.")
        finally:
                return(self.price)