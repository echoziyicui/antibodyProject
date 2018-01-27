#!/bin/bash
# A bash script for testing files with different sequence sources.
#
# version 1.1 on 3.11.2016
# author: (Echo) Ziyi Cui
#

#write the result into a .faa file and compare the difference between this file and expected file.
#test 18 sets of testfiles in testfile1: with 18 combinations of sequence sources.

cp testfile1/R1.faa testfile1/expected1.faa
python3 integrateData.py testfile1/R1.faa testfile1/P1.faa testfile1/IR1.faa testfile1/IP1.faa >testfile1/1.faa
diff -b -B testfile1/1.faa testfile1/expected1.faa

cp testfile1/R2.faa testfile1/expected2.faa
python3 integrateData.py testfile1/R2.faa testfile1/P2.faa testfile1/IR2.faa testfile1/IP2.faa >testfile1/2.faa
diff -b -B testfile1/2.faa testfile1/expected2.faa

cp testfile1/R3.faa testfile1/expected3.faa
python3 integrateData.py testfile1/R3.faa testfile1/P3.faa testfile1/IR3.faa testfile1/IR3.faa >testfile1/3.faa
diff -b -B testfile1/3.faa testfile1/expected3.faa

cp testfile1/R4.faa testfile1/expected4.faa
python3 integrateData.py testfile1/R4.faa testfile1/P4.faa testfile1/IR4.faa testfile1/IP4.faa >testfile1/4.faa
diff -b -B testfile1/4.faa testfile1/expected4.faa

cp testfile1/R5.faa testfile1/expected5.faa
python3 integrateData.py testfile1/R5.faa testfile1/P5.faa testfile1/IR5.faa testfile1/IP5.faa >testfile1/5.faa
diff -b -B testfile1/5.faa testfile1/expected5.faa

cp testfile1/R6.faa testfile1/expected6.faa
python3 integrateData.py testfile1/R6.faa testfile1/P6.faa testfile1/IR6.faa testfile1/IP6.faa >testfile1/6.faa
diff -b -B testfile1/6.faa testfile1/expected6.faa

cp testfile1/P7.faa testfile1/expected7.faa
python3 integrateData.py testfile1/R7.faa testfile1/P7.faa testfile1/IR7.faa testfile1/IP7.faa >testfile1/7.faa
diff -b -B testfile1/7.faa testfile1/expected7.faa

cp testfile1/P8.faa testfile1/expected8.faa
python3 integrateData.py testfile1/R8.faa testfile1/P8.faa testfile1/IR8.faa testfile1/IP8.faa >testfile1/8.faa
diff -b -B testfile1/8.faa testfile1/expected8.faa

cp testfile1/IR9.faa testfile1/expected9.faa
python3 integrateData.py testfile1/R9.faa testfile1/P9.faa testfile1/IR9.faa testfile1/IP9.faa >testfile1/9.faa
diff -b -B testfile1/9.faa testfile1/expected9.faa

cp testfile1/R10.faa testfile1/expected10.faa
python3 integrateData.py testfile1/R10.faa testfile1/P10.faa testfile1/IR10.faa testfile1/IP10.faa >testfile1/10.faa
diff -b -B testfile1/10.faa testfile1/expected10.faa

cp testfile1/IR11.faa testfile1/expected11.faa
python3 integrateData.py testfile1/R11.faa testfile1/P11.faa testfile1/IR11.faa testfile1/IP11.faa >testfile1/11.faa
diff -b -B testfile1/11.faa testfile1/expected11.faa

cp testfile1/IP12.faa testfile1/expected12.faa
python3 integrateData.py testfile1/R12.faa testfile1/P12.faa testfile1/IR12.faa testfile1/IP12.faa >testfile1/12.faa
diff -b -B testfile1/12.faa testfile1/expected12.faa

cp testfile1/IR13.faa testfile1/expected13.faa
python3 integrateData.py testfile1/R13.faa testfile1/P13.faa testfile1/IR13.faa testfile1/IP13.faa >testfile1/13.faa
diff -b -B testfile1/13.faa testfile1/expected13.faa

cp testfile1/R14.faa testfile1/expected14.faa
python3 integrateData.py testfile1/R14.faa testfile1/P14.faa testfile1/IR14.faa testfile1/IP14.faa >testfile1/14.faa
diff -b -B testfile1/14.faa testfile1/expected14.faa

cp testfile1/P15.faa testfile1/expected15.faa
python3 integrateData.py testfile1/R15.faa testfile1/P15.faa testfile1/IR15.faa testfile1/IP15.faa >testfile1/15.faa
diff -b -B testfile1/15.faa testfile1/expected15.faa

cp testfile1/P16.faa testfile1/expected16.faa
python3 integrateData.py testfile1/R16.faa testfile1/P16.faa testfile1/IR16.faa testfile1/IP16.faa >testfile1/16.faa
diff -b -B testfile1/16.faa testfile1/expected16.faa

cp testfile1/IP17.faa testfile1/expected17.faa
python3 integrateData.py testfile1/R17.faa testfile1/P17.faa testfile1/IR17.faa testfile1/IP17.faa >testfile1/17.faa
diff -b -B testfile1/17.faa testfile1/expected17.faa

cp testfile1/IR18.faa testfile1/expected18.faa
python3 integrateData.py testfile1/R18.faa testfile1/P18.faa testfile1/IR18.faa testfile1/IP18.faa >testfile1/18.faa
diff -b -B testfile1/18.faa testfile1/expected18.faa
