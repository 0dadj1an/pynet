

'''
create list and write elements into yaml and json files
read those files and print them
'''
import json
import yaml
from pprint import pprint as tisk




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
    
    
    print "Yaml list is:\n {}".format(a)
    print""
    print "Yaml pprint format is:\n"
    tisk(a)
    print""
    print "Json list is:\n {}".format(b)
    print""
    print "Json pprint format is:\n"
    tisk(b)
    
def main():
    writeFile()
    openFile()  


if __name__ == '__main__':
   main()

