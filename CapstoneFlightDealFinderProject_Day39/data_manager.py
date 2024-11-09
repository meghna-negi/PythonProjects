import requests

AUT_KEY = ""
USERNAME = ""
PROJECT_NAME = "flightPricesTracker"
SHEET_NAME = "flights"
SHEETY_ENDPOINT = f"https://api.sheety.co/{USERNAME}/{PROJECT_NAME}/{SHEET_NAME}"

SHEETY_HEADER = {
    "Authorization": f'Bearer {AUT_KEY}'
}

class DataManager:
    #This class reads and writes into the google sheets using SHEETY API
    def __init__(self) -> None:
        self.response = requests.get(url=SHEETY_ENDPOINT,headers=SHEETY_HEADER)
    
    def set_code(self,code,id):
        column_data = {
            "flight": {
                "iataCode": code,
            }
        }
        sheety_response = requests.put(url=f'{SHEETY_ENDPOINT}/{id}',json=column_data,headers=SHEETY_HEADER)

    def set_price(self,price,id):
        column_data = {
            "flight": {
                "lowestPrice": price,
            }
        }
        sheety_response = requests.put(url=f'{SHEETY_ENDPOINT}/{id}',json=column_data,headers=SHEETY_HEADER)