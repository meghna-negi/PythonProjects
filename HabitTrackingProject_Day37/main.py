import requests
import datetime as dt

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = ""  #Your username
TOKEN = "" #Your secret token

#Step 1
#Add spme token starting with alphabets and can have numbers
#Add username in lower case
user_parameters = {
    "token": "", 
    "username": "",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

#Will create the user and print success if operation is successful
response = requests.post(url=pixela_endpoint,json=user_parameters)
print(response.text)

#Step 2
#Endpoint for creating a graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

#Configuration to create a graph
#Graph ID and name with unit and the type of values of habit to track
graph_config = {
    "id": 'graph1',
    "name": 'coding graph',
    "unit": 'min',
    "type": 'int',
    "color": 'ajisai'
}

#Header inclusing the token created in step 1
headers = {
    "X-USER-TOKEN": TOKEN
}

#Post operation to the API, creating a new graph for the user
#Prints the success message if operation is successful
graph_response = requests.post(url=graph_endpoint,json=graph_config,headers=headers)
print(graph_response.text)

#Step 3
#Endpoint to post the data onto the pixel in the graph
post_graph_endpoint =  f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

#Getting todays date and posting the qunatity for the date
#The date is converted into expected format
today = dt.datetime.now()
todays_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "200"
}

#Post operation to the API to write the today's data on to the pixel
#Prints the success message if operation is successful
adding_pixel_response = requests.post(url=post_graph_endpoint,json=todays_data,headers=headers)
print(adding_pixel_response.text)

#Step 4
#Put operation to update the yesterdays data
put_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/20241103"

updated_data = {
    "quantity": "150"
}

#Put operation to the API to update the data in the graph
#Prints the success message if operation is successful
updating_pixel_response = requests.put(url=put_graph_endpoint,json=updated_data,headers=headers)
print(updating_pixel_response)

#Step 5
#Delete operation to delete the data of the pixel
#Prints the success message if operation is successful
delete_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/20241105"
deleting_pixel_response = requests.delete(url=delete_graph_endpoint,headers=headers)
print(deleting_pixel_response)