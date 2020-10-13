import jinja2
import netmiko
import pyscreenshot as ImageGrab

config_template = "config_template.j2"
csv_file = "parameters.csv"
csv_list = []

csv = (open(csv_file).read()).splitlines() #split lines into a list
csv_key = (csv[0]).split(';') #remove comma and separate into a list for header row

for row in range(1,len(csv)): #iterate through rows excluding header
    csv_dict = {}
    csv_value = (csv[row]).split(';') #remove comma and separate into a list for parameter row
    for parameter in range(0,len(csv_value)): #iterate through parameters
        csv_dict[csv_key[parameter]] = csv_value[parameter] #create dictionary by using header as key and parameter as value
    csv_list.append(csv_dict) #append all values to empty list

env = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath="."))
template = env.get_template(config_template)

for device in csv_list:
    config = template.render(device)
    with open(device['hostname']+'.cfg','w') as f:
        f.write(config)
        f.close()
        dev = device['management']
        print('### CONFIGURING ' + device['hostname'] + ' ###')

        connection = netmiko.ConnectHandler(ip=dev, device_type='cisco_ios', username='admin', password='admin')
        cfg = connection.send_config_from_file(device['hostname']+'.cfg')
        print(connection.find_prompt())
        ss = connection.send_command('show ip int brief')
        print(ss)

        screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.
        currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
        pyautogui.moveTo(100, 150) # Move the mouse to XY coordinates.
        pyautogui.click()          # Click the mouse.
        pyautogui.click(100, 200)  # Move the mouse to XY coordinates and click it.
        pyautogui.click('button.png') # Find where button.png appears on the screen and click it.
        im = ImageGrab.grab()
        im.save(device['hostname']+'.png')
