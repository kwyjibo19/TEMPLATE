from ncclient import manager
from devices import router
import xml.dom.minidom #prettify xml output

for device in router:
    m = manager.connect(host=device['host'], port=device['port'], username=device['username'],password=device['password'],hostkey_verify=False)
    print(device['host'])

    filter = '''
    <filter>
        <interfaces-state xmlns='urn:ietf:params:xml:ns:yang:ietf-interfaces'>
          <interface>
           <name>Loopback0</name>
          </interface>
        </interfaces-state>
    </filter>
    '''

    config = m.get(filter)
    
    config_xml_pretty = (xml.dom.minidom.parseString(str(config))).toprettyxml(indent='  ')
    print(config_xml_pretty)
    print('-'*75)

    m.close_session()
