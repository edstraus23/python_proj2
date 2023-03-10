# Documenting Python Code with Doxygen (python_proj2)

This project demonstrates how to document code for a simple Python script by using Doxygen. Open the index.html file in the doxygen/html directory to view autogenerated documentation.

## About the Python Script

This Python script creates a DITA topic map and topics based on the contents of the xml input files. The following command line shows the help output:

```
$ python3 create_map.py -h

create_map.py -m <map> -i <inputdir> -o <outputdir>
```
Use a command line similar to the following to run the script:

```
$ python3 create_map.py -m media.ditamap -i ../tables -o ../media_out
Map name is " media.map "
Input directory is " ../tables "
Output directory is " ../media_out "

Creating media.map

Creating topic for movies.dita
Creating topic for tv_shows.dita
```
## Output

The script ouputs three files:
- media.ditamap
- movies.dita
- tv_shows.dita

## DITA OT Tool Kit

To generate a PDF file, you can copy the three files above to into your DITA OT directory and run the following commnd:

```
bin/dita --input=docsrc/samples/media.ditamap --format=pdf -Dnumbers-before-title=yes
```

This will generate a PDF file, but you can use other formats like "HTML". I like to use section numbering; hence, the "-Dnumbers-before-title=yes". But, you can leave this option out. For DITA OT documentation, see [DITA Open Toolkit](https://www.dita-ot.org/dev/).

## Documenting Code with Doxygen

One of the main objectives of this project was to show how to automatically document the Python code by using Doxygen. 
I will provide some examples in the following sections on how to enable doxygen to automatically document the code. For additional information on documenting the code by using Doxygen, refer to [Documenting Python Programs With Doxygen](https://www.woolseyworkshop.com/2020/06/25/documenting-python-programs-with-doxygen/).

### Install Doxygen

I am using Ubuntu for this demo. To install Doxygen for Ubuntu, follow the instructions from the following site:

[How to install Doxygen on Ubuntu](https://www.tutorialspoint.com/how-to-install-doxygen-on-ubuntu)

### Setting Up the Project Information

Add the following text to the main Python script (in this case, create_map.py):

``` Python
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
```

### Adding Information about Functions/Definitions

To add information about the functions/definitions and their parameters, use comments like in the following examples:

``` Python
def create_array(inputdir):
    """! This method creates an array of the file listings.
    @param inputdir   The input directory
    @return  An array of the file listings
    """
```

``` Python
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
```

### Creating the Configuration File (Doxyfile)

In a terminal, perform the following steps (starting at a level above the src directory):
```
$ mkdir doxygen
$ cd doxygen
$ doxygen -g
```
These actions create the configuration file (Doxyfile).

### Editing the Configruation File

Make the following updates to the Doxyfile.

Change the project name from:

```
PROJECT_NAME           = "My Project"
```

to

```
PROJECT_NAME           = "Documenting Python Code with Doxygen"
```

To use Javadoc style briefs (@brief) like shown above, change from:

```
JAVADOC_AUTOBRIEF      = NO
```

to

```
JAVADOC_AUTOBRIEF      = YES
```

To optimize the generated documentation for Java and Python based source code, change from:

```
OPTIMIZE_OUTPUT_JAVA   = NO
```

to

```
OPTIMIZE_OUTPUT_JAVA   = YES
```

To extract all elements found in the source code, change from:

```
EXTRACT_ALL            = NO
```

to

```
EXTRACT_ALL            = YES
```

To make the documentation for some pages appear cleaner, change from:

```
HIDE_SCOPE_NAMES       = NO
```

to

```
HIDE_SCOPE_NAMES       = YES
```

To sort the elements in alphabetical order, change from:

```
SORT_BRIEF_DOCS        = NO
```

to

```
SORT_BRIEF_DOCS        = YES
```

To inform Doxygen where to find the Python source code, change from

```
INPUT                  =
```

to

```
INPUT                  = ../src
```

To disable the Latex generation, change from:

```
GENERATE_LATEX         = YES
```

to

```
GENERATE_LATEX         = NO
```

Save your updated Doxyfile configuration file when you have completed your updates.

### Running Doxygen

From within the doxygen directory, run:

```
doxygen
```

This will display the tasks that it performs and any warnings or errors that occur during its execution. When complete, you should see an html directory that contains the autogenerated HTML documentation.

### Viewing the Documentation

Open **index.html** file in the **doxygen/html** directory to view the defintions for the functions of the create_map.py script.
