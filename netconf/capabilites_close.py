from ncclient import manager

m =  manager.connect(host='172.16.152.141', port='830', username='admin',password='admin',hostkey_verify=False)

for capability in m.server_capabilities:
    print('-'*75)
    print(capability)

m.close_session()