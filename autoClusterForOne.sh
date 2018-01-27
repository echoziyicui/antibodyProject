#!/bin/bash
################################################################################
# A bash script for automating the process from a single sequence to give
# clusters of unusual residues on antibody surface 
#
# Author:    Ziyi (Echo) Cui
# Version:   2.0 tested
# Date:      20/01/2017 
# 
#
# Functions:
# ---------
# 1.Apply Chothia numbering scheme,generating sequence file
# 2.Get residue frequency from web server using the sequence file
# 3.Create pdb file for each .seq file
# 4.Generate corresponding file of distance matrix of side chains and the file
#   of accessibility for each residue.
# 5.Get clusters using distance matrix, accessibility and residue frequency,with
#   certain cutoffs to find the unusual clusters on antibody surface.
#
# Usage:
# ------
#  $1:    a file of antibody sequence 
################################################################################
# input a file using antibodyname as the filename and the file contains the 
# sequence of this antibody
# e.g. siltuximab.faa

file=$1
#echo $file
filenameFull=${file##*/} #takes the last of the path
#echo $filenameFull
filename=${filenameFull%.*} #with %.* only take the filename without extension
#echo $filename #test

#step1
python3 getAbNumForOne.py $file > "${filename}.seq"  

#step2
python3 getResFreq.py "${filename}.seq" > "${filename}.num"

#step3
#echo "${filename}.seq" 
/acrm/bsmhome/abymod/abymod.pl "${filename}.seq" > "${filename}.pdb" 

#step4
export DATADIR=/home/bsm/martin/data
./pdbsolv -n -r stdout "${filename}.pdb" | awk '{print $2$3, $8}' >"${filename}.sa"
./distmat -s -c L,H -p "${filename}.pdb" > "${filename}.scdistmat" #get sidechain distansmatrix

#step5
./clusterResidues.pl -m=3 -d=4 "${filename}.scdistmat" "${filename}.sa" ">10" "${filename}.num" "<20" > "${filename}.cl" 

