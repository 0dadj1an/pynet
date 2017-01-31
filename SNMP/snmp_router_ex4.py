#!/usr/bin/env python


import snmp_helper
   
sys_desc = raw_input("Enter sys desc:" + '\n')
sys_name = raw_input("Enter sys name:" + '\n')
community_str = raw_input("Enter community string:" + '\n')
ip_list = []


def checkIPFormat(ip_add):
    
    '''
    testing function if IP address entered into cmd is correct
    '''
    checker = 1
    ip4_sections = ip_add.split(".")
    if len(ip4_sections) == 4:
        for item in ip4_sections:
            if item.isdigit() == False:
                checker = 0
                
    if checker == 1:
        return  True
       
    else:
        return False 

 

def main():
    
    '''
    main function for inswerting data about snmp and devices, printing sysName and sysDescr values
    '''

    print "Enter IP addresses for connection and end with key word CLOSE:" + '\n'


    while True:
         a = raw_input()
         if a == 'CLOSE':
            break
         else:
              if checkIPFormat(a) == True:
                   ip_list.append(a)
              else:
                   print "Bad IP format, try it again"
           
    for item in ip_list:
        print "##########################"
        for oid in (sys_desc, sys_name):
             snmp_data = snmp_helper.snmp_get_oid(item, oid=oid)
             output = snmp_helper.snmp_extract(snmp_data) 
             print output
             print "##############"
                                                                                                                         

if __name__ == "__main__":
    main()
