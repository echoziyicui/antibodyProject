#!/bin/bash
# A bash script for testing the generatio of pdb files from .seq files
# 
# version 1.0 on 12.12.2016
# auhor: Ziyi (Echo) Cui
#
# run the auto_cluster.sh for the testfile and compare the results with the expected data


./auto_cluster.sh testfile4/testinput4/ testfile4/testoutput4/abpdb/ testfile4/testoutput4/access/ testfile4/testoutput4/scdistmat/
cd testfile4/
diff testoutput4/abpdb/ testexpected4/abpdb/
diff testoutput4/access/ testexpected4/access/
diff testoutput4/scdistmat/ testexpected4/scdistmat/
