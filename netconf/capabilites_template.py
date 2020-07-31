from ncclient import manager
from devices import router

for device in router:
    m = manager.connect(host=device['host'], port=device['port'], username=device['username'],password=device['password'],hostkey_verify=False)
    print(device['host'])

    for capability in m.server_capabilities:
        print('-'*75)
    
        print(capability)
        

    m.close_session()
