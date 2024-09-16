import requests
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def getTLOCroutes(url, session, device_id):
    tloc_ROUTES = f"/dataservice/device/omp/tlocs/received?deviceId={device_id}"
    sesh = session
    tlocRoutes = sesh.get(
        url=f"{url}{tloc_ROUTES}", verify=False).json()
    
    #print(tlocroutes.text)
    return tlocRoutes

