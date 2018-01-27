#!/usr/bin/env python3
################################################################################
#
# Program: statisticalTests.py
# Author:  Ziyi Cui
# Version: 1.2
# Date:    07/03/2017
#
# Function:
# ---------
# Perform statistical test for scores of unusual residue clusters of antibodies.
#
# Usage:
# ------
# statisticalTests.py [.txt] [test type]
# [.txt]      file with cluster score for all antibodies
# [test type] [t] for Welch t test; [u] for Mann-Whitney u test 
################################################################################
# import modules
import sys
import csv
import numpy as np
import scipy
from scipy import stats 
import pandas
################################################################################
scoreDict = {}
approvedls = []
unapprovedls = []
list_approved=['adalimumab', 'arcitumomab', 'atezolizumab', 'avelumab', 'basiliximab', 'bavituximab', 'blinatumomab', 'brodalumab', 'certolizumab', 'daclizumab', 'daratumumab', 'denosumab', 'efalizumab', 'ibritumomab', 'ipilimumab', 'necitumumab', 'obiltoxaximab', 'ofatumumab', 'olaratumab', 'ranibizumab', 'rituximab', 'romosozumab', 'sarilumab', 'secukinumab', 'siltuximab', 'sirukumab', 'tositumomab', 'alemtuzumab', 'alirocumab', 'brentuximab', 'canakinumab', 'evolocumab', 'ixekizumab', 'nivolumab', 'pembrolizumab', 'ustekinumab', 'vedolizumab', 'omalizumab', 'ramucirumab', 'gemtuzumab', 'abciximab', 'dinutuximab', 'obinutuzumab', 'cetuximab', 'trastuzumab', 'idarucizumab']
list_unapproved=['remtolumab', 'adalimumab', 'arcitumomab', 'atezolizumab', 'avelumab', 'basiliximab', 'bavituximab', 'blinatumomab', 'brodalumab', 'certolizumab', 'daclizumab', 'daratumumab', 'denosumab', 'efalizumab', 'ibritumomab', 'ipilimumab', 'necitumumab', 'obiltoxaximab', 'ofatumumab', 'olaratumab', 'ranibizumab', 'rituximab', 'romosozumab', 'sarilumab', 'secukinumab', 'actoxumab', 'alacizumab_pegol', 'amatuximab', 'aprutumab', 'ascrinvacumab', 'atinumab', 'benralizumab', 'bezlotoxumab', 'blosozumab', 'brazikumab', 'burosumab', 'camrelizumab', 'carlumab', 'carotuximab', 'conatumumab', 'crizanlizumab', 'crotedumab', 'depatuxizumab', 'drozitumab', 'efungumab', 'elezanumab', 'enokizumab', 'enoticumab', 'eptinezumab', 'erenumab', 'farletuzumab', 'fezakinumab', 'fibatuzumab', 'flanvotumab', 'foralumab', 'fresolimumab', 'fulranumab', 'futuximab', 'ganitumab', 'gantenerumab', 'gemtuzumab2', 'gevokizumab', 'girentuximab', 'icrucumab', 'ifabotuzumab', 'imgatuzumab', 'inclacumab', 'intetumumab', 'iratumumab', 'itolizumab', 'laprituximab', 'lirilumab', 'lucatumumab', 'motavizumab', 'moxetumomab_pasudotox', 'narnatumab', 'nesvacumab', 'ocaratuzumab', 'olokizumab', 'orticumab', 'oxelumab', 'pasotuxizumab', 'pateclizumab', 'pidilizumab', 'pogalizumab', 'prezalumab', 'quilizumab', 'racotumomab', 'radretumab', 'roledumab', 'rosmantuzumab', 'sapelizumab', 'seribantumab', 'setoxaximab', 'sifalimumab', 'solitomab', 'tabalumab', 'tamtuvetmab', 'tavolixizumab', 'teplizumab', 'tregalizumab', 'ublituximab', 'urelumab', 'utomilumab', 'veltuzumab', 'vesencumab', 'vorsetuzumab', 'abagovomab', 'bimagrumab', 'dalotuzumab', 'dezamizumab', 'elotuzumab', 'emapalumab', 'ensituximab', 'fasinumab', 'foravirumab', 'ibalizumab', 'iodine_girentuximab', 'lambrolizumab', 'lebrikizumab', 'lodelcizumab', 'lorvotuzumab_mertansin', 'lupartumab', 'lutikizumab', 'milatuzumab', 'onartuzumab', 'panobacumab', 'parsatuzumab', 'perakizumab', 'pinatuzumab_vedotin', 'ranevetmab', 'rozanolixizumab', 'sacituzumab_govitecan', 'samalizumab', 'suptavumab', 'tadocizumab', 'tigatuzumab', 'vatelizumab', 'cixutumumab', 'etaracizumab', 'fremanezumab', 'gemetuzumab', 'ligelizumab', 'namilumab', 'naratuximab', 'pritoxaximab', 'rilotumumab', 'rontalizumab', 'stamulumab', 'tanezumab', 'vunakizumab', 'bavituximab', 'briakinumab', 'dusigitumab', 'lanadelumab', 'lendalizumab', 'patritumab', 'polatuzumab_vedotin', 'ponezumab', 'telisotuzumab', 'andecaliximab', 'brolucizumab', 'cantuzumab_ravtansin', 'demcizumab', 'enavatuzumab', 'ficlatuzumab', 'navicixizumab', 'otelixizumab', 'robatumumab', 'suvizumab', 'tildrakizumab', 'anrukinzumab', 'citatuzumab_bogatox', 'concizumab', 'inebilizumab', 'lampalizumab', 'tralokinumab', 'dacetuzumab', 'ozanezumab', 'simtuzumab', 'etrolizumab', 'mogamulizumab', 'crenezumab', 'solanezumab', 'zatuximab']
################################################################################
# UsageDie()
# ----------
# provide general information about the whole process.
#
# 07.11.16 Original version By: Echo
def UsageDie():
    print("""
    version:   1.0
    Function:  Perform statistical test for scores of unusual residue clusters of antibodies.
    Usage:     statisticalTests.py [.txt] [test type]
               [.txt]       file with cluster score for all antibodies
               [test type] [t] for Welch t test; [u] for Mann-Whitney u test   
    Date:      07/03/2017   """)
    sys.exit()

