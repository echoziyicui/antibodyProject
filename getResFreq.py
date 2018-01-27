#!/usr/bin/env python3
################################################################################
#
# Program:    getresfreq.py
# Author:     Ziyi (Echo) Cui
# Version:    1.1
# Date:       6/10/2016
#
# Function:
# ---------
# 1. Given a numbered sequence of antibody, transfer the amino acid code to 
#    one-letter form. 
# 2. By accessing to the web services, obtain the frequency of each residue in 
#    this sequence.
# 
# Usage:
# ------
# sys.argv[1]  a .seq file of numbered sequence for an antibody 
#
################################################################################
# import modules
from urllib import request
import sys
import time

################################################################################
# The dictionary for the conversion from three-letter code to one-letter code 
# for amino aicd.
threeOneConversion = dict(ALA='A', ARG='R', ASN='N', ASP='D', ASX='B', CYS='C', 
                          GLU='E', GLN='Q', GLX='Z', GLY='G', HIS='H', ILE='I',
                          LEU='L', LYS='K', MET='M', PHE='F', PRO='P', SER='S',
                          THR='T', TRP='W', TYR='Y', VAL='V')
url= "http://www.bioinf.org.uk/abysis/ws/resfreq.cgi"

################################################################################
# UsageDie()
# ----------
# provide general information about the whole process.
#
# 06/10/16 version 1.0 By Ziyi (Echo) Cui
#
def UsageDie():
    print("""
    version:   1.1
    Usage:     sys.argv[1]  a .seq file of numbered sequence for an antibody 
    Function:  Given a sequence of antibody, present the frequency of each 
               residue in this sequence
    Date:      06.10.2016""")
    sys.exit()

################################################################################
### Function 1
# ------------
# aa1 = throne(aa3oraa1)
#
# Transfer amino acid to uppercase and format them to one-letter code.
# Input can be a 3-letter or 1-letter name
#
# 06/10/16
#
# Version 1.0 By Ziyi (Echo) Cui
def throne(aa):
    aa = aa.upper()
    if len(aa) == 3:
        return threeOneConversion[aa]
    else:
        return(aa)

################################################################################
### Main program
#
# 06/10/16 
#
# Version 1.0 By Ziyi (Echo) Cui
#


# Check the command line for '-h' (help)
if sys.argv[-1] == "-h":
    UsageDie()

try:
    inputFileHandle = open(sys.argv[1], "r")
except:
    print("Unable to open file " + sys.argv[1])
    sys.exit()

for line in inputFileHandle.readlines():
    if line   == '\n':
        continue
    else:
        line       = line.rstrip()     # discard trailing whitespace
        fields     = line.split()      # split into fields delimited by spaces
        resnum     = fields[0]
        AminoAcid  = fields[1]
        AminoAcid  = throne(AminoAcid) # 3 letter -> 1 letter code

        # get access to the web services and obtain the frequency for this residue
        parameters = 'quiet=1&residue=' + resnum + '&aa=' + AminoAcid
        full_url   = url + "?" + parameters
        frequency  = request.urlopen(full_url).read()
        frequency  = str(frequency, encoding='utf-8')
        frequency  = frequency.rstrip()

        # print the result
        print(resnum + ' ' + frequency)
        time.sleep(1)

inputFileHandle.close()
