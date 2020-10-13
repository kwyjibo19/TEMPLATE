import requests
import json

url_base = 'http://127.0.0.1:8080/api'
auth = ('admin','admin')

#'application/vnf.yang.api+json',
#'application/vnf.yang.datastore+json',
#'application/vnf.yang.data+json',

headers = {'Accept' : 'application/vnd.yan.collection+json'}

response = requests.get(f'{url_base}/running/devices/device', auth=auth, headers=headers).json()

devices=response['collection']['tailf-ncs:device']
for device in devices:
    #print(f'Name: {device['name']}')
    #print(f'IP: {device['address']}')
    #print(f'SSH Port: {device['port']}')
    #print(f'Auth Group: {device['authgroup']}')
    print(device)
    print(' ')
