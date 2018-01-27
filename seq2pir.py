#!/usr/bin/env python3
################################################################################
#
# program: seq2pir.py
# Author:  (Echo) Ziyi Cui
# version: Version 1.0
# Date: 27/02/2017   
#
# Function:
# ---------
# Convert .seq file to .pir
#
# Usage:
# ------
# seq2pir.py + .seq > .pir 
# sys.argv[1]  the .seq file input that requires convertion
################################################################################
# import
import textwrap
import sys
################################################################################
# UsageDie()
# ----------
# provide general information about the whole program
#
# 28/02/2017 version 1.0 By Ziyi (Echo) Cui
#
def UsageDie():
    print("""
    Version:    1.0 
    Usage:      seq2pir.py + .seq > .pir 
    sys.argv[1] the .seq file input that requires convertion
    Function:   Convert .seq file to .pir
    Date:       27/02/2017   """)
    sys.exit()

################################################################################### Function 1
# ------------
# convert seq file into pir 
#
# 27/02/2017
#
# Version 1.0 By Ziyi (Echo) Cui
#
def seq2pir(InputFile):
    seq           = open(InputFile, "r")
    pirH          = ''    
    pirL          = ''

    for line in seq.readlines():
       
        field     = line.split()
        
        if field == []:
            continue
       
        elif 'H' in field[0]:
            pirH += field[1]
        elif 'L' in field[0]:
            pirL += field[1]

    pirH_F        = textwrap.fill(pirH,30)
    pirL_F        = textwrap.fill(pirL,30)
    
    pir           = pirH_F + '*\n' + pirL_F + '*'
    print(pir)
###################################################################################  Main program
#
# 27/02/2017 
# Cersion 1.0 By Ziyi (Echo) Cui
#
 
# Check the command line for '-h' (help)
if sys.argv[-1] == "-h":
    UsageDie()
           
print(">P1;PDBPIR" +"\n"+ "Sequence extracted from PDB file - By pdb2pir")
seq2pir(sys.argv[1])
