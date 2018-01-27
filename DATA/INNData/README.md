INNDATA/
========

seqDatabase/
------------
This folder stores the data for constructing the database of antibody sequences from INN lists.

### integratedDataFinal.faa
It is the latest database constructed. Each entry of an antibody name and a chain type gives an antibody sequence.

### integratedDataFinalForAbnum.faa
It is modified from integratedDataFinal.faa by splitting SCFV into separate chains according to the chain type.

### summaryOfData.txt
This file summarizes the antibodies in the database in these aspects:
-whether they have sequences
-whether they are in the reference list

### mabFromRef/
This folder contains antibodies in the reference list.

### INNsource/
This folder has the .faa, .txt and .pdf files for each list in INN.

### INNextracted/
It contains the pre-integrated data, which stores antibodies from either R lists, P lists, or antibodies with imaged sequences.

dataForClusterResidues/
-----------------------
This folder stores all the files requried to get clusters of unusual residues under the seleted criteria.

### abnum/
It stores the sequences numbered by Chothia scheme.

### resFreq/
It stores the residue frequencies in a list for each antibody.

### accessibility/
It stores the solvent accessibility of each residue in each antibody from the database.

### distmat-a/
It stores the c-alpha distance matrix for each antibody from the database.

### distmat-c/
It stores the side-chain distance matrix for each antibody from the database.

### pdb/
It stores the structures modelled for each antibody using 'abyMod' program.

###cluster/
It stores the clusters found under the selected criteria:
-m=3, -d=4, distmat of sidechain,  accessibility > 10, frequency < 20

### tmp/
It stores the corrected abnum, pdb and resfreq for some antibodies on 16/01/2017.

dataForStats/
-------------
This folder stores data for the statistical results for all five scoring methods under the initial selected criteria of clustering:


###resultOfInitialCriteria
the clustering criteria used in the program'clusterResidues':
-m=3, -d=4, distmat of sidechain,  accessibility > 10, frequency < 20

This folder stores the scores for each of the five scoring methods:
#### score1.txt
Method 1:
Uc = ∑U(100-fx), fx is the frequency of each amino acid found in the clusters of an antibody
#### score2.txt
Method 2:
Uc = ∑U 100/(fx+c), fx is the frequency of each amino acid in the clusters of an antibody
#### score3.txt
Method 3:
Uc = N, N is the number of residues found in the clusers of an antibody
#### score4.txt
Method 4:
Uc = ∑U(100-fx)/N
#### score5.txt
Method 5:
Uc = ∑U 100/(fx+c)/N

#### testResults.txt
It presents the test results of Welch's t test and Mann-Whitney's U test for the scores obtained under each method.
The statistical tests compares the difference in the scores of unusual clusters between approved antibodies and unapproved antibodies.

