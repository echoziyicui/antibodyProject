#!/usr/bin/env python3
################################################################################
#
# Program: getAbNumForOne.py
# Author:  Ziyi (Echo) Cui
# Version: 1.2.1 tested  
#          Adapted from 'getAbNumForDatabase.py' for automated process for
#          one antibody
# Date:    12/01/2017
#
# Function:
# ---------
# 1. Apply the Chothia numbering scheme to sequences of just one antibody using 
#    web-services access to abnum.
# 2. Print the result(a vertical list of numbered sequence) on the screen.
# 
# Usage:
# ------
# sys.argv[1]  a .faa file for sequences of just one antibody
################################################################################
# import modules
from urllib import request
import sys
import time
import re

################################################################################
# UsageDie()
# ----------
# provide general information about the whole process.
#
# 07.11.16 Original version By: Echo
def UsageDie():
    print("""
    version: 1.2.1 
             Adapted from 'getAbNumForDatabase.py' for automated process for 
             one antibody
    Usage:   sys.argv[1]   a .faa file for sequences of just one antibody
    Function: 
         1. apply the Chothia numbering scheme to sequences of just one antibody 
            using web-services access to abnum
         2. print the result(a vertical list of numbered sequence) on the screen
    Date:      12.01.2017""")
    sys.exit()

################################################################################
### Function 1
# ------------
# abnum = applyNumbering(mab.faa)
#
# 1. Apply Chothia numbering schem to antibody sequences, resulting in a vertical
# list of  [numbered position AAcode]
# e.g.
#     "H1 Q
#      L1 P"
# 2. Remove those lines with '-'
#
# 07.11.16 version 1.0 By: Ziyi (Echo) Cui
#
def applyNumbering(InputFileHandle):
    try:
        seqWithoutNumbering = open(InputFileHandle, 'r')
    except:
        print("Unable to open file " + InputFileHandle)
        sys.exit()

    url                           = "http://www.bioinf.org.uk/cgi-bin/abnum/abnum.pl?plain=1"
    isReadingSequence             = False
    antibodyName                  = ''
    abnum                         = ''
    sequence                      = ''
    antibodyNameSet               = []

    for line in seqWithoutNumbering.readlines():

        if (line[0] == '>' or line[0] == '\n') and isReadingSequence:
            isReadingSequence = False

            sequence              = sequence.replace('\t', '').replace('\n', '').replace(' ', '')
            # remove \t, \n, ' ' from the sequence
            parameters            = "&aaseq=" + sequence +"&scheme=-c"
            full_url              = url + parameters
            numberedSeq           = request.urlopen(full_url).read()
            numberedSeq           = str(numberedSeq, encoding='utf-8').rstrip()
            numberedSeq           = re.sub(r'[A-Z][0-9]*\s[-]\s*', '', numberedSeq)  
            # remove lines with '-'
            numberedSeq           = numberedSeq + '\n'
            abnum                += numberedSeq
            sequence              = ''
            time.sleep(1)

            if line[0]           == '\n':
                if antibodyName not in antibodyNameSet:
                    antibodyNameSet.append(antibodyName)
                else:
                    antibodyName  = antibodyName + '2'

                #old version output = open('abnum/'+antibodyName+'.seq', 'w')
                #OUTPUT = OPEN(antibodyName+'.seq', 'w')
                #output.write(abnum)
                #output.close()
                #abnum             = ''
                

        if isReadingSequence:
            sequence             += line

        if line[0]               == '>':
            if '- no sequence' in line:
                isReadingSequence = False
                continue
            else:
                isReadingSequence = True
                line              = line.replace('>', '').rstrip()
                field             = line.split('|')
                antibodyName      = field[0]


    seqWithoutNumbering.close()
    return abnum

################################################################################
### Main program
#
# 07/11/16
#
# Version 1.0 By Ziyi (Echo) Cui
#

# Check the command line for '-h' (help)
if sys.argv[-1] == "-h":
    UsageDie()

numberedSeq      = applyNumbering(sys.argv[1])
print(numberedSeq)
