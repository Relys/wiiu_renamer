#wiiu_renamer.py
#By Relys
#January 5, 2016
#Renames game folders in specified directory from information stored in /meta/meta.xml

#!/usr/bin/python2

import sys, getopt, os, string, xml.etree.ElementTree

def main(argv):
   inputFolder= ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifolder="])
   except getopt.GetoptError:
      print 'test.py -i <inputFolder>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'test.py -i <inputFolder>'
         sys.exit()
      elif opt in ("-i", "--ifolder"):
         inputFolder = arg
   if inputFolder=='':
      print 'test.py -i <inputFolder>'
      sys.exe()
   print 'Input folder is "'+inputFolder+'"'
   for item in os.listdir(inputFolder):
      curFolder=os.path.join(inputFolder,item)
      curXML=os.path.join(curFolder,'meta/meta.xml')
      print('Looking at folder: '+curFolder)
      if os.path.isfile(curXML):
         print('Parsing XML file')
         e = xml.etree.ElementTree.parse(curXML).getroot()
         prodCode=e.find('product_code').text
         compCode=e.find('company_code').text
         name=e.find('longname_en').text.replace('\n', ' ').replace('\r', '').replace(':',' -').replace('BAYONETTA','Bayonetta').replace('THE LEGEND OF ZELDA','The Legend of Zelda -')
         newName=(name+' ['+prodCode[-4:]+compCode[-2:]+']')
         newFolder=os.path.join(inputFolder,newName)
         print('Renaming '+curFolder+' to '+newFolder)
         os.rename(curFolder,newFolder)
      else:
	     print 'Error '+curXML+' not found'

if __name__ == "__main__":
   main(sys.argv[1:])