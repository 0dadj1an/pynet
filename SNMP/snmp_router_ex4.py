#!/usr/bin/env python


import snmp_helper
   
ip_list = []

sys_desc = ''
sys_name = ''
community_str = ''




def checkIPFormat(ip_add):
    
    '''
    testing function if IP address entered into cmd is correct(all octetcs and only numbers)
    '''
    checker = 1
    ip4_sections = ip_add.split(".")
    if len(ip4_sections) == 4:
        for item in ip4_sections:
            if item.isdigit() == False:
                checker = 0
    else:
        print "Bad IP format, try it again"           
                
    if checker == 1:
        return  True
       
    else:
         print "Bad IP format, try it again"
         return False 

def loadData():
    '''
    loading user data (input) for sys_desc, sys_name, IP and snmp community string
    '''
    print "This is SNMP MIB2 sysName and sysDescr checke "
    #accessing global variables
    global sys_desc
    global sys_name
    global community_str
    global ip_list
    #load data
    sys_desc = raw_input("Enter sys desc:" + '\n');
    sys_name = raw_input("Enter sys name:" + '\n');
    community_str = raw_input("Enter community string:" + '\n');
    
    print "Enter IP addresses for connection and end with key word CLOSE:" + '\n'
    # in this cyklus IP addresses for routers are loaded 
    while True:
         a = raw_input()
         if a == 'CLOSE':
             break
         else:
              if checkIPFormat(a) == True:
                 ip_list.append(a)
                 
def getData(item):
    '''
    getting correct list for snmp_helper ->tuple with IP, string and port
    '''
    temp_list = (item, community_str, 161)
    return temp_list
           
    

def main():
    
    
    '''
    main function for getting snmp data, printing sysName and sysDescr values
    '''
    #loads data from user
    loadData()
    #iterates list of IPs entered during main prompt
    for item in ip_list:
        device_list = getData(item)# setting up correct tuple
        print "##########################"
        for oidvalue in (sys_desc, sys_name): # iterate through OID values
             snmp_data = snmp_helper.snmp_get_oid(device_list, oid=oidvalue)
             output = snmp_helper.snmp_extract(snmp_data) 
             print output
        print "##############"
                                                                                                                  

if __name__ == "__main__":
    main()
    

