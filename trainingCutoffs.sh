#!/bin/bash
################################################################################
# A bash script for presenting the statistical test results of all combinations 
# of cutoffs of clusterResidues.
#
# Author:    Ziyi (Echo) Cui
# Version:   1.0
# Date:      17/03/2017 
# 
# Function:
# --------
# Automate the process from clustering via scoring to statistical test.
# ./clusterResidues.pl -m=3 -d=[1-10] .scdistmat .sa ">10" .num "<[10-30]
# Give the test trying all -d=integer 1 to 10 with freq threshold integer 10 to 30
#
# Usage:
# ------
# ./trainingCutoffs.sh [pdbfolder] [distfolder] [accessibilityfolder] [freqfolder]
################################################################################

pdbfolder=$1
distfolder=$2
accessibilityfolder=$3
freqfolder=$4



for d in `seq 1 10`;do
    for i in `seq 10 30`; do
        folder="${d}_${i}/"
	mkdir -p /acrm/bsmhome/zcbtzcu/git/abypatch/DATA/INNData/dataForClusterResidues/training/cluster/$folder

	for file in "$pdbfolder"*.pdb;do
	    filenameFull=${file##*/}
	    filename=${filenameFull%.*}
	    ./clusterResidues.pl -m=3 -d=$d "$distfolder${filename}.scdistmat" "$accessibilityfolder${filename}.sa" ">10" "$freqfolder${filename}.num" "<${i}" > "/acrm/bsmhome/zcbtzcu/git/abypatch/DATA/INNData/dataForClusterResidues/training/cluster/$folder${filename}.cl"
	done

	for m in `seq 1 5`;do
            scorefile="${d}_${i}_${m}.txt"

	    for file in "/acrm/bsmhome/zcbtzcu/git/abypatch/DATA/INNData/dataForClusterResidues/training/cluster/$folder"*.cl;do
	        python3 scoreCluster.py $file $4 -$m >> /acrm/bsmhome/zcbtzcu/git/abypatch/DATA/INNData/dataForClusterResidues/training/score/$scorefile
	    done

	    echo "${d}_${i}_${m}" >>  /acrm/bsmhome/zcbtzcu/git/abypatch/DATA/INNData/dataForClusterResidues/training/results.txt
	    python3 statisticalTests.py "/acrm/bsmhome/zcbtzcu/git/abypatch/DATA/INNData/dataForClusterResidues/training/score/$scorefile" t >> /acrm/bsmhome/zcbtzcu/git/abypatch/DATA/INNData/dataForClusterResidues/training/results.txt
        done
    done
done


