#!/usr/bin/env python
# encoding: utf-8

import numpy
import xml.etree.ElementTree as ET
from PIL import Image
import pdb

from xml.etree.ElementTree import ElementTree,Element
import os
import pdb
import sys

def read_xml(img,filename,width1,height1,depth1):
    path = "xml/" + filename + ".xml"
    eleTree = ET.parse(path)
    root=eleTree.getroot()			
    print(root)
    src_img = img
    objects = eleTree.findall('object')
    count = 0
    try:
        for obj in objects:
    	    print obj.findall('bndbox')
	    xmin = int(obj.findall('bndbox')[0].findall('xmin')[0].text.strip())
            ymin = int(obj.findall('bndbox')[0].findall('ymin')[0].text)
            xmax = int(obj.findall('bndbox')[0].findall('xmax')[0].text)
            ymax = int(obj.findall('bndbox')[0].findall('ymax')[0].text)
            if xmin <= 0:
                obj.findall('bndbox')[0].findall('xmin')[0].text = "1"
            if ymin <= 0:
	        obj.findall('bndbox')[0].findall('ymin')[0].text = "1"
            if xmax >= width1:
                obj.findall('bndbox')[0].findall('xmax')[0].text = str(width1 - 1)
            if ymax >= height1:
                obj.findall('bndbox')[0].findall('ymax')[0].text = str(height1 - 1)    
	    print obj.findall('name')
	    #crop img
	    label_name = obj.findall('name')[0].text.lower()
	    print label_name
	    out_dir = "crop/"
	    brand_id = filename.split("_")[0]
	    str1 = "_"
	    filename_houzhui = str1.join(filename.split("_")[1:])
	    print "==================="
	    print filename_houzhui
	    save_img_name = out_dir + brand_id + "_" + label_name + "_" + filename_houzhui + "_" + str(count) + ".jpg"
	    ROI = src_img.crop((xmin,ymin,xmax,ymax))
	    ROI.save(save_img_name)
	    count += 1
    except:
        pass

    for child in root:
	print child       
    size = Element('size')
    width = Element('width')
    width.text = str(width1)
    height = Element('height')
    height.text = str(height1)
    depth = Element('depth')
    depth.text = str(depth1)
    root.append(size) 
    size.append(width)   
    size.append(height)
    size.append(depth)
    #eleTree.write("Out_Annotation/" + filename)
    #crop img
    

if __name__=="__main__":
    img_folder = "src"
    xml_list = "test.list"
    with open(xml_list, 'r') as f:
	for line in f:
            print line
            img_name = line.strip()[:-4]
 	    #print img_folder + img_name[:-4]+".jpg"
	    try:
                #img=Image.open(img_folder + "/" + img_name[:-4]+".jpg")
                img=Image.open(img_folder + "/" + img_name + ".jpg")
                width, height = img.size
	        read_xml(img,img_name, width,height,"3")
            except:
	        pass
