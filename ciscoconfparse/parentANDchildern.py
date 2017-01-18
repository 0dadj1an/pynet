from ciscoconfparse import CiscoConfParse

parse = CiscoConfParse("config.txt")
serial_objs = parse.find_objects("^crypto map CRYPTO")
count=0
list_lengh = len(serial_objs)

for obj in serial_objs:
    print "Parent is:"
    print obj.text
    parent = serial_objs[count]
    list_a= parent.children
    print "Childerns are:"
    for child in list_a:
        print child.text
    



    
