from netmiko import ConnectHandler
from datetime import datetime



def connect(devices):
    
    time= datetime.now()
    for device in devices:
        conn = ConnectHandler(device)
        output = conn.send_command("show arp")
        print "\n\n####### Device {0}#######".format(device['device_type'])
        print output
        print "############ END  ##############"
    etime = datetime.now()
    total = time - etime
    print total


def main():
    
    router01 = {
         'device_type': 'cisco_ios',
         'ip':   '10.10.10.227',
         'username': 'pyclass',
         'password': 'password',
         'verbose': False,
     }
    
    arista_sw = {
         'device_type': 'arista_eos',
         'ip':   '10.10.10.227',
         'username': 'admin1',
         'password': 'password',
         'port': 8522,               # there is a firewall performing NAT in front of this device
         'verbose': False,
     }
 
    juniper_srx = {
         'device_type': 'juniper',
         'ip':   '10.10.10.227',
         'username': 'pyclass',
         'password': 'password',
         'port': 9822,               # there is a firewall performing NAT in front of this device
         'verbose': False,
     } 
    
    devices = [router01, router02, arista_sw, juniper_srx] 
    connect(devices)
    
if __name__ == "__main__":
    main()
    
