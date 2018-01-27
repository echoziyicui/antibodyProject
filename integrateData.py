#!/usr/bin/env python3
################################################################################
#
# Program:    integrateData.py
# Author:     Ziyi (Echo) Cui
# Version:    1.8
# Date:       3/11/2016
#
# Function:
# ---------
# 1. Replenish RL.faa and PL.faa with their corresponding manually converted 
#    sequences.
# 2. Integrate antibody sequence data from Proposed list(PL.faa and PL115
#    imagedSeq.faa) and Recommended list(RL.faa and RLimagedSeq.faa).
#
# Usage:
# ------
# sys.argv[1]  RL.faa, data from all RL lists 
# sys.argv[2]  PL.faa, data from all PL lists
# sys.argv[3]  RLPngSeq, data from RL lists converted from images 
# sys.argv[4]  PLPngSeq, data from PL lists converted from images 
#
################################################################################
# import
import sys

################################################################################
# constant
################################################################################
# UsageDie()
# ----------
# provide general information about the whole process.
#
# 02/11/16 version 1.1 By Ziyi (Echo) Cui
#
def UsageDie():
    print("""
    version:   1.8
    Usage:  
        sys.argv[1]  RL.faa, data from all RL lists 
        sys.argv[2]  PL.faa, data from all PL lists
        sys.argv[3]  RLPngSeq, data from RL lists converted from images 
        sys.argv[4]  PLPngSeq, data from PL lists converted from images 
    Function: 
        1. Replenish RL.faa and PL.faa with their corresponding manually 
           converted sequences.
        2. Integrate antibody sequence data from Proposed list(PL.faa and PL115
           imagedSeq.faa) and Recommended list(RL.faa and RLimagedSeq.faa).
    Date:      26/10/2016""")
    sys.exit()

################################################################################
### testOpen()
# ------------
# test whether the file can be opened
#
# 03/11/16 version 1.1 By Ziyi (Echo) Cui
#
def testOpen(filepath):
    try:
        f = open(filepath, "r")
        f.close()
    except:
        print("Unable to open file " + filepath)
        sys.exit()

################################################################################
### Function 1
#------------
# add_key(sys.arfv[1]) --> RseqDict = {antibodyName | Heavy/light :[]}
# add_key(sys.arfv[2]) --> RseqDict = {antibodyName | Heavy/light :[]}
# --------------------------------------------------------------------
# extract antibodyName and chain type as the key of a new dict
#
# 03/11/2016
#
# Version 1.3 By Ziyi (Echo) Cui
#
def add_key(InputFileHandle):

    antibodyData = open(InputFileHandle, "r")
    abNoSeq      = []
    abWithSeq    = []
    seqDict      = {}

    for line in antibodyData.readlines():

        if line[0] == ">":
            antibodyKey = line.replace('>', '').rstrip()
            seqDict.setdefault(antibodyKey, '')
            #print(antibodyKey)

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
    return seqDict, abWithSeq, abNoSeq

################################################################################
### Function 2
# ------------
# dictwithseq = add_seq(database, Dict only with key)
# add_seq(sys.argv[1]) -->RseqDict = {antibodyName | Heavy/light :[sequence]}
# add_seq(sys.argv[2]) -->PseqDict = {antibodyName | Heavy/light :[sequence]}
# ---------------------------------------------------------------------------
# add the corresponding sequence of each antibody.
#
# 03/11/2016
#
# Version 1.3 By Ziyi (Echo) Cui
#
def add_seq(InputFileHandle, DictwithabName):

    antibodyData      = open(InputFileHandle, 'r')
    isReadingSequence = False
    antibodyKey       = ''
    sequence          = ''

    for line in antibodyData.readlines():

        if (line[0] == '>' or line[0] == '\n') and isReadingSequence:
            isReadingSequence = False

            DictwithabName[antibodyKey] = sequence
            #print("test1",DictwithabName)
            sequence = ''

        if isReadingSequence:
            sequence += line

        if line[0] == '>':
            if '- no sequence' in line:
                isReadingSequence = False
                continue
            else:
                isReadingSequence = True
                antibodyKey = line.replace('>', '').rstrip()
    
    dictwithseq = DictwithabName
    #print("test", dictwithseq)
    antibodyData.close()
    return dictwithseq

################################################################################
### Function 3
# ------------
# add_imagedSeq(sys.argv[3]) --> RseqDict += RLimagedSeq
# add_imagedSeq(sys.argv[4]) --> PseqDict += PL115imagedSeq
# --------------------------------------------------------
# add those sequences that manually converted from the images to each dict for RL
# and PL
#
# 03/11/2016
#
# Version 1.4 By Ziyi (Echo) Cui
#
def add_imagedSeq(InputFileHandle, seqDict, abWithSeq, abNoSeq):

    imagedSeq         = open(InputFileHandle, 'r')
    isReadingSequence = False
    i_sequence        = ''

    for line in imagedSeq.readlines():

        if (line[0] == '>' or line[0] == '\n') and isReadingSequence:
            isReadingSequence = False
            field             = antibodyKey.split('|')
            antibodyName      = field[0]


            seqDict.setdefault(antibodyKey, '')
            seqDict[antibodyKey] = i_sequence

            if (antibodyName + ' - no sequence') in seqDict:
                seqDict.pop(antibodyName + ' - no sequence')
                abNoSeq.remove(antibodyName)
            if antibodyName not in abWithSeq:
                abWithSeq.append(antibodyName)

            i_sequence = ''

        if isReadingSequence:
                i_sequence += line

        if line[0] == ">":
            if "- no sequence" in line:
                isReadingSequence = False
                continue
            else:
                isReadingSequence = True
                antibodyKey       = line.replace(">", "").rstrip()

    imagedSeq.close()
    return seqDict, abWithSeq, abNoSeq