################################################################################
# Function 1
# ----------
# Extract data in .txt file and convert them to arrays
#
# 06/02/2017 version 1.0 By Ziyi (Echo) Cui
#
def extract_data(InputFileHandle):    
    scorefile       = open(InputFileHandle, 'r')

    for line in scorefile.readlines():
        field       = line.split()
        rawscore    = float(field[1])
        score       = "{0:.3f}".format(rawscore) # round to 3 decimal places
        scoreDict.setdefault(field[0],score)

        # Sort score results to two arrays
        if field[0] in list_approved:
            approvedls.append(score)
        elif field[0] in list_unapproved:
            unapprovedls.append(score)
        
        
    approvedArray   = np.asarray(approvedls).astype(np.float)
    unapprovedArray = np.asarray(unapprovedls).astype(np.float)
 
    return scoreDict, approvedArray, unapprovedArray

################################################################################
### Function 2
# ------------
# do welch t test on sample a and b
# ---------------------------------
# We can use this test, if we observe two independent samples from the same or 
# different population, e.g. exam scores of boys and girls or of two ethnic groups.
# The test measures whether the average (expected) value differs significantly
# across samples.
# If we observe a large p-value, for example larger than 0.05 or 0.1, then we
# cannot reject the null hypothesis of identical average scores. If the p-value
# is smaller than the threshold, e.g. 1%, 5% or 10%, then we reject the null
# hypothesis of equal averages
#
# 28/02/2017
#
# Version 1.1 By Ziyi (Echo) Cui
#

def welch_ttest(a,b):  # a,b: array_like

   t, p =  stats.ttest_ind(a,b, axis=0, equal_var=False, nan_policy='propagate')
   
   t_value = "{0:.3f}".format(t) 
   p_value = "{0:.3f}".format(p) #two-tailed p value

   return t_value, p_value
################################################################################
### Function 3
# ------------
# Compute the Man-Whitney rank test on samples a and b. 
# -----------------------------------------------------
# Use only when the number of observation in each sample is > 20 and you have 2
# independent samples of ranks. Mann-Whitney U is significant if the u-obtained
# is LESS THAN or equal to the critical value of U.
#
# This test corrects for ties and by default uses a continuity correction.
#
# Statistical talbes for the Mann-Whitney U test are used to find the probability
# of observing a value of U or lower. If the test is one-sided, p is the p-value;
# if the test is two- sided, then double this probability to obtain the p-value.
# 28/02/2017
#
# Version 1.0 By Ziyi (Echo) Cui
#
def u_test(a,b):
    
    u, p2 = stats.mannwhitneyu(a,b, use_continuity=True, alternative='greater')
    #one-side p value

    u_value  = "{0:.3f}".format(u) 
    p2_value = "{0:.3f}".format(2) 


    return u_value, p2_value
################################################################################
### Main program
#
# 28/02/17
#
# Version 1.0 By Ziyi (Echo) Cui
#

# Check the command line for '-h' (help)
if sys.argv[-1] == "-h":
    UsageDie()

Dict, array_a, array_u = extract_data(sys.argv[1])

# select which test to use 
func_arg = {"t":welch_ttest, "u":u_test}

if __name__ == "__main__":  
    statistic, pvalue = func_arg[sys.argv[-1]](array_a, array_u)
    print('t_or_u=',statistic,'p=',pvalue)
 



