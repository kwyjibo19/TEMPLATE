import requests
import json
from pprint import pprint
from devices import router



payload = {}
headers = {
  'Accept': 'application/yang-data+json',
  'Content-Type': 'application/yang-data+json'
}

for device in router:
    print('-'*75)
    print(device['dev'],device['host'])

    url = f"https://{device['host']}/restconf/data/ietf-interfaces:interfaces/interface=Loopback0"

    response = requests.request("GET", url, headers=headers, data = payload, auth=(device['username'],
        device['password']), verify = False)

#print(response.text.encode('utf8'))

#convert to dict
    pprint(response.json())
