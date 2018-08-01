#!/bin/bash
for i in ../data/edges/*.txt
do
    ## Get the file name
    fname="${i##*/}"
    echo "processing $fname"
    mcl ../data/edges/$fname --abc -o ../data/clusters/clusters_$fname.tsv

done
