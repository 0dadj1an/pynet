'''
reads the config file, prints parent CRYPTO map and for every map also all childern- exercise no.8
also prints pfs group2 only crypto maps - exercise no.9
also prints just cryptomap without AES enc

'''




import re
from ciscoconfparse import CiscoConfParse

parse = CiscoConfParse("/home/hrb/github/pynet/ciscoconfparse/config.txt")
objects = parse.find_objects("^crypto map CRYPTO")
objects2 = parse.find_objects_wo_child(parentspec=r"crypto map CRYPTO", childspec=r"AES")



def findParentAndChildern():
    for obj in objects:
       print "Parent is:"
       print obj.text
       print""
       parent = objects[objects.index(obj)]
       list_a= parent.children
       print "Childerns are:"
       for child in list_a:
           print child.text
           print""
    

    

def findPFSgroup2():
    print "#################"
    print "CRYPTO maps with PFSgroup2 are:\n"
    for obj in objects:
       if obj.re_search_children(r"set pfs group2"):
           print obj.text 
           print""
            
           
    

def findNOTAES():
    print "#################"
    print "CRYPTO maps with NO AES:\n"
    for obj in objects2:
        for child in obj.children:
            if 'transform' in child.text:
                pattern = re.search(r"set transform-set (.*)$", child.text)
                transform_set = pattern.group(1)
        print "{0} and transform set is: {1}".format(obj.text, transform_set)
    

def main():
    findParentAndChildern()
    findPFSgroup2()
    findNOTAES()

if __name__ == '__main__':
   main()


    



    
