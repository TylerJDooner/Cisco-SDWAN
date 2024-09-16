import requests
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def getOMProutes(url, session, device_id):
    omp_ROUTES = f"/dataservice/device/omp/routes/received?deviceId={device_id}"
    sesh = session
    ompRoutes = sesh.get(
        url=f"{url}{omp_ROUTES}", verify=False).json()
    
    #print(omproutes.text)
    return ompRoutes