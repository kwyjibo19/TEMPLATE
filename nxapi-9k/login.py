import requests
from pprint import pprint

url = "https://172.16.152.150/api/aaaLogin.json"

payload = "{\n  \"aaaUser\":{\n    \"attributes\":{\n      \"name\":\"admin\",\n      \"pwd\":\"Cisco123\"\n    }\n  }\n}\n"
headers = {
  'Authorization': 'Basic YWRtaW46Q2lzY28xMjM=',
  'Content-Type': 'text/plain',
  'Cookie': 'nxapi_auth=dzqnf:YNxJgXj1fA96ZYRlaeCboqrsfNU=; APIC-cookie=qYHlT7SJtS4PKSPA+s1RkDE+0cwjBn1Zqvjdedka2L7ocwU3h3OJAHcKAMXQAMLgZq7AHnc5IynsGJS2ibASCHjbm6Nd1i0MI/LrH20Qq/0jTAvD0ttrSCSdYG6Y/9njEe6LOb6Q4uHmq9NiMjLPFv6n+PRs9PTYlMGa9+Mv5TQ='
}

response = requests.post(url, headers=headers, data = payload, verify = False).json()

#pprint(response)

token = response['imdata'][0]['aaaLogin']['attributes']['token']

print(token)

cookies={}
cookies['APIC-cookie']=token


url = "https://172.16.152.150/api/node/mo/sys/intf/phys-[eth1/1].json"

payload = "{\n    \"l1PhysIf\": {\n        \"attributes\": {\n            \"descr\": \"via PostmanPy\",\n        }\n    }\n}"
headers = {

  'Authorization': 'Basic YWRtaW46Q2lzY28xMjM=',
  'Content-Type': 'text/plain',

}

post_response = requests.post(url, headers=headers, data = payload, cookies=cookies, verify = False).json

pprint(post_response)