################################################################################
### Function 4
# ------------
# integrate_dict() --> integratedSeqInfo = RseqDict + PseqDict
# ------------------------------------------------------------
# integrate dict for RL and dict for PL, resulting in integratedSeqINfo
#
# 03/11/2016
#
# Version 1.4 By Ziyi (Echo) Cui
#
def integrate_dicts(RseqDict, RabWithSeq, RabNoSeq, PseqDict):

    listForWarning       = []

    for antibodyKey in PseqDict:
        if antibodyKey in RseqDict:
            if RseqDict[antibodyKey] != PseqDict[antibodyKey]:
                listForWarning.append(antibodyKey)

        elif ' - no sequence' in antibodyKey:
            field        = antibodyKey.split(' - ')
            antibodyName = field[0]
            if antibodyName not in RabWithSeq:
                RseqDict.setdefault(antibodyKey, '')

        else:
            field        = antibodyKey.split('|')
            antibodyName = field[0]
            RseqDict.setdefault(antibodyKey, PseqDict[antibodyKey])
            if antibodyName not in RabWithSeq:
                RabWithSeq.append(antibodyName)
            if (antibodyName + ' - no sequence') in RseqDict:
                RseqDict.pop(antibodyName + ' - no sequence')
                RabNoSeq.remove(antibodyName)

    return RseqDict, RabWithSeq, RabNoSeq, listForWarning

################################################################################
### Function 5
# ------------
# sort_seq() --> chain_appearance = {antibodyName: [chain type]}
# groupName (of antibodies with the same chain_appearance) = [antibodyName]
# ------------------------------------------------------------------------
# sort integratedSeqInfo according to chainType
#
# 03/11/2016
#
# Version 1.4 By Ziyi (Echo) Cui
#
def sort_seq(integratedSeqInfo):

    chain_appearance    = {}
    allInOne            = []
    pairChain           = []
    onlyHeavy           = []
    onlyLight           = []
    multiPair           = {}
    pairWithFusion      = {}
    multiPairWithFusion = {}

    for key in integratedSeqInfo:
        if ' - no sequence' in key:
            pass
        elif ('-' in key) and ('|' in key):
            field = key.split('|')
            allInOne.append(field[0])
        else:
            field = key.split('|')
            antibodyName = field[0]

            if len(field) == 2:
                chainType = field[-1]
                chain_appearance.setdefault(antibodyName, [])
                chain_appearance[antibodyName].append(chainType)
            else:  # case when len(field) = 3
                chainType = field[1] + field[2]
                chain_appearance.setdefault(antibodyName, [])
                chain_appearance[antibodyName].append(chainType)

    for antibodyName in chain_appearance:
        if chain_appearance[antibodyName]   == ['Heavy', 'Light'] \
          or chain_appearance[antibodyName] == ['Light', 'Heavy']:
            pairChain.append(antibodyName)
        elif chain_appearance[antibodyName] ==['Heavy']:
            onlyHeavy.append(antibodyName)
        elif chain_appearance[antibodyName] == ['Light']:
            onlyLight.append(antibodyName)
        elif ('Heavy2' in chain_appearance[antibodyName]) \
            or ('Light2' in chain_appearance[antibodyName]):
            multiPair.setdefault(antibodyName, chain_appearance[antibodyName])

        else:
            if len(chain_appearance[antibodyName]) == 2:
                pairWithFusion.setdefault(antibodyName, chain_appearance[antibodyName])
            else:
                multiPairWithFusion.setdefault(antibodyName, chain_appearance[antibodyName])
    
    #print(chain_appearance)
    #print('5.multiPair=', multiPair)
    #print('5.pairWithFusion=',pairWithFusion)
    #print('5.multiPairWithFusion=',multiPairWithFusion)
    #print('5.onlyHeavy=', onlyHeavy)
    #print('5.onlyLight=', onlyLight)
    #print(pairChain)
    return chain_appearance, pairChain,multiPair, onlyHeavy, onlyLight, pairWithFusion, multiPairWithFusion, allInOne
   
################################################################################
### Function 6
# ------------
# format_data() --> string printed out
# ------------------------------------
# format the integrated data and put it into a file
#
# 03/11/2016
#
# Version 1.5 By Ziyi (Echo) Cui
# 
def format_data(integratedSeqInfo):
    formatData              = ''

    for key in integratedSeqInfo:
        if ' - no sequence' in key:
            formatData     += '>' + key + '\n\n'

        else:
            field           = key.split('|')
            antibodyName    = field[0]
            chainType       = field[1]
            correspondingH  = antibodyName   + '|Heavy'
            correspondingL  = antibodyName   + '|Light'
            correspondingLF = antibodyName   + '|Light|Fusion'
            correspondingH2 = antibodyName   + '|Heavy2'
            correspondingL2 = antibodyName   + '|Light2'
            correspondingL2F= antibodyName   + '|Light2|Fusion'
            

            if (antibodyName in pairChain) and chainType == 'Heavy':
                formatData     += '>' + key             + '\n' + integratedSeqInfo[key]             + \
                                  '>' + correspondingL  + '\n' + integratedSeqInfo[correspondingL]  + '\n\n'

            elif (antibodyName in pairWithFusion)and chainType == 'Heavy':
                formatData     += '>' + key + '\n' + integratedSeqInfo[key]
                if correspondingL in integratedSeqInfo:
                    formatData += '>' + correspondingL  + '\n' + integratedSeqInfo[correspondingL]  + '\n\n'
                else:      
                    formatData += '>' + correspondingLF + '\n' + integratedSeqInfo[correspondingLF] + '\n\n'

            elif (antibodyName in multiPair) and (chainType == 'Heavy'):
                formatData     += '>' + key + '\n' + integratedSeqInfo[key]
                if correspondingL in integratedSeqInfo:
                    formatData += '>' + correspondingL  + '\n' + integratedSeqInfo[correspondingL]  + '\n\n'

                if correspondingH2 in integratedSeqInfo:
                    formatData += '>' + correspondingH2 + '\n' + integratedSeqInfo[correspondingH2]
                else:
                    formatData += '>' + key             + '\n' + integratedSeqInfo[key]

                if correspondingL2 in integratedSeqInfo:
                    formatData += '>' + correspondingL2 + '\n' + integratedSeqInfo[correspondingL2] + '\n\n'
                else:
                    formatData += '>' + correspondingL  + '\n' + integratedSeqInfo[correspondingL]  + '\n\n'

            elif antibodyName in multiPairWithFusion:
                    if chainType       == 'Heavy2':
                        formatData      = '>' + correspondingH   + '\n' + integratedSeqInfo[correspondingH]   + \
                                          '>' + correspondingL   + '\n' + integratedSeqInfo[correspondingL]   + '\n\n' + \
                                          '>' + key              + '\n' + integratedSeqInfo[key]
                        
                        if correspondingL2F in integratedSeqInfo:
                            formatData += '>' + correspondingL2F + '\n' + integratedSeqInfo[correspondingL2F] + '\n\n'
                        else:
                            formatData += '>' + correspondingL   + '\n' + integratedSeqInfo[correspondingL]   + '\n\n'

                    elif chainType     == 'Light2':
                            formatData  = '>' + correspondingH   + '\n' + integratedSeqInfo[correspondingH]   + \
                                          '>' + correspondingL   + '\n' + integratedSeqInfo[correspondingL]   + '\n\n' + \
                                          '>' + correspondingH   + '\n' + integratedSeqInfo[correspondingH]   + \
                                          '>' + key              + '\n' + integratedSeqInfo[key]              + '\n\n'

            elif (antibodyName in allInOne) or (antibodyName in  onlyHeavy) or (antibodyName in onlyLight):
                formatData += '>' + key + '\n' + integratedSeqInfo[key] + '\n\n'

    return formatData

################################################################################
### Main program
#
# 03/11/2016 
#
# Version 1.1 By Ziyi (Echo) Cui
#

# Check the command line for '-h' (help)
if sys.argv[-1] == "-h":
    UsageDie()

# test open for each files
testOpen(sys.argv[1])
testOpen(sys.argv[2])
testOpen(sys.argv[3])
testOpen(sys.argv[4])

# 1.get a RseqDict combining the txt data and data manually converted from images
RseqDictonlyWithName, RabWithSeq, RabNoSeq = add_key(sys.argv[1])
#print(len(RabWithSeq),RabWithSeq, len(RabNoSeq),RabNoSeq)
RseqDict = add_seq(sys.argv[1], RseqDictonlyWithName)
RseqDict, RabWithSeq, RabNoSeq = add_imagedSeq(sys.argv[3],RseqDict, RabWithSeq, RabNoSeq)


# 2.get a PseqDict combining the txt data and data manually converted from images
PseqDictonlyWithName, PabWithSeq, PabNoSeq = add_key(sys.argv[2])
PseqDict = add_seq(sys.argv[2], PseqDictonlyWithName)
PseqDict, PabWithSeq, PabNoSeq = add_imagedSeq(sys.argv[4],PseqDict, PabWithSeq, PabNoSeq)


# 3.integrate RseqDict and PseqDict and print out the result after formatting.
integratedSeqInfo, abWithSeq, noSeq, warningList = integrate_dicts(RseqDict, RabWithSeq, RabNoSeq, PseqDict)
chain_appearance, pairChain, multiPair, onlyHeavy, onlyLight, pairWithFusion, multiPairWithFusion, allInOne= sort_seq(integratedSeqInfo)
outPut = format_data(integratedSeqInfo)
print(outPut)






