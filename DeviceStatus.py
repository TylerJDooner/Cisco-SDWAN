import requests

url = "https://192.168.254.107:8443/dataservice/device"

payload = {}
headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
  'Cookie': 'JSESSIONID=t0cPhG-Jhs1H9IYwgHzuGdZTYu3ucp_lciVXJ9ad.4f5973a1-9445-4fdc-af2a-1e07275ffcc9'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response)

