DATA/
====
This folder stores all the data used in this project.

INNData/
-------
Data in this folder is related to the analysis of antibodies extracted from the INN lists.

paperData/
---------
Data in this folder is related to the analysis of antibodies in Hwang's paper (Hwang et.al 2005) and Baker's paper (Baker et.al 2010).

analysis.ods/
-------------
It is the analysis results of this project.
They are separated into different sheets based on the different analysis carried out:
### sheet: list_excluding_unapproved_in5yr
It presents a list of approved and unapproved antibodies with sequences in the INN database, excluding those unapproved one from the recent 5 years.

### sheet: antibodies_with_pdb
It presents a list of antibodies in our database that can get pdb files by 'abyMod'.

### sheet: scores_of_Method_1
It gives the test results for comparing the score difference between approved and unapproved antibodies, based on scoring method 1 (Uc = ∑U(100-fx)).

### sheet: scores_of_Method_2
It gives the test results for comparing the score difference between approved and unapproved antibodies, based on scoring method 2 (Uc = ∑U 100/(fx+c)) and the initial clusering criteria.

### sheet: scores_of_Method_3
It gives the test results for comparing the score difference between approved and unapproved antibodies, based on scoring method 3 (Uc = N) and the initial clusering criteria.

### sheet: scores_of_Method_4
It gives the test results for comparing the score difference between approved and unapproved antibodies, based on scoring method 4 (Uc = ∑U(100-fx)/N) and the initial clusering criteria.

### sheet: scores_of_Method_5
It gives the test results for comparing the score difference between approved and unapproved antibodies, based on scoring method 5 (Uc = ∑U(100-fx)/N) and the initial clusering criteria.

### sheet: analysis_of_3-14-3
It presents a bar chart, showing the separation of approved and unapproved antibodies based on their scores of unusual residues.
The criteria used for clustering and scoring:
####cutoffs for "clusterResidues":
-m = 3
-d = 3, for sc_distmat
accessibility > 10
frequency < 14
#### scoring method: Method 3 (Uc = N, N is the number of residues found in unusual clusters)

### sheet: immunogenicity_data_summary
It presents the immunogenicity levels (AAR incidences) extracted from Hwang's paper and Baker's paper.

### sheet: collect_mab_names
It shows the process of finding the name ending in 'mab' for antibodies from the two papers.

### sheet: u_test_and_t_test_imunogenicity
It shows the test results for two different tests, which compare the difference in the immunogenicity level between approved and unapproved antibodies.

### sheet: immunogenicity_vs_score
It shows a scatter plot of immunogenicity level vs. score (using the initial clustering criteria and scoring method 1)

### sheet: grouping
It sorts the immunogenicty levels into three groups (negligible: <2%, tolerable: 2-15%, marked: >15%)

### drugsWithEmptyPdb
It collects the antibodies failed in structure modeling process and the details of the failure and the correction.