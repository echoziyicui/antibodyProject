#!/usr/bin/env python3
################################################################################
#
# Program: summarizeDatabase.py
# Author:  Ziyi (Echo)Cui
# Version: 1.2.1
# Date:    16/01/2017
#
# Function:
# ---------
# Summarize the number and list of antibodies refering to the database obtained
# and the  reference list.
#
# Usage:
# ------
# summarizeDatabase.py + obtainedDataset.faa + referencelist.faa
# sys.argv[1]    database file
# sys.argv[2]    a file with all the antibody names in reference list 
################################################################################
import sys
################################################################################
# UsageDie()
# ----------
# provide general information about the whole process.
#
# 16.01.17 version 1.0 By: Echo


def UsageDie():
    print("""
    version:   1.2.1
    Usage:     summarizeDatabase.py + obtainedDataset.faa + referencelist.faa
    sys.argv[1]    database file 
    sys.argv[2]    a file with all the antibody names in reference list 
    Function:  Summarize the number and list of antibodies refering to the 
               database obtained and the  reference list.
    Date:      16/01/2017""")
    sys.exit()

################################################################################
### Function 1
# obtainedAbWithSeq,obtainedAbNoSeq,presentWithSeq,absent,notInRef = 
# testAppearance(tested, dataset)
# ----------------------------------------
# Test whether antibody in tested is already in dataset and sort them to
#  different list.
#
# 21/112016 version 1.0 By Ziyi (Echo) Cui
#
def testAppearance(tested, dataset):
    try:
        absObtained              = open(tested, 'r')
        absRef                   = open(dataset, 'r')
    except:
        print("Unable to open file ")
        sys.exit()

    obtainedAbNoSeq              = []
    obtainedAbWithSeq            = []

    presentWithSeq               = []
    presentWithoutSeq            = []
    absent                       = []

    notInRef                     =[]

    for line in absObtained.readlines():
        if line[0]              == '>':
            if 'no sequence' in line:
                line             = line.replace('>', '').rstrip()
                field            = line.split(' - ')
                antibodyName     = field[0]
                obtainedAbNoSeq.append(antibodyName)
            else:
                line             = line.replace('>', '').rstrip()
                field            = line.split('|')
                antibodyName     = field[0]
                if antibodyName not in obtainedAbWithSeq:
                    obtainedAbWithSeq.append(antibodyName)
  
    for line in absRef.readlines():
        antibodyName             = line.replace('\n','').rstrip()

        if antibodyName in obtainedAbWithSeq:
            presentWithSeq.append(antibodyName)
        elif antibodyName in obtainedAbNoSeq:
            presentWithoutSeq.append(antibodyName)
        else:
            absent.append(antibodyName)

    for antibodyName in obtainedAbWithSeq:
        if antibodyName not in presentWithSeq:
            if antibodyName not in notInRef:
                notInRef.append(antibodyName)

    absRef.close()
    absObtained.close()
    return  obtainedAbWithSeq,obtainedAbNoSeq,presentWithSeq,absent,notInRef

################################################################################
### Main program
#
# 12/01/2017 
#
# Version 1.0 By Ziyi (Echo) Cui
#
if sys.argv [-1] == "-h":
    UsageDie()

getobtainedAbWithSeq,getobtainedAbNoSeq,presentWithSeq,getabsent,getnotInRef = testAppearance(sys.argv[1],sys.argv[2])
#print(len(presentWithSeq),presentWithSeq)
print('obtainedAb+', len(getobtainedAbWithSeq),getobtainedAbWithSeq,'\n\n','obtainedAb-',len(getobtainedAbNoSeq),getobtainedAbNoSeq,'\n\n','absentfromRef',len(getabsent),getabsent,'\n\n','outOfRef',len(getnotInRef),getnotInRef)
