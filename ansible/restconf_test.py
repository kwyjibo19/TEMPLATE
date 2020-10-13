import requests
import json
from pprint import pprint

router = {
    'dev':'R2',
    'host':'172.16.152.142',
    'port':'443',
    'username':'admin',
    'password':'admin'
}

payload = {}
headers = {
    'Accept': 'application/yang-data+json',
    'Content-Type': 'application/yang-data+json'
}


url = f"https://{router['host']}/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet1"

response = requests.get(url, headers=headers, data = payload, auth=(router['username'],
    router['password']), verify = False)

#print(response.text.encode('utf8'))

#convert to dict
pprint(response.json())
