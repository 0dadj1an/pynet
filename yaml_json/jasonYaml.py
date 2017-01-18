

'''
create list and write elements into yaml and json files
'''
import json
import yaml



number_Str = raw_input("Write random number for list:\n") 
list_Gen = range(int(number_Str))
list_Gen.append({'vendor': 'Check Point', 'model': 'R77', 'IP': '10.1.1.1/24', "OS": "Gaia", "SNMP_RO":"ahojNazdar" })
list_Gen.append(raw_input("Write string to be added:\n"))


def writeFile():
    
    with open("yaml.yml", "w") as file:
        file.write(yaml.dump(list_Gen, default_flow_style = False))  
         
    with open("json.json", "w") as file:
        json.dump(list_Gen, file)
        
    
def openFile():
    
    with open("yaml.yml", "r") as file:
         new_list_yml = yaml.load(file)
    
    with open("json.json", "r") as file:
         new_list_json = json.load(file)     
    
    printList(new_list_yml, new_list_json)


def printList(a, b):
    
    print a
    print "#####################################"
    print b
    

writeFile()
openFile()  
    

