import requests

AMADEUS_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self,code,today) -> None:
        self.Amadeus_parameter = {
            "originalLocationCode":"FRA",
            "destinationLocationCode": code,
            "departureDate": today,
            "adults": 1
        }
        self.response = requests.get(url=AMADEUS_ENDPOINT,params=self.Amadeus_parameter)
    
    def get_data(self):
        return(self.response.json())