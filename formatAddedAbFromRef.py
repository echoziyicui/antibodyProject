#!/usr/bin/env python3
################################################################################
#
# Program:    formatAddedAbFromRef.py
# Author:     Ziyi (Echo) Cui
# Version:    1.2
# Date:       15/03/2017
#
# Function:
# ---------
# format newly added data from reference to the unified form in our database
# 
# Usage:
# ------
# sys.argv[1]  a file of names of antibodies with no sequence in reference
# sys.argv[2]  an unformatted file of antibodies and sequences 
################################################################################
# import modules 
import sys
import re
################################################################################
# UsageDie()
# ----------
# provide general information about the whole program
#
# 15/03/2017 version 1.0 By: Ziyi (Echo) Cui
#
def UsageDie():
    print("""
    Version:    1.2
    Usage: 
    sys.argv[1] a file of names of antibodies with no sequence in reference
    sys.argv[2] an unformatted file of antibodies and sequences     
    Function:   Format newly added data from reference to the unified form in 
                our database.
    Date:       15/03/2017""")
    sys.exit()
################################################################################
### Function 1
# ------------
# format antibody with no seq to the format:
# >pertuzumab - no sequence
# 
# 23/11/2016
#
# Version 1.0 By Ziyi (Echo) Cui
#
def addnosequence(InputFileHandle):

    antibodyData    = open(InputFileHandle, 'r')

    for line in antibodyData.readlines():
        if line[0] != '\n':
            line    = line.rstrip()
            line    = '>'+ line + ' - no sequence' + '\n\n'
            print(line)
################################################################################
### Function 2
# ------------
# format antibody with sequence to the format:
# >gantenerumab|Heavy
# sequence
# >gantenerumab|Light
# sequence 
#
# 23/11/2016
#
# Version 1.0 By Ziyi (Echo) Cui
#
def formatsequence(InputFileHandle):

    antibodyData = open(InputFileHandle, 'r')
    newdata = ''
    lines = antibodyData.readlines()
    for line in lines:
        if '|' in line:
            field = line.split('|')
            field[0] = field[0].lower()
            line = '>' + field[0] + '|' + field[1]
            newdata += line
        elif line[0] == '\n':
            newdata += line
        else:
            line =line.replace(' ','')
            line =line.replace('\t','')
            line = re.sub("[0-9]", "", line)
            newdata += line
    print(newdata)
################################################################################
### main program
#
# 06.10.16 Original version By: Echo
#

# Check the command line for '-h' (help)
if sys.argv[-1] == "-h":
    UsageDie()

addnosequence(sys.argv[1])
formatsequence(sys.argv[2])

