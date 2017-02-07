import paramiko
import time


def showVersion(self,connection):
         connection.send("show version\n")
         return connection.recv(5000)

def enterConfig(self, connection):
         connection.send("conf t\n")
         return connection.recv(5000)


def main():
    
     ip = '184.105.247.70'
     username = 'pyclass'
     password = '88newclass'
     
     remote_conn=paramiko.SSHClient()
    # avoid issues with not trusted targets
     remote_conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
     remote_conn.connect(ip, username=username, password=password, look_for_keys=False, allow_agent=False)
     remote_conn02 = remote_conn.invoke_shell()
     output = showVersion(remote_conn02)
     print output

    









