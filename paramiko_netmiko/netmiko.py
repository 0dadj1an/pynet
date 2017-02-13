from netmiko import ConnectHandler
from datetime import datetime

def main():
    router01 = {
        'device_type': 'cisco_ios',
        'ip':   '10.10.10.227',
        'username': 'pyclass',
        'password': 'password',
        'verbose': False,
     }
    
     arista_veos_sw = {
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

 