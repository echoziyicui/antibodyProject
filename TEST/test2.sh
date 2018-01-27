#!/bin/bash
# A bash script for testing files with different chain combinations from PL and RL.
#
# version 1.0 on 3.11.2016
# author: (Echo) Ziyi Cui
#

#write the result into a .faa file and compare the difference between this file and expected file.
#test 13 sets of testfiles in testfile2: with different chain combinations.

python3 integrateData.py testfile2/R1.faa testfile2/P1.faa testfile2/IR1.faa testfile2/IP1.faa >testfile2/1.faa
diff -b -B testfile2/1.faa testfile2/expected1.faa

python3 integrateData.py testfile2/R2.faa testfile2/P2.faa testfile2/IR2.faa testfile2/IP2.faa >testfile2/2.faa
diff -b -B testfile2/2.faa testfile2/expected2.faa

python3 integrateData.py testfile2/R3.faa testfile2/P3.faa testfile2/IR3.faa testfile2/IR3.faa >testfile2/3.faa
diff -b -B testfile2/3.faa testfile2/expected3.faa

python3 integrateData.py testfile2/R4.faa testfile2/P4.faa testfile2/IR4.faa testfile2/IP4.faa >testfile2/4.faa
diff -b -B testfile2/4.faa testfile2/expected4.faa

python3 integrateData.py testfile2/R5.faa testfile2/P5.faa testfile2/IR5.faa testfile2/IP5.faa >testfile2/5.faa
diff -b -B testfile2/5.faa testfile2/expected5.faa

python3 integrateData.py testfile2/R6.faa testfile2/P6.faa testfile2/IR6.faa testfile2/IP6.faa >testfile2/6.faa
diff -b -B testfile2/6.faa testfile2/expected6.faa

python3 integrateData.py testfile2/R7.faa testfile2/P7.faa testfile2/IR7.faa testfile2/IP7.faa >testfile2/7.faa
diff -b -B testfile2/7.faa testfile2/expected7.faa

python3 integrateData.py testfile2/R8.faa testfile2/P8.faa testfile2/IR8.faa testfile2/IP8.faa >testfile2/8.faa
diff -b -B testfile2/8.faa testfile2/expected8.faa

python3 integrateData.py testfile2/R9.faa testfile2/P9.faa testfile2/IR9.faa testfile2/IP9.faa >testfile2/9.faa
diff -b -B testfile2/9.faa testfile2/expected9.faa

python3 integrateData.py testfile2/R10.faa testfile2/P10.faa testfile2/IR10.faa testfile2/IP10.faa >testfile2/10.faa
diff -b -B testfile2/10.faa testfile2/expected10.faa

python3 integrateData.py testfile2/R11.faa testfile2/P11.faa testfile2/IR11.faa testfile2/IP11.faa >testfile2/11.faa
diff -b -B testfile2/11.faa testfile2/expected11.faa

python3 integrateData.py testfile2/R12.faa testfile2/P12.faa testfile2/IR12.faa testfile2/IP12.faa >testfile2/12.faa
diff -b -B testfile2/12.faa testfile2/expected12.faa

python3 integrateData.py testfile2/R13.faa testfile2/P13.faa testfile2/IR13.faa testfile2/IP13.faa >testfile2/13.faa
diff -b -B testfile2/13.faa testfile2/expected13.faa

