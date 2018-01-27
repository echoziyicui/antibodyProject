#!/usr/bin/env python3
################################################################################
#
# Program: testappearance.py
# Author:  Ziyi Cui
# Version: 1.2
# Date:    23/11/2016
#
# Function:
# ---------
# 1. Test whether antibody in tested file is already in dataset file.
# 2. Summarize the newly added info according to the sequence appearance.
#
# Usage:
# ------
# testappearance.py + allmabs.faa + integratedData.faa + newlyaddedab.faa
#  -> groups sorting antibodies
# sys.argv[1]    a file containing all the mab names 
# sys.argv[2]    the integrated database file 
# sys.argv[3]    a file of data that added from reference 
################################################################################
import sys
################################################################################
# UsageDie()
# ----------
# provide general information about the whole program
#
# 23/11/2016 version 1.0 By Ziyi (Echo) Cui
#
def UsageDie():
    print("""
    Version:    1.2
    Usage:      testappearance.py + allmabs.faa + integratedData.faa + 
                newlyaddedab.faa -> groups sorting antibodies
    sys.argv[1]    a file containing all the mab names 
    sys.argv[2]    the integrated database file 
    sys.argv[3]    a file of data that added from reference 
    Function:     
    1. Test whether antibody in tested file is already in dataset file.
    2. Summarize the newly added info according to the sequence appearance.

    Date:      """)
    sys.exit()

################################################################################
### Function 1
# testOpen()
# ---------
# test whether the file can be opened
#
# 03/11/2016
#
# Version 1.1 By Ziyi (Echo) Cui
#
def testOpen(filepath):
    try:
        f = open(filepath, "r")
        f.close()
    except:
        print("Unable to open file " + filepath)
        sys.exit()

################################################################################
### Function 2
# groups = testAppearance(tested, dataset)
# ----------------------------------------
# Test whether antibody in tested is already in dataset and sort them to 
# different list.
#
# 21/11/2016
#
# Version 1.0 By Ziyi (Echo) Cui
#
def testAppearance(tested, dataset):
    try:
        allmabs             = open(tested, 'r')
        mabsObtained        = open(dataset, 'r')
    except:
        print("Unable to open file ")
        sys.exit()

    setAbNoSeq              = []
    setAbWithSeq            = []

    presentWithSeq          = []
    presentWithoutSeq       = []
    absent                  = []

    for line in mabsObtained.readlines():
        if line[0]          == '>':
            if 'no sequence' in line:
                line         = line.replace('>', '').rstrip()
                field        = line.split(' - ')
                antibodyName = field[0]
                setAbNoSeq.append(antibodyName)
            else:
                line         = line.replace('>', '').rstrip()
                field        = line.split('|')
                antibodyName = field[0]
                if antibodyName not in setAbWithSeq:
                    setAbWithSeq.append(antibodyName)

    for line in allmabs.readlines():
        antibodyName         = line.replace('\n','').rstrip()

        if antibodyName in setAbWithSeq:
            presentWithSeq.append(antibodyName)
        elif antibodyName in setAbNoSeq:
            presentWithoutSeq.append(antibodyName)
        else:
            absent.append(antibodyName)


    allmabs.close()
    mabsObtained.close()
    return len(presentWithSeq), presentWithSeq, len(presentWithoutSeq), presentWithoutSeq, len(absent), absent
################################################################################
### Function 3
# abWithSeq, abNoSeq = classifyab(InputFileHandle)
# -----------------------------------------------
# sort the newly added antibody according to whether they have sequence.
#
# 23/11/2016
#
# Version 1.0 By Ziyi (Echo) Cui
#
def classifyab(InputFileHandle):

    antibodyData            = open(InputFileHandle, "r")
    abNoSeq                 = []
    abWithSeq               = []

    for line in antibodyData.readlines():
        if line[0]          == ">":
            antibodyKey      = line.replace('>', '').rstrip()
            #seqDict.setdefault(antibodyKey, '')
            #print(antibodyKey)
        if line[0]          == ">":
            if '- no sequence' in antibodyKey:
                field        = antibodyKey.split(' - ')
                antibodyName = field[0]
                abNoSeq.append(antibodyName)
            else:
                field        = antibodyKey.split('|')
                antibodyName = field[0]
                if antibodyName not in abWithSeq:
                    abWithSeq.append(antibodyName)

    antibodyData.close()
    return len(abWithSeq), abWithSeq,len(abNoSeq), abNoSeq
################################################################################
### Function 4
# groups = testAppearance(tested, dataset)
# ---------------------------------------
# Compare two sets of data accounting to there sequence appearance.
#
# 23/11/2016
#
# Version 1.0 By:(Echo) Ziyi Cui
#
def checkresult(newseqlist,newnoseqlist,seqlist,absentlist,noseqlist):
    repeatedadd        = []
    seqreplaceabsent   = []
    seqreplacenoseq    = []
    noseqreplaceabsent = []
    stillabsent        = []

    for antibody in newseqlist:
        if antibody in seqlist:
           if antibody not in repeatedadd:
               repeatedadd.append(antibody)
        elif antibody in absentlist:
           if antibody not in seqreplaceabsent:
               seqreplaceabsent.append(antibody)
        elif antibody in noseqlist:
           if antibody not in seqreplacenoseq:
               seqreplacenoseq.append(antibody)

    for antibody in newnoseqlist:
        if antibody in absentlist:
            if antibody not in noseqreplaceabsent:
                noseqreplaceabsent.append(antibody)

    for antibody in absentlist:
        if (antibody not in newseqlist) and(antibody not in newnoseqlist) and (antibody not in stillabsent):
            stillabsent.append(antibody)

    return len(repeatedadd),len(seqreplaceabsent),len(seqreplacenoseq),len(noseqreplaceabsent),len(stillabsent)
                   
################################################################################
### Main program
#
# 23/11/2016 
#
# Version 1.1 By Ziyi (Echo) Cui
#

# Check the command line for '-h' (help)
if sys.argv[-1] == "-h":
    UsageDie()

NumofwithSeq,listwithSeq, NumofNoSeq,listNoSeq,NumofAbsent,listAbsent = testAppearance(sys.argv[1], sys.argv[2])
print('Number of ab in dataset with sequence', NumofwithSeq, '\n\n')
print('Number of ab in dataset with no sequence', NumofNoSeq, '\n\n')
print('Number of ab absent', NumofAbsent, '\n\n')

NumofnewlyaddedSeq,newlyAddedSeq,NumofnewlyaddedNoSeq,newlyAddedNoSeq = classifyab(sys.argv[3])

print('Number of newly added ab with sequence',NumofnewlyaddedSeq,'\n', 'Number of newly added ab with no sequence',NumofnewlyaddedNoSeq, '\n\n')

