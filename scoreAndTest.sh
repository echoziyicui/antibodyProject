#!/bin/bash
################################################################################
# A bash script for giving score to each antibody according to their unusual
# clusters and perform statistical test.
#
# Author:    Ziyi (Echo) Cui
# Version:   1.0 
# Date:      28/02/2017
#
# Function:
# ---------
# Rate the clusters for all antibodies in a given folder, using specific ranking
# method.
#
# Usage:
# ------
# scoreAllAbs.sh [input folder] [freqfolder] [-N] [.txt] [testtype]
# [input folder]  a folder containing all the .cl files to be rated and tested
# [freq folder]   a folder of .freq files of residue frequencies  
# [-N]:           (-1, -2, -3, -4) specify the number of method for ranking the 
#                 clusters
# [.txt]:         a txt file storing the list of scores for clusters. 
# [test type]:    [t] for welch t test; [u] for mann-whitney u test 
################################################################################

#[input folder] $1
#[freq folder]  $2
#[-N]           $3
#[.txt]         $4 
#[testtype]     $5

> $4 # empty the .txt file
for file in "$1"*.cl;do
    python3 scoreCluster.py $file $2 $3 >> $4 
    # >> to append instead of overwriting
done

python3 statisticalTests.py $4 $5
