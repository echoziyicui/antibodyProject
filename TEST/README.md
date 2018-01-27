
TEST
=========
bash scripts and data for testing the programs in abypatch.


bash script
-----------
###1. Tests for the database construction

#### test1.sh
It tests whether integrateData.py can integrate data from different sequence sources.

#### test2.sh
It tests whether integrate.py can format sequences with different chain combinations into the uniform layout.

###2. Tests for getAbNumForDatabase.py

#### test3.sh
It compares the sample results from getAbNumForDatabase.py and the expected data.

###3. Tests for auto_cluster.sh

#### test4.sh
It compares the pdb, solvent accessibility and the distance matrix created from auto_clsuter.sh with the expected outcomes.

datafolder
----

###testfile1/
Input files for test1.sh and the expected outcomes are stored inside.

###testfile2/
Input files for test2.sh and the expected outcomes are stored inside.

###testfile3/
The sample results from getAbNumForDatabase.py and the expected outcomes are stored inside.

###testfile4/
The sample results from auto_cluster.sh and the expected outcomes are stored inside.

###testForTrainig/
It contains the files used to test trainingCutoffs.sh

datafile
--------
### 1yqv.num
This is a sample of numbered sequence, which is used to test getResFreq.py

###siltuximab.faa
This is a file stores sequences for a single antibody, which is used to test getAbNumForOne.py



