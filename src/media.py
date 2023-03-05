"""! @brief Defines the Media classes."""
##
# @file media.py
#
# @brief Defines the media classes.
#
# @section description_media Description
# Defines the media classes for various media.
#
#
# @section author_media Author(s)
# - Created by Eric Strausbaugh on 03/04/2023.
#
# Copyright (c) 2023 Eric Strausbaugh.  All rights reserved.
import random
class Media:
    """! The Media class.
    Defines the title, year start, and year end for the Media class. Media can be movies, TV shows, books, etc.
    """
    def __init__(self, title, year_start, year_end):
        """! The Media class initializer.
        @param title  Media title.
        @param year_start  Media start date.
        @param year_end  Media end date.

        @return  An instance of the Media class initialized.
        """
        ## The title of the Media.
        self.title = title
        ## The year start of the Media.
        self.year_start = year_start
        ## The year end of the Media.
        self.year_end = year_end

m1 = Media("Old School", "2001", "2001")

print(m1.title)
print(m1.year_start)
print(m1.year_end)

