import requests
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# Defines a new funtion called getIPSECout. It takes in the parameters listed in parentheses. 
#IPSEC_out constreucts endpoint url path using an f string 
#Session parameter gets assigned to sesh
#IPSECout uses the .get method from the session "sesh" object to perform a get request 
#url combines the base url with the endpoiint path (IPSEC_out) to form the full url request. Verify false is used to disable ssl verification. .json() parses json response from 
##http request  and places it into a python dictionary. Structures the data returned from API call
#Return is used for returning the parsed json data from the api call. It allows us to use the data for further processing or to display 

def getIPSECout(url, session, device_id):
    IPSEC_out = f"/dataservice/device/ipsec/outbound?deviceId={device_id}"
    sesh = session
    IPSECout = sesh.get(
        url=f"{url}{IPSEC_out}", verify=False).json()
    
    #print(omppeers.text)
    return IPSECout
