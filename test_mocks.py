## Test Mocks ##
# This file contains the mocks for the tests. Often, in a code function, the execution may be dependent on some backend service or some other function. In such cases, we can mock the function to return a predefined value. This is done to test the function in isolation.

import pytest
import requests
import sqlite3


# This front-end code depends on a backend weather api for it's functionality.
def get_weather(city):
    response = requests.get(f"https://api.weather.com/v1/{city}")
    if response.status_code == 200:
        return response.json()
    else:
        raise ValueError("Could not fetch the data")
    
## Therefore for testing this function, we need to mock(fake) the requests.get function to return a predefined value(fake data). This is done using the following code. 

def test_get_weather(mocker):
    mock_get = mocker.patch("requests.get")
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"temp": 25, "humidity": 50} # The fake json file returned when return value is called.
    
    result = get_weather("Dubai")
    
    assert result == {"temp": 25, "humidity": 50}
    mock_get.assert_called_once_with("https://api.weather.com/v1/Dubai") # To ensure if the function was called with the correct url.



# Adding the user info into database(db file) using the following function.
def save_user(name,age):
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO users VALUES (?,?)",(name,age))
    conn.commit()
    conn.close()
    
    
# Gonna mock the connect function, so that we don't actually need to set up the database and connect it.

def test_save_user(mocker):
    mock_connect = mocker.patch("sqlite3.connect")
    mock_cursor = mock_connect.return_value.cursor.return_value
    
    save_user("John",25)
    
    mock_connect.assert_called_once_with("test.db")
    mock_cursor.execute.assert_called_once_with("INSERT INTO users VALUES (?,?)",("John",25)
    )  
    

## Mocking an API client class
class api_client:
    "Simulates an external API client"
    def get_user_data(self,user_id):
        response = requests.get(f"https://api.com/v1/users/{user_id}")
        if response.status_code == 200:
            return response.json()
        raise ValueError("API request failed")


class UserService:
    "Uses API client to fetch user data and process it"
    def __init__(self,api_client):
        self.client = api_client
    
    def get_user_name(self,user_id):
        data = self.client.get_user_data(user_id)
        return data["name"].upper()
    

def test_get_username(mocker):
    mock_client = mocker.Mock(spec=api_client) # Mocking of the api_client class
    
    mock_client.get_user_data.return_value = {"id":1,"name":"John"}
    
    user_service = UserService(mock_client)
    
    result = user_service.get_user_name(1)
    
    assert result == "JOHN"
    mock_client.get_user_data.assert_called_once_with(1)                      