import requests

AUT_KEY = "Bearer meghna5negi10lko"
USERNAME = "925341593a7a285a2549cde1596d5cd6"
PROJECT_NAME = "flightPricesTracker"
SHEET_NAME = "flights"
SHEETY_ENDPOINT = f"https://api.sheety.co/{USERNAME}/{PROJECT_NAME}/{SHEET_NAME}"

SHEETY_HEADER = {
    "Authorization": AUT_KEY
}

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self) -> None:
        self.response = requests.get(url=SHEETY_ENDPOINT,headers=SHEETY_HEADER)

    def get_codeList(self):
        flights_list = self.response.json()['flights']
        code_list = []
        for flight in flights_list:
            code_list.append(flight['iataCode'])
        return(code_list)
        
    def get_prices(self, code):
        flights_list = self.response.json()['flights']
        for flight in flights_list:
            if(flight['iataCode'] == code.upper()):
                return(flight['lowestPrice'])
