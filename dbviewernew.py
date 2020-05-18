#!/usr/bin/python
import string
import json
import os
import subprocess
import uuid
import time

epoch = int(time.time())

size=(2*1073741824) #2 GB
id1 = str(uuid.uuid4())
cmd1 = "head -c %d < /dev/urandom > /home/roche/%s.xml"%(size,id1)
id2 = str(uuid.uuid4())
cmd2 = "head -c %d < /dev/urandom > /home/roche/%s.xml"%(size,id2)

id3 = str(uuid.uuid4())
cmd3 = "head -c %d < /dev/urandom > /home/roche/%s.xml"%(size,id3)


s1 = 'INSERT INTO gws_contentInventory (systemClass, RUDI,contentId, originalName,modifiedName,contentPath,contentPackagePath,interface,category,priority,status,transformStatus,originalSize,modifiedSize,arrivalTime) VALUES ("c800DM","GTIN^94915630938469^CZ9002N01","%s","","","/home/roche//%s.xml","",4,1,1,1,0,%d,0,%d)'%(id1,id1,size,epoch)

s2 = 'INSERT INTO gws_contentInventory (systemClass, RUDI,contentId, originalName,modifiedName,contentPath,contentPackagePath,interface,category,priority,status,transformStatus,originalSize,modifiedSize,arrivalTime) VALUES ("c800DM","GTIN^94915630938469^CZ9002N01","%s","","","/home/roche/%s.xml","",4,1,1,1,0,%d,0,%d)'%(id2,id2,size,epoch)

s3 = 'INSERT INTO gws_contentInventory (systemClass, RUDI,contentId, originalName,modifiedName,contentPath,contentPackagePath,interface,category,priority,status,transformStatus,originalSize,modifiedSize,arrivalTime) VALUES ("c800DM","GTIN^94915630938469^CZ9002N01","%s","","","/home/roche/%s.xml","",4,1,1,1,0,%d,0,%d)'%(id3,id3,size,epoch)

#print "Run below commands to create %.2f MB files:\n%s\n%s\n%s"%(size/(1024*1024),cmd1,cmd2,cmd3)
print "============================================================="
print "\n\tGo to mysql prompt using <mysql -uroot -prochediag2018 gws> and run below queries:\n"
#print("ALTER TABLE gws_contentInventory MODIFY COLUMN originalSize bigint;")
print "\n %s;"%(s1)
print "\n %s;"%(s2)
print "\n %s;"%(s3)