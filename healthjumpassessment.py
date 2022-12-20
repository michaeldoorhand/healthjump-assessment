import requests
import requests_cache
import urllib
#Healthjump api: https://apidocs.healthjump.com/

#Constants
EMAIL = "sandbox@healthjump.com"
PASSWORD = "R-%Sx?qP%+RN69CS"
URL = "https://api.healthjump.com"
CLIENT_ID = "SBOX02"
SECRET_KEY = "yemj6bz8sskxi7wl4r2zk0ao77b2wdpvrceyoe6g"

#Create a cache for patients which expires after 180 seconds
requests_cache.install_cache('patient_cache', expire_after = 180)

#Healthjump API wrapper to easily query data from the Healthjump API.
class HealthjumpAPI():
    def __init__(self):
        self.data = {"email":EMAIL, "password":PASSWORD}
        self.token = False

    #Sets the authorization token and calls the authentication endpoint 
    def __create_auth(self):
        if self.token:
            return True
        try:
            response = requests.post(URL + "/authenticate", json=self.data).json()
            self.token = response["token"]
        except requests.exceptions.RequestException as e: 
            return False

    #Queries the endpoint with the auth token and params and returns the formatted data 
    def __submit_get(self, endpoint, **kwargs):
        if len(kwargs) == 0:
            query = ''
        else:
            params = kwargs["params"]
            query =  urllib.parse.urlencode(params)
        self.__create_auth()
        headers = {"Secretkey": SECRET_KEY, "Authorization": "Bearer " + self.token}
        try:
            url = URL + "/hjdw/" + CLIENT_ID + "/" + endpoint + "?" + query
            response = requests.get(url, headers = headers).json()
        except requests.exceptions.RequestException as e: 
            return False
        return self.__format_response(response)

    #Returns the data section of the get from the endpoint
    def __format_response(self, response):
        return response["data"]

    #Gets the demographics with params
    def get_demographics(self, **kwargs):
        if len(kwargs) == 0:
            return self.__submit_get("demographic")
        else:
            params = kwargs["params"]
            return self.__submit_get("demographic", params = params)

    #Can be expanded to account for other endpoints

def main():
    #Create an instance of the API and call get_demographics with params
    api = HealthjumpAPI()
    demographics = api.get_demographics(params={"first_name": "btwn~Patient_A~Patient_C"})

    #Prints the first name of the queried demographics
    for patient in demographics:
        print(patient["first_name"])

main()