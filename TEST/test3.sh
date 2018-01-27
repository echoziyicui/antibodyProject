#!/bin/bash
# A bash script for testing files with different chain combinations.
#
# version 1.1 on 9.11.2016
# author: (Echo) Ziyi Cui
#

#write the result into a .faa file and compare the difference between this file and expected file.
#test one file containing 5 different cases for chain combinations.

python3 getabnum.py testinput3.faa
diff -b -B  abnum/'cergutuzumab amunaleukin.seq' testfile3/'expected cergutuzumab amunaleukin.seq'
diff -b -B abnum/'cergutuzumab amunaleukin2.seq' testfile3/'expected cergutuzumab amunaleukin2.seq'
diff -b -B abnum/'lulizumab pegol.seq' testfile3/'expected lulizumab pegol.seq' 
diff -b -B abnum/'vanucizumab.seq' testfile3/'expected vanucizumab.seq' 
diff -b -B abnum/'vanucizumab2.seq' testfile3/'expected vanucizumab2.seq'
