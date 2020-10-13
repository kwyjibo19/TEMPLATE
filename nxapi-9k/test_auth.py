import requests
import json



url = 'http://172.16.152.150:8080/ins'
username = 'admin'
password = 'Cisco123'

headers = {
  'Content-Type': 'application/json'
}

payload = {
  "ins_api": {
    "version": "1.0",
    "type": "cli_show",
    "chunk": "0",
    "sid": "sid",
    "input": "show ip int brief",
    "output_format": "json"
  }
}



response = requests.post(
        url,
        data=json.dumps(payload), #convert to string
        headers=headers,
        auth=(username,password),
        verify = False).json()


#print(response)
#print(json.dumps(response, indent = 2, sort_keys = True))
#rdict = response

#print(rdict['ins_api']['outputs']['output']['body']['TABLE_intf']['ROW_intf']['intf-name'])


########### login ###########

auth_url = "https://172.16.152.150/api/aaaLogin.json"
auth_body = {
  "aaaUser":{
    "attributes":{
      "name":"admin",
      "pwd":"Cisco123"
    }
  }
}
auth_response = requests.post(
        auth_url,
        data=json.dumps(auth_body), #convert to string
        timeout=5,
        verify = False).json()

token = auth_response['imdata'][0]['aaaLogin']['attributes']['token']

cookies={}
cookies['APIC-cookie']=token
print(cookies)
