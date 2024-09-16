import requests
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def getBFDsession(url, session, device_id):
    bfd_Session = f"/dataservice/device/bfd/sessions?deviceId={device_id}"
    sesh = session
    bfdSession = sesh.get(
        url=f"{url}{bfd_Session}", verify=False).json()
    
    #print(bfdsession.text)
    return bfdSession

