from ncclient import manager
from devices import router
import xml.dom.minidom #prettify xml output
import xmltodict 
from pprint import pprint

config_template = open('config.xml').read()

netconf_config = config_template.format(name='Loopback0',description='via netconf')
 
for device in router:
    m = manager.connect(host=device['host'], port=device['port'], username=device['username'],password=device['password'],hostkey_verify=False)
    print(device['dev'],device['host'])

    device_reply = m.edit_config(netconf_config,target='running')
    print(device_reply)

    #config = m.get(filter)
    
    #display as XML
    #config_xml_pretty = (xml.dom.minidom.parseString(str(config))).toprettyxml(indent='  ')
    #print(config_xml_pretty)
    #print('-'*75)

    #convert to parsable dictionary
    #config_dict = xmltodict.parse(config.xml)
    #print(config_dict['rpc-reply'].keys())
    #pprint(config_dict['rpc-reply']['data'])
    #interface = config_dict['rpc-reply']['data']['interfaces-state']['interface']
    #int_name = interface['name']['#text']
    #int_status = interface['admin-status']
    #print(f'Interface name: {int_name}')
    #print(f'Interface status: {int_status}')
    #print('-'*75)
    m.close_session()
