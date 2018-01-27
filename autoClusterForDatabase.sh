#!/bin/bash
################################################################################
# A bash script for automating the process from sequence database  to give
# clusters of unusual residues on antibody surface for each antibody 
#
# Author:    Ziyi (Echo) Cui
# Version:   2.1 #tested
# Date:      21/02/2017
#
# Function:
# ---------
# 1.Apply Chothia numbering scheme,generating a numbered sequence file for an
#   antibody.
# 2.Get residue frequency from web server using the sequence file.
# 3.Create pdb file for each sequence file.
# 4.Generate corresponding files of distance matrix of side chains and the file
#   of accessibility for each residue.
# 5.get clusters using distance matrix, accessibility and residue frequency,with
#   certain cutoffs to find the unusual clusters on antibody surface.
#
# Usage:
# ------
# $1:    database of all antibody sequences
# $2:    folder for putting numbered sequence files
# $3:    folder for putting frequency files
# $4:    folder for putting pdb files 
# $5:    folder for putting accessibility files 
# $6:    folder for putting distance matrix files
# $7:    folder for putting clusterresult files
################################################################################


database=$1 
abnumfolder=$2
freqfolder=$3
pdbfolder=$4
accessibilityfolder=$5
distfolder=$6
clusterfolder=$7

#step1
python3 getAbNumForDatabase.py $database $abnumfolder  


for file in "$abnumfolder"*.seq; do
    filenameFull=${file##*/} #takes the last of the path
    filename=${filenameFull%.*}
    #with %.* only take the filename without extension
    
#step2    
    python3 getResFreq.py "$abnumfolder${filename}.seq" > "$freqfolder${filename}.num"

#step3
    /acrm/bsmhome/abymod/abymod.pl "$abnumfolder${filename}.seq" > "$pdbfolder${filename}.pdb" 
done


#step4
export DATADIR=/home/bsm/martin/data
for file in "$pdbfolder"*.pdb;do
    filenameFull=${file##*/} #takes the last of the path
    filename=${filenameFull%.*}
    ./pdbsolv -n -r stdout "$pdbfolder${filename}.pdb" | awk '{print $2$3, $8}' >"$accessibilityfolder${filename}.sa"
    ./distmat -s -c L,H -p "$pdbfolder${filename}.pdb" > "$distfolder${filename}.scdistmat"
     #get sidechain distansmatrix

#step5
    ./clusterResidues.pl -m=3 -d=4 "$distfolder${filename}.scdistmat" "$accessibilityfolder${filename}.sa" ">10" "$freqfolder${filename}.num" "<20" > "$clusterfolder${filename}.cl"
done