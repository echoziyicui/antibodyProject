#!/usr/bin/env python3
################################################################################
#
# Program: scoreCluster.py
# Author:  Ziyi Cui
# Version: 2.1
# Date:    03/02/2017
#
# Function:
# ---------
# Provides 5 different methods for giving scores of  unusual clusters on 
# antibody surface.
#
# Usage:
# ------
# scoreCluster.py cluster freqfolder(with/) [-x] -> stdout
# sys.argv[1]  .cl file of cluster info 
# sys.argv[2]  folder of .freq files of residue frequencies
# [-x]         specify the method Number [-1, -2, -3, -4,-5]
################################################################################
# import modules
import os 
import sys
import csv
import collections
################################################################################
# UsageDie()
# ----------
# provide general information about the whole program
#
# 07/11/2016 Version 1.0 By Ziyi (Echo) Cui
#
def UsageDie():
    print("""
    Version:  2.1
    Usage:    scoreCluster.py cluster resfolder(with/) -x -> stdout
              sys.argv[1]  .cl file of cluster info 
              sys.argv[2]  folder of .freq files of residue frequencies
              [-x]         specify the method Number [-1, -2, -3, -4,-5]
    Function: Provides 5 different methods of ranking the score of unusual
              clusters on antibody surface. 
    Date:     03/02/2017 """)
    sys.exit()
################################################################################
### Function 1
# ------------
# score  Uc=ΣU(1-fx)
# rate_clusters_1(clusterFile, freqFolder) --> sumofscore
#
# 30/01/2017
#
# Version 1.1 By Ziyi (Echo) Cui
#
def rate_clusters_1(clusterFile, freqFolder):
   
    freqDict               = {} 
    listoffreq             = []
    listofscore            = []

    basename               = os.path.basename(clusterFile)
    filename               = os.path.splitext(basename)[0]
    freqfilename           = filename + '.num'
    
    clfile                 = open(clusterFile, 'r')
    freqfile               = open(freqFolder + freqfilename, 'r')
    clusters               = clfile.readlines()
    freq                   = freqfile.readlines()
    

    for line in freq:
        field              = line.split()
        unusualness        = 100 - float(field[1])
        freqDict.setdefault(field[0],unusualness)
           
    for line in clusters:
        field              = line.split()

        if field          == []:
            if listoffreq == []:
                continue
            else:
                score      = sum(float(i) for i in listoffreq)
                listofscore.append(score)
                
                
        elif field[0]     == 'Cluster':
           listoffreq      = []
        
        else:
            listoffreq.append(freqDict[field[0]])
            if line       == clusters[-1]:
                score      = sum(float(i) for i in listoffreq)
                listofscore.append(score)

    sumofscore = sum(listofscore)

    clfile.close()
    freqfile.close()
    return filename, sumofscore
################################################################################
### Function 2
# ------------
# score Uc=Σ100/(fx+c), c=20
# rate_clusters_2(clusterFile, freqFolder) --> sumofscore
#
# 31/01/2017
#
# Version 1.1 By Ziyi (Echo) Cui
#
def rate_clusters_2(clusterFile, freqFolder):
    
    freqDict               = {} 
    listoffreq             = []
    listofscore            = []

    basename               = os.path.basename(clusterFile)
    filename               = os.path.splitext(basename)[0]
    freqfilename           = filename + '.num'
    
    clfile                 = open(clusterFile, 'r')
    freqfile               = open(freqFolder + freqfilename, 'r')
    clusters               = clfile.readlines()
    freq                   = freqfile.readlines()
      
    for line in freq:
        field              = line.split()
        unusualness        = 100/(float(field[1])+20)
        freqDict.setdefault(field[0],unusualness)

    for line in clusters:
        field              = line.split()
        if field          == []:
            if listoffreq == []:
                continue
            else:
                score      = sum(float(i) for i in listoffreq)
                listofscore.append(score)
                
        elif field[0]     == 'Cluster':
           listoffreq      = []
        
        else:
            listoffreq.append(freqDict[field[0]])
            if line       == clusters[-1]:
                score      = sum(float(i) for i in listoffreq)
                listofscore.append(score)
 
    sumofscore             = sum(listofscore)
 
    clfile.close()
    freqfile.close()
    return filename, sumofscore
################################################################################
### Function 3
# ------------
# rate_clusters_3(clusterFile, freqFolder) --> sumofscore
# score Uc=N,N is the number of residues found in clusters
#
# 01/02/2017
#
# Version 1.1 By Ziyi (Echo) Cui
#
def rate_clusters_3(clusterFile, freqFolder):

    freqDict               = {} 
    listoffreq             = []
    listofscore            = []
    N                      = 0
    basename               = os.path.basename(clusterFile)
    filename               = os.path.splitext(basename)[0]
    freqfilename           = filename + '.num'
    
    clfile                 = open(clusterFile, 'r')
    freqfile               = open(freqFolder + freqfilename, 'r')
    clusters               = clfile.readlines()
    freq                   = freqfile.readlines()
   
    for line in freq:
        field              = line.split()
        unusualness        = 100/(float(field[1])+20)
        freqDict.setdefault(field[0],unusualness)


    for line in clusters:
        field              = line.split()
       
        if field          == []:
            if N          == 0:
                continue
            else:
               listofscore.append(N)
                
        elif field[0]     == 'Cluster':
           N               = 0
        
        else:
            N             += 1
            if line       ==clusters[-1]:
                listofscore.append(N)
    sumofscore             = sum(listofscore)

    clfile.close()
    freqfile.close()
    return filename, sumofscore
    
################################################################################
### Function 4
# ------------
# rate_clusters_4(clusterFile, freqFolder) --> sumofscore
# score Uc=ΣUx/n
# The score is the result of function 1 divided by the residue numbers found
# in clusters.
# 
# 02/02/2017
#
# Version 1.1 By Ziyi (Echo) Cui
#
def rate_clusters_4(clusterFile, freqFolder):

    freqDict               = {} 
    listoffreq             = []
    listofscore            = []

    basename               = os.path.basename(clusterFile)
    filename               = os.path.splitext(basename)[0]
    freqfilename           = filename + '.num'
    
    clfile                 = open(clusterFile, 'r')
    freqfile               = open(freqFolder + freqfilename, 'r')
    clusters               = clfile.readlines()
    freq                   = freqfile.readlines()
   
    for line in freq:
        field              = line.split()
        unusualness        = 100 - float(field[1])
        freqDict.setdefault(field[0],unusualness)

    for line in clusters:
        field              = line.split()
        #print(field)
        if field          == []:
            if listoffreq == []:
                continue
            else:
                score      = sum(float(i) for i in listoffreq)
                listofscore.append(score)
                
        elif field[0]     == 'Cluster':
           listoffreq      = []
        
        else:
            listoffreq.append(freqDict[field[0]])
            if line       == clusters[-1]:
                score      = sum(float(i) for i in listoffreq)
                listofscore.append(score)
                
    if listofscore        == []:
        sumofscore         = 0
    else:
        sumofscore         = sum(listofscore)/len(listofscore)

    clfile.close()
    freqfile.close()
    return filename, sumofscore
  
################################################################################
### Function 5
# ------------
# rate_clusters_5(clusterFile, freqFolder) --> sumofscore
# score Uc=Σ100/(fx+c)/n, c=20
# The score is the result of function 2 divided by the number of residues found 
# in clusters. 
#
# 31/01/2017
#
# Version 1.1 By Ziyi (Echo) Cui
#
def rate_clusters_5(clusterFile, freqFolder):

    freqDict               = {} 
    listoffreq             = []
    listofscore            = []

    basename               = os.path.basename(clusterFile)
    filename               = os.path.splitext(basename)[0]
    freqfilename           = filename + '.num'
    
    clfile                 = open(clusterFile, 'r')
    freqfile               = open(freqFolder + freqfilename, 'r')
    clusters               = clfile.readlines()
    freq                   = freqfile.readlines()
   
    for line in freq:
        field              = line.split()
        unusualness        = 100/(float(field[1])+20)
        freqDict.setdefault(field[0],unusualness)

    for line in clusters:
        field              = line.split()
        if field          == []:
            if listoffreq == []:
                continue
            else:
                score      = sum(float(i) for i in listoffreq)
                listofscore.append(score)
                
        elif field[0]     == 'Cluster':
           listoffreq      = []
        
        else:
            listoffreq.append(freqDict[field[0]])
            if line       == clusters[-1]:
                score      = sum(float(i) for i in listoffreq)
                listofscore.append(score)
    if listofscore        == []:
        sumofscore         = 0
    else:    
        sumofscore         = sum(listofscore)/len(listofscore)

    clfile.close()
    freqfile.close()
    return filename, sumofscore
################################################################################
### Main program
#
# 03/02/2017
#
# Version 1.1 By Ziyi (Echo) Cui
#

# Check the command line for '-h' (help)
if sys.argv[-1] == "-h":
    UsageDie()

#select which function to use 
func_arg = {"-1":rate_clusters_1, "-2":rate_clusters_2, "-3":rate_clusters_3,
            "-4":rate_clusters_4, "-5": rate_clusters_5}

if __name__ == "__main__":  
       
    antibodyname,finalscore = func_arg[sys.argv[-1]](sys.argv[1],sys.argv[2])
    print(antibodyname,finalscore)
