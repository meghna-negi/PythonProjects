import requests

AMADEUS_ENDPOINT = 'https://test.api.amadeus.com/v1/reference-data/locations/cities'
ACCESS_TOKEN = ''

HEADERS = {
    "Authorization": f'Bearer {ACCESS_TOKEN}'
}

class FlightSearch:
    #This class searches for the city in the city search and gives iata code
    def __init__(self,city) -> None:
        self.citySearch_param = {
            'keyword': city
        }
    
    def set_code(self):
        try:
            response = requests.get(url=AMADEUS_ENDPOINT,headers=HEADERS,params=self.citySearch_param)
            code = response.json()["data"][0]["iataCode"]
            
        except:
            print("No data available for this city")
            code = "N/A"

        finally:
            return(code)
        