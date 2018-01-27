#!/usr/bin/env python3
################################################################################
#
# Program:  sortScores.py
# Author:  Ziyi Cui
# Version: 1.0
# Date:    27/03/2017
#
# Function:
# ---------
# It sorts the scores to either an approved list or unapproved list.
#
# Usage:
# ------
# sortScores.py [scorelist]
# [scorelist]   file with a list of scores for all antibodies.
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
list_approved = ['adalimumab', 'arcitumomab', 'atezolizumab', 'avelumab', 'basiliximab','blinatumomab',
                 'brodalumab', 'certolizumab', 'daclizumab', 'daratumumab', 'denosumab', 'efalizumab', 'ibritumomab',
                 'ipilimumab', 'necitumumab', 'obiltoxaximab', 'ofatumumab', 'olaratumab', 'ranibizumab', 'rituximab',
                 'romosozumab', 'sarilumab', 'secukinumab', 'siltuximab', 'sirukumab', 'tositumomab', 'alemtuzumab',
                 'alirocumab', 'brentuximab', 'canakinumab', 'evolocumab', 'ixekizumab', 'nivolumab', 'pembrolizumab',
                 'ustekinumab', 'vedolizumab', 'omalizumab', 'ramucirumab', 'gemtuzumab', 'abciximab', 'dinutuximab',
                 'obinutuzumab', 'cetuximab', 'trastuzumab', 'idarucizumab']
list_unapproved = ['bavituximab','remtolumab', 'adalimumab', 'arcitumomab', 'atezolizumab', 'avelumab', 'basiliximab', 'bavituximab',
                   'blinatumomab', 'brodalumab', 'certolizumab', 'daclizumab', 'daratumumab', 'denosumab', 'efalizumab',
                   'ibritumomab', 'ipilimumab', 'necitumumab', 'obiltoxaximab', 'ofatumumab', 'olaratumab',
                   'ranibizumab', 'rituximab', 'romosozumab', 'sarilumab', 'secukinumab', 'actoxumab',
                   'alacizumab_pegol', 'amatuximab', 'aprutumab', 'ascrinvacumab', 'atinumab', 'benralizumab',
                   'bezlotoxumab', 'blosozumab', 'brazikumab', 'burosumab', 'camrelizumab', 'carlumab', 'carotuximab',
                   'conatumumab', 'crizanlizumab', 'crotedumab', 'depatuxizumab', 'drozitumab', 'efungumab',
                   'elezanumab', 'enokizumab', 'enoticumab', 'eptinezumab', 'erenumab', 'farletuzumab', 'fezakinumab',
                   'fibatuzumab', 'flanvotumab', 'foralumab', 'fresolimumab', 'fulranumab', 'futuximab', 'ganitumab',
                   'gantenerumab', 'gemtuzumab2', 'gevokizumab', 'girentuximab', 'icrucumab', 'ifabotuzumab',
                   'imgatuzumab', 'inclacumab', 'intetumumab', 'iratumumab', 'itolizumab', 'laprituximab', 'lirilumab',
                   'lucatumumab', 'motavizumab', 'moxetumomab_pasudotox', 'narnatumab', 'nesvacumab', 'ocaratuzumab',
                   'olokizumab', 'orticumab', 'oxelumab', 'pasotuxizumab', 'pateclizumab', 'pidilizumab', 'pogalizumab',
                   'prezalumab', 'quilizumab', 'racotumomab', 'radretumab', 'roledumab', 'rosmantuzumab', 'sapelizumab',
                   'seribantumab', 'setoxaximab', 'sifalimumab', 'solitomab', 'tabalumab', 'tamtuvetmab',
                   'tavolixizumab', 'teplizumab', 'tregalizumab', 'ublituximab', 'urelumab', 'utomilumab', 'veltuzumab',
                   'vesencumab', 'vorsetuzumab', 'abagovomab', 'bimagrumab', 'dalotuzumab', 'dezamizumab', 'elotuzumab',
                   'emapalumab', 'ensituximab', 'fasinumab', 'foravirumab', 'ibalizumab', 'iodine_girentuximab',
                   'lambrolizumab', 'lebrikizumab', 'lodelcizumab', 'lorvotuzumab_mertansin', 'lupartumab',
                   'lutikizumab', 'milatuzumab', 'onartuzumab', 'panobacumab', 'parsatuzumab', 'perakizumab',
                   'pinatuzumab_vedotin', 'ranevetmab', 'rozanolixizumab', 'sacituzumab_govitecan', 'samalizumab',
                   'suptavumab', 'tadocizumab', 'tigatuzumab', 'vatelizumab', 'cixutumumab', 'etaracizumab',
                   'fremanezumab', 'gemetuzumab', 'ligelizumab', 'namilumab', 'naratuximab', 'pritoxaximab',
                   'rilotumumab', 'rontalizumab', 'stamulumab', 'tanezumab', 'vunakizumab', 'bavituximab',
                   'briakinumab', 'dusigitumab', 'lanadelumab', 'lendalizumab', 'patritumab', 'polatuzumab_vedotin',
                   'ponezumab', 'telisotuzumab', 'andecaliximab', 'brolucizumab', 'cantuzumab_ravtansin', 'demcizumab',
                   'enavatuzumab', 'ficlatuzumab', 'navicixizumab', 'otelixizumab', 'robatumumab', 'suvizumab',
                   'tildrakizumab', 'anrukinzumab', 'citatuzumab_bogatox', 'concizumab', 'inebilizumab', 'lampalizumab',
                   'tralokinumab', 'dacetuzumab', 'ozanezumab', 'simtuzumab', 'etrolizumab', 'mogamulizumab',
                   'crenezumab', 'solanezumab', 'zatuximab']
# unapproved list exclude antibodies from the recent 5 years


################################################################################
# UsageDie()
# ----------
# provide general information about the whole process.
#
# 07.11.17 Original version By: Echo
def UsageDie():
    print("""
    version:   1.0
    Function:  It sorts the scores to either an approved list or unapproved list
    Usage:     sortScores.py [scorelist]
               [scorelist]   file with a list of scores for all antibodies.
    Date:      27/03/2017   """)
    sys.exit()


################################################################################
# Function 1
# ----------
# Extract data in .txt file and convert them to arrays
#
# 27/03/2017 version 1.0 By Ziyi (Echo) Cui
#
def extract_data(InputFileHandle):
    scorefile = open(InputFileHandle, 'r')

    for line in scorefile.readlines():
        field = line.split()
        score = int(field[1])
        # score = float(field[1])
        # score = "{0:.3f}".format(rawscore)  # round to 3 decimal places
        scoreDict.setdefault(field[0], score)

        # Sort score results to two arrays
        if field[0] in list_approved:
            approvedls.append(score)
        elif field[0] in list_unapproved:
            unapprovedls.append(score)

    # approvedArray = np.asarray(approvedls).astype(np.float)
    # unapprovedArray = np.asarray(unapprovedls).astype(np.float)

    return scoreDict, approvedls, unapprovedls

################################################################################
### Main program
#
# 27/03/17
#
# Version 1.0 By Ziyi (Echo) Cui
#
# Check the command line for '-h' (help)
if sys.argv[-1] == "-h":
    UsageDie()

Dict, ls_a, ls_u = extract_data(sys.argv[1])
print(ls_a)
print(ls_u)
