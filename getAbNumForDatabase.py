#!/usr/bin/env python3
################################################################################
#
# Program:    getAbNumForDatabase.py
# Author:     Ziyi (Echo) Cui
# Version:    1.3 tested
# Date:       21/02/2017
#
# Function:
# ---------
# 1. Apply the Chothia numbering scheme to antibody sequences using web-services
#    access to abnum.
# 2. Get .seq file(a vertical list of numbered sequence) for each antibody.
# 3. Put all results(.seq files) into a specified folder.
# 
# Usage:
# ------
# sys.argv[1]  a .faa file of Database of antibody seuqences
# sys.argv[2]  the output Folder (with'/') for putting all the .seq files
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
# 07.11.16 Original version By: Ziyi (Echo) Cui
#
def UsageDie():
    print("""
    Version:   1.3
    Usage:
        sys.argv[1]  a .faa file of Database of antibody seuqences
        sys.argv[2]  he output Folder (with'/') for putting all the .seq files
    Function:
        1. Apply the Chothia numbering scheme to antibody sequences using
            web-services access to abnum.
        2. Get .seq file(a vertical list of numbered sequence) for each antibody.
        3. Put all results(.seq files) into a specified folder.
    Date:      21/02/2017""")
    sys.exit()

################################################################################
### Function 1
# ------------
# 1. Apply Chothia numbering schem to antibody sequences, resulting in a vertical 
#    list of [numbered position AAcode]
# e.g.
#     "H1 Q
#      L1 P"
# 2. Remove those lines with '-'
#
# 21.02.17 version 2.0 By: Ziyi (Echo) Cui
#
def applyNumbering(InputFileHandle,outputFolder):
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
                
                output = open(outputFolder+antibodyName+'.seq', 'w') 
                # output folder
                ### old version:
                #output = open('abnum/'+antibodyName+'.seq', 'w') # output folder
                output.write(abnum)
                output.close()
                abnum             = ''


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

################################################################################
### Main program
#
# 07/11/2016
# 
# Version 1.0  By Ziyi (Echo) Cui
#

# Check the command line for '-h' (help)
if sys.argv[-1] == "-h":
    UsageDie()

applyNumbering(sys.argv[1], sys.argv[2])

