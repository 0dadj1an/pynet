from netmiko import ConnectHandler
from datetime import datetime



def showArp(devices):
    
    time= datetime.now()
    for device in devices:
        conn = ConnectHandler(**device)
        output = conn.send_command("show arp")
        print "\n\n####### Device {0}#######".format(device['device_type'])
        print output
        print "############ END  ##############"
    etime = datetime.now()
    total = time - etime
    print total
    
def checkConfigMode(devices):
    time= datetime.now()
    for device in devices:
        conn = ConnectHandler(**device)
        output = conn.check_config_mode()
        print "\n\n####### Device {0}#######".format(device['device_type'])
        print output
        print "############ END  ##############"
    etime = datetime.now()
    total = time - etime
    print total
    


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
    showArp(devices_all)
    checkConfigMode(devices_cisco)
    
    
if __name__ == "__main__":
    main()
    
