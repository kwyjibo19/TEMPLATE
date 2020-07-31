import requests
import json
from pprint import pprint

router = {
    'dev':'R1',
    'host':'172.16.152.141',
    'port':'830',
    'username':'admin',
    'password':'admin'
}

payload = {}
headers = {
  'Accept': 'application/yang-data+json',
  'Content-Type': 'application/yang-data+json'
}


url = f"https://{router['host']}/restconf/data/ietf-interfaces:interfaces/interface=Loopback0"

response = requests.request("GET", url, headers=headers, data = payload, auth=(router['username'],
        router['password']), verify = False)

#print(response.text.encode('utf8'))

#convert to dict
pprint(response.json())
