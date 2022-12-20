# healthjump-assessment
Assessment to create an api extract using the Healthjump api.

Hello, for my solution I've created a wrapper for the Healthjump api called HealthjumpAPI() that handles authentication and get requests
Firstly, ensure you have the requests, requests_cache, and urllib modules installed
Next to create an instance of the healthjump api by calling the HealthjumpAPI() class

  api = HealthjumpAPI()

You can now use this instance to perform api calls. This method call will return the data portion of the demographics endpoint

  demographics = api.get_demographics()

You can also pass optional keyword parameters to the get_demographics() method for more refined requests

  demographics = api.get_demographics(params={"first_name": "btwn\~Patient_A~Patient_C"})

You can now iterate through demographics and access certain fields

  for patient in demographics:
    print(patient["first_name"])
    
I went with this route for this assignment so that it can be easily extended to account the rest of the endpoints in the Healthjump api
I've also included global constants for the email, password, url, client_id, and secret_key so it can be modified for different users and/or clients
