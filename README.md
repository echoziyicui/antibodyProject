abypatch
=========
Codes and data for the analysis of unusual clusters on antibody surface.


Programs
---------
### A. Generate database 
#### integrateData.py
It extracts and reformats sequence data of antibodies from INN lists and generates an integrated database of antibody seuqences. 

#### summarizeDatabase.py 
It compares the integrated database to the reference, sorting the antibodies in integrated database into different groups.

#### formatAddedAbFromRef.py
It reforms those antibodies added from reference in the same format as that in the integrated database.

#### testApperance_LINUX.py
It check antibodies in the final integrated database, testing whether they are from the refrence and whether they have sequences.


### B. Get files for clustering
#### getAbNumForDatabase.py
It takes a database of antibody sequences and apply the Chothia scheme to generate a file of numbered sequence for each antibody in the database.

#### getAbNumForOne.py
It takes a file of only one antibody sequence and apply the Chothia scheme to genereate a file of numbered sequence for this antibody.

#### getresfreq.py
It takes a numbered sequence file and replace the amino acid by the corresponding frequency of this resiude at the numbered position, generating a resfreq file.

#### abymod.pl
It takes a numbered sequence of an antibody and do the structual modelling for this antibody, generating a pdb file.

#### seq2pir.py
It takes a .seq file and converts it to the .pir format. It is used for dealing with the modelling failure.

#### distmat
It takes a pdb file and calculate the distance matrix between each two residues.

#### pdbsolv 
It takes a pdb file and calculate the accessibility for each residues.

#### clusterResidues.pl
A program for finding clusters of residues matching a set of
criteria. You need:

[-m=3] specify that each cluster should at least have 3 residues
- a distance matrix to define distances between residues in the PDB file of interest 
- an accessibility file describing the position of each residues, specified >10 to filter only the surface residues
- a frequency file to filter all the residues with frequency lower than a threshold, defined as 'unusual' 

#### autoClusterForDatabase.sh
It automately gives the clusters for each antibody in a given database.

#### autoClusterForONe.sh
It automately gives the clsuters for an antibody with sequence file.

#### scoreCluster.py
It takes a cluster file and can give it a score using 5 different methods.

##### sortScores.py
It sore a list of scores to either an approved group or an unapproved group.


### C. do statistical tests 
#### statisticalTests.py
It takes two samples, and can either do Welch's t test or Mann-Whitney's u test, giving the statiscal value and the p value.

#### scoreAndTest.sh
It automately gives scores to clusters files in a folder and do the statistical tests. Both score method and test type can be specified.


### D. train the cutoffs of cluserResidues
#### trainingCutoffs.sh
It Automates the process from clustering via scoring to statistical test.


### Others
#### template.py
It presents the standard format for a python script.

#### template.sh
It presents the standard format for a bash script.



DATA/
-----
All the data is stored in this folder.

TEST/
----
The test programs and the testfiles used are in this folder.

PAPER/
------
Folder PAPER/ contains the papers used in this project.

scannedLabBook/
---------------
The scanned version of my writtern lab book is stored in this folder as a pdf file.
