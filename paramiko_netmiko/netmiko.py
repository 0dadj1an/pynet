import netmiko
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

router02 = {
     'device_type': 'cisco_asa',
     'ip': '10.10.10.10',
     'username': 'admin',
     'password': 'password',
     'secret': 'secret',
     'verbose': False,
 }

arista = {
     'device_type': 'arista_eos',
     'ip':   '10.10.10.227',
     'username': 'admin1',
     'password': 'password',
     'port': 8522,               # there is a firewall performing NAT in front of this device
     'verbose': False,
 }

junipe = {
     'device_type': 'juniper',
     'ip':   '184.105.247.76',
     'username': 'pyclass',
     'password': 'password',
     'port': 9822,               # there is a firewall performing NAT in front of this device
     'verbose': False,
 }

devices = [router01, router02, arista, juniper] 


if __name__ == "__main__":
    main()
