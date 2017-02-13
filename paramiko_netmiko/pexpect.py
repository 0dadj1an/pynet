import pexpect
import sys
import time

def main():
    
    
    ip = '184.105.247.70'
    username = 'pyclass'
    password = '88newclass'
    port = 8022
    remote_conn = pexpect.spawn('ssh -l {} {} -p {}'.format(username, password, port))
    remote_conn02 = pexpect.spawn()
    remote_conn.timeout = 3
    
    remote_conn.expect('ssword:')
    remote_conn.sendline(password)
    
    remote_conn.expect('#')
    remote_conn.sendline('show ip int brief')
    remote_conn.expect('#')
    remote_conn.sendline('conf t')
    remote_conn.expect('#')
    remote_conn.sendline('loggin buffered 65000')
    remote_conn.expect('#')
    remote_conn.sendline('exit')
    remote_conn.expect('#')
    remote_conn.sendline('show run')
    remote_conn.expect('#')
    
    print remote_conn.before
    

if __name__ == "__main__":
    main()
    
    
