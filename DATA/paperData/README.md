paperData/
========

seqDatabase/
------------
This folder stores the data for constructing the database of antibody sequences from Hwang's paper and Baker's paper.

### allAbFromPaper.faa
It store the whole database of antibody sequences from two papers.

### abFromPaper1601.faa
This folder contains antibodies added on 16/01/2017.

### supplementalInfo1601.txt
It provides information about antibodies dded on 16/01/2017.

### abFromPaper2102.faa
This folder contains antibodies added on 21/02/2017.

### summaryOfAllAbFromPaper.txt
It summarizes the antibodies in allAbFromPaper.faa in these aspect:
-whether approved or not
-whether have sequences
-whether have immunogenicity data


dataForClusterResidues/
-----------------------
This folder stores all the files requried to get clusters of unusual residues under the seleted criteria.

### abnum/
It stores the sequences numbered by Chothia scheme.

### resFreq/
It stores the residue frequencies in a list for each antibody.

### accessibility/
It stores the solvent accessibility of each residue in each antibody from the database.

### distmat/
It stores the side-chain distance matrix for each antibody from the database.

### pdb/
It stores the structures modelled for each antibody using 'abyMod' program.

###cluster/
It stores the clusters found under the selected criteria:
-m=3, -d=4, distmat of sidechain,  accessibility > 10, frequency < 20

### abWithPdbErr/
It stores the antibodies that failed in structure modeling with their fixed pdbs and related files (abnum,resFreq,solv,pdb,cluster)

#### tpl/
It stores the intermediate files for those antibodies failed in modeling.

#### pir/
It stores the sequences in .pir form for antibodies and their corresponding template found in modeling.

