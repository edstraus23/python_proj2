#!/usr/bin/python

"""! @brief Python program that generates DITA topicmap and topics."""
##
# @mainpage DITA Topicmap Creation Project
#
# @section description_main Description
# This Python program generates DITA topicmap and topics from an xml file
# or from media class files.
#
# @section notes_main Notes
# - This project also demonstrates how to use Doxygen comments for
# generating source code documentation with Doxygen.
#
# Copyright (c) 2023 Eric Strausbaugh.  All rights reserved.
##
# @file create_map.py
#
# @brief Creates DITA topicmap and topics from an xml or from media class files.
#
# @section description_doxygen_example Description
# Example Python program with Doxygen style comments.
#

#
# @section notes_doxygen_example Notes
# - Comments are Doxygen compatible.
#
# @section todo_doxygen_example TODO
# - None.
#
# @section author_doxygen_example Author(s)
# - Created by Eric Strausbaugh on 03/03/2023.
#
# Copyright (c) 2023 Eric Strausbaugh.  All rights reserved.
# Imports
import sys, getopt, os, csv, re
from lxml import etree
from io import StringIO, BytesIO
import xml.etree.ElementTree as ET
import codecs
import map_mods
#farr=[]

def main(argv):
   """! This main method calls all of the subroutines from the maps_mod module. 
        @param argv  -h | -m <map> -i <inputdir> -o <outputdir>; Use -h option to see available arguments.
        
   """
   ## Map name.
   map_name = ''
   ## Input directory.
   inputdir = ''
   ## Output directory.
   outputdir = ''
   

   try:
      opts, args = getopt.getopt(argv,"hm:i:o:",["mfile=","ifile=","ofile="])
   except getopt.GetoptError:
      print('create_map.py -m <map> -i <inputdir> -o <outputdir>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('create_map.py -m <map> -i <inputdir> -o <outputdir>')
         sys.exit()
      elif opt in ("-m", "--map"):
         map_name = arg
      elif opt in ("-i", "--idir"):
         inputdir = arg
      elif opt in ("-o", "--odir"):
         outputdir = arg
   print('Map name is "', map_name, '"')
   print('Input directory is "', inputdir, '"')
   print('Output directory is "', outputdir, '"')
   #replace_files(inputdir,outputdir)
   farr=map_mods.create_array(inputdir)
   farr.sort()
   map_mods.create_mapfile(map_name,inputdir,outputdir,farr)
   map_mods.create_topics(map_name,inputdir,outputdir,farr)

if __name__ == "__main__":
   main(sys.argv[1:])

