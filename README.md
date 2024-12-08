# Genomics of grey wolf in Central Europe, Diploma thesis 
This GitHub repository was created to store scripts and results related to a thesis called "Genomics of the grey wolf in Central Europe"
  The repository is divided into five directories, which contain documents for each part of the thesis: ANGSD_GL, Daasets_info, KING_results, NGSadmix_results, PCA_results.

This repository contains files in the following formats: _.txt, .cov, .R, .py, .png, .pdf, .csv, .xlsx._ The scripts are written in R (.R) and Python (.py) programming languages. 
The following READ.me section describes the directories of this repository.  

##ANGSD_GL
This directory contains commands for calculating genotype likelihoods (GL) and a python script for merging the output of the GL calculation.
#_GL_commands.txt_
The commands in this text file generates these outputs: .txt, .arg, .mafs.gz, and .beagle.gz, the computation is parallelized across chromosomes (38). 
#_merge.py_
This Python script is used to merge Beagle files, which were one of the outputs from GL calculations using ANGSD software. 
