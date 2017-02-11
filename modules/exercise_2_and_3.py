import telnetlib
import time
import socket
import sys


class ConnectDevice02(object):
    
    
    def __init__(self, ip, username, password):
        self.ip = ip
        self.username = username
        self.password = password
        self.timeout = 6
        self.port =23
        try:
            self.connection = telnetlib.Telnet(self.ip, self.port, self.timeout)
        except socket.timeout:
                sys.exit("Unable to connect due timeout")
        self.telnetLogin()
        
    def telnetSend(self, command):
        
         command = command.rstrip()
         self.connection.write(command + '\n')
         time.sleep(1)
         return self.connection.read_very_eager()


    def telnetLogin(self):
         output = self.connection.read_until("sername:", self.timeout)
         if output:
              self.connection.write(self.username +'\n')
         else:
              print "Not possible to add username"
         
         output = output + self.connection.read_until("ssword:", self.timeout)
         if output:
               self.connection.write(self.password +'\n')
         else:                                     
                print "Not possible to add username"

         #print output

    def telnetClose(self):
         self.connection.close()


            
def main():
    
    ip_add = '184.105.247.70' ## raw_input("write IP" + '\n')
    username = 'pyclass' ## raw_input("write username" + '\n')
    password = '88newclass' ##raw_input("write password" + '\n')
    command = raw_input("enter command to be executed" + '\n')    

    new_connection = ConnectDevice02(ip_add, username, password)
    output = new_connection.telnetSend("terminal length 0")
    output = new_connection.telnetSend(command)
    print output
    new_connection.telnetClose()

if __name__ == "__main__":
    main()
    
