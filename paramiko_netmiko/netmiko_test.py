from netmiko import ConnectHandler


def showArp(devices):
    
    for device in devices:
        conn = ConnectHandler(**device)
        output = conn.send_command("show arp")
        print "\n\n####### Device {0}#######".format(device['device_type'])
        print "\n\n####### Device {0}#######".format(device['ip'])
        print output
        print "############ END  ##############"
   
    
def checkConfigMode(devices):
    
    for device in devices:
        conn = ConnectHandler(**device)
        output = conn.check_config_mode()
        print "\n\n####### Device {0}#######".format(device['device_type'])
        print output
        print "############ END  ##############"
   
def enterConfigMode(devices):
    for device in devices:
        conn = ConnectHandler(**device)
        output = conn.config_mode()
        print "\n\n####### Device {0}#######".format(device['device_type'])
        print output
        output = conn.check_config_mode()
        print output
        print "############ END  ##############"

def loggingBuffered(devices):
    for device in devices:
        conn = ConnectHandler(**device)
        print "\n\n####### Device {0}#######".format(device['device_type'])
        output = conn.config_mode()
        print output
        output = conn.send_command("loggin buffered 65000")
        
        print output
        print "############ END  ##############"
        
def fromFile(devices):
    for device in devices:
        conn = ConnectHandler(**device)
        conn.config_mode()
        output = conn.send_config_from_file(config_file='config_file.txt')
        print "\n\n####### Device {0}#######".format(device['device_type'])
        print output
        print "############ END  ##############"
    
            
def showCommand(devices, command):
    for device in devices:
        conn = ConnectHandler(**device)
        output = conn.send_command(command)
        print "\n\n####### Device {0}#######".format(device['device_type'])
        print output
        print "############ END  ##############"
 
def sendCommands(devices, commands):
    for device in devices:
        conn = ConnectHandler(**device)
        output = conn.send_config_set(commands)
        print "\n\n####### Device {0}#######".format(device['device_type'])
        print output
        print "############ END  ##############"
 
        


def main():
    
    pasword_cisco = raw_input("enter Cisco router password:\n")
    password_juniper = raw_input("Enter Juniper password:\n")
    
    router01 = {
         'device_type': 'cisco_ios',
         'ip':   '184.105.247.70',
         'username': 'pyclass',
         'password': pasword_cisco,
         'verbose': False,
     }
    
    router02 = {
         'device_type': 'cisco_ios',
         'ip':   '184.105.247.71',
         'username': 'pyclass',
         'password': pasword_cisco,
         'verbose': False,
     }
 
    juniper_srx = {
         'device_type': 'juniper',
         'ip':   '184.105.247.76',
         'username': 'pyclass',
         'password': password_juniper,
         'port': 22,               # there is a firewall performing NAT in front of this device
         'verbose': False,
     } 
    
    devices_all = [router01, router02, juniper_srx] 
    devices_cisco = [router01, router02]
    
    commands = ['loggin buffered 65000']
    
    
    
    showArp(devices_all)
    #enterConfigMode(devices_cisco)
    #checkConfigMode(devices_cisco)
    #loggingBuffered(devices_cisco)
    fromFile(devices_cisco)
    #exitConfigMode(devices_cisco)
    sendCommands(devices_cisco, commands)
    showCommand(devices_cisco, "show run | in loggi")
    
    
    
    
if __name__ == "__main__":
    main()
    
