"""! @brief Contains the map modules."""
##
# @file map_mods.py
#
# @brief Contains the map modules.
#
# @section description_map Description
# Contains the map modules.
#
# Copyright (c) 2023 Eric Strausbaugh.  All rights reserved.
# Imports
import sys, getopt, os, csv, re
from lxml import etree
from io import StringIO, BytesIO
import xml.etree.ElementTree as ET
import codecs

def create_array(inputdir):
    """! This method creates an array of the file listings.
    @param inputdir   The input directory
    @return  An array of the file listings
    """
    farr=[]
    Path = os.getcwd() + "/" + inputdir
    filelist = os.listdir(Path)
    for x in filelist:
        #print("DDDD" + x + "\n")
        if x.endswith(".xml"):
            z = x.split(".")
            farr.append(z[0])
            #print("DDDD Adding to array:", z[0] )
            #print "LLL", Path
    return farr        

def create_mapfile(mapname,inputdir,outputdir,farr):
    """! This method creates a DITA topic map.
    @param mapname   The map name
    @param inputdir  The input directory
    @param outputdir  The output directory
    @param farr  The array of files
    """
    Path = os.getcwd() + "\\" + inputdir
    Pathout = os.getcwd() + "/" + outputdir
    #filelist = os.listdir(Path)
    
    print("\nCreating " + mapname + "\n")

    mapout = Pathout + "/" + mapname
    mout = open(mapout, "w")
    prev_m_fname=""
    fcount = 0
    mapname_wop = mapname.replace('.ditamap', "")

    mout.write("<?xml version='1.0' encoding='UTF-8'?>\n")
    mout.write('<!DOCTYPE map PUBLIC "-//OASIS//DTD DITA Map//EN" "map.dtd">\n')
    mout.write('<map id="map_id_' + mapname_wop + '" title="' + mapname_wop + ' Map">\n')


    for y in farr:
        #print("LLL" + y)
        mout.write('    <topicref href="' + y + '.dita" />\n')

    mout.write('</map>')

def create_topics(mapname,inputdir,outputdir,farr):
    """! This method creates DITA topics with tables.
    @param mapname   The map name
    @param inputdir  The input directory
    @param outputdir  The output directory
    @param farr  The array of files
    """
    Path = os.getcwd() + "/" + inputdir
    Pathout = os.getcwd() + "/" + outputdir

    for x in farr:

        #print("ZZZ" + x)
        print('Creating topic for ' + x + '.dita')
        #file = Path + "/" + x + ".xml"
        #f = open(file, "r")
        fileout = Pathout + "/" + x + ".dita"
        fout = open(fileout, "w")

        fout.write('<?xml version="1.0" encoding="utf-8"?>\n')
        fout.write('<!DOCTYPE topic PUBLIC "-//OASIS//DTD DITA Topic//EN" "topic.dtd">\n')
        fout.write('<topic id="' + x + '" xml:lang="en-us">\n')
        fout.write('<title>' + x + '</title>\n')
        fout.write('<table frame="all" rowheader="firstcol">\n')
        fout.write('<title>' + x + '</title>\n')
        fout.write('<tgroup cols="3">')
        fout.write('<colspec colname="c1"/>\n<colspec colname="c2"/>\n<colspec colname="c3"/>\n')
        fout.write('<thead>\n')
        fout.write('  <row>\n')
        fout.write('    <entry>Title</entry>\n')
        fout.write('    <entry>Year Start</entry>\n')
        fout.write('    <entry>Year End</entry>\n')
        fout.write('  </row>\n')
        fout.write('</thead>\n')
        fout.write('<tbody>')
      

        target_file = codecs.open(Path + "/" + x + ".xml", mode='r',encoding='utf-8', errors="ignore")
        tree = ET.parse(target_file)
        root = tree.getroot()
        flag = 0 # to only show first occurence - 6/21/22

        for btopic in root.iter():
            
            if btopic.tag == "media":
                #print("   type: media")
                s_btopic_id = btopic.get('id')
                #print("   id: " + s_btopic_id)
                
            if btopic.tag == "title":
                tag = "title"
                s_btopic = btopic.text
                #print("   title: " + s_btopic)
                fout.write('\n<row>\n  <entry>' + s_btopic + '</entry>\n')


            if btopic.tag == "year_start":
                tag = "year_start"
                s_btopic = btopic.text
                #print("   year_start: " + s_btopic)
                fout.write('  <entry>' + s_btopic + '</entry>\n')

            if btopic.tag == "year_end":
                tag = "year_end"
                s_btopic = btopic.text
                #print("   year_end: " + s_btopic)
                fout.write('  <entry>' + s_btopic + '</entry>\n</row>\n')

        fout.write('</tbody>\n')
        fout.write('</tgroup>\n')
        fout.write('</table>\n')
        fout.write('</topic>')





