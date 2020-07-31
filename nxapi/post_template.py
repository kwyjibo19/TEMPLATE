import requests
import json

#only post

router = {
    'dev':'R1',
    'host':'172.16.152.145',
    'port':'830',
    'username':'admin',
    'password':'admin'
}

target = 'http://172.16.152.145/ins'
username = 'admin'
password = 'admin'

payload = {}
headers = {
  'Content-Type': 'application/json'
}

showcmd = {
  "ins_api": {
    "version": "1.2",
    "type": "cli_show",
    "chunk": "0",
    "sid": "1",
    "input": "show ip int brief",
    "output_format": "json"
  }
}

print(showcmd)

print(json.dumps(showcmd))

response = requests.post(
        target,
        data=json.dumps(showcmd),
        headers=headers,
        auth=(router['username'],router['password']),
        verify = False).json()


print(json.dumps(response, indent = 2, sort_keys = True))
