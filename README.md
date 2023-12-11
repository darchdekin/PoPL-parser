# PoPL-parser

## Project info

Python Parser Project for CS4450, created by "Parser? I barely know 'er"
Group Members: Dee Archdekin, Mel Tully, Zoe Spriggs, David Douglas.
The goal of this project is to create a parser for the Python language, using Antlr

Please note that all group members have contributed to creating and refining the grammar, 
we have been collaborating online and in-person.

## Environment & Necessary Software

Any environment can be used, but Antlr. AntlrDenter, and Python3 install is required  

Python can be installed here: https://www.python.org/downloads/  

Antlr can be installed here: https://www.antlr.org/download.html  

Note when installing Antlr that this project uses the Python version of Antlr.  

This project also makes use of AntlrDenter. Further information on AntlrDenter can be found here: https://github.com/yshavit/antlr-denter  

**You can install AntlrDenter using 'pip install antlr-denter'**

## How to run the parser

After installing python, you must run the following command to build the program:
'antlr4 -v 4.13.0 -Dlanguage=Python3 P1.g4'

This will generate the necessary files in order to run the driver program, driver.py. This can be done by running the command: 
'python3 driver.py file_to_parse.txt'

This driver creates the parse tree in string format, but the a .png generated from a DOT file with Graphvis has also been provided (see parse_tree_final.png)

**Note that there is a unique branch for deliverable1 and deliverable2. Deliverable 3 is on branch Main.**
