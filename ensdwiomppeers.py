import requests
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def getOMPpeers(url, session, device_id):
    omp_peers = f"dataservice/device/omp/peers?deviceId={device_id}"
    sesh = session
    omppeers = sesh.get(
        url=f"{url}{omp_peers}", verify=False).json()
    
    #print(omppeers.text)
    return omppeers