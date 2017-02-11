import pexpect
import time
import getpass



def main():
    
    
    ip = '184.105.247.70'
    username = 'pyclass'
    password = '88newclass'
    port = 8022
    remote_conn = pexpect.spawn('ssh -l {} {} -p {}'.format(username, password, port))
    remote_conn.timeout = 3
    remote_conn.expect('ssword:')
    remote
    
   

if __name__ == "__main__":
    main()
    
    
