# Genomics of grey wolf in Central Europe, Diploma thesis 
This GitHub repository was created to store scripts and results related to a thesis called "Genomics of the grey wolf in Central Europe"
  The repository is divided into five directories, which contain documents for each part of the thesis: ANGSD_GL, Daasets_info, KING_results, NGSadmix_results, PCA_results.

This repository contains files in the following formats: _.txt, .cov, .R, .py, .png, .pdf, .csv, .xlsx._ The scripts are written in R(_.R_) and Python (_.py_) programming languages. 
The following READ.me section describes the directories of this repository.  

## ANGSD_GL
This directory contains commands for calculating genotype likelihoods (GL) and a python script for merging the output of the GL calculation.
### _GL_commands.txt_
The commands in this text file generates these outputs: _.txt, .arg, .mafs.gz_, and _.beagle.gz_, the computation is parallelized across chromosomes (38). 
### _merge.py_
This Python script is used to merge Beagle files, which were one of the outputs from GL calculations using ANGSD software. 

## Datasets_info
This directory contains tables of information about the individual formulas used in the work.
### _DT_dataset_info_table.xlsx_
This _.xlsx_ file contains complete information about the samples, it has three sheets that correspond to the _.csv_ files that follow in this directory.
### _filtered_dataset_info.csv_
This _.csv_ file contains information about the filtered dataset (110 samples).
### _full_dataset_info.csv_
This _.csv_ file contains information about the full dataset (165 samples).
### _imput_mvc.csv_
This _.csv_ file contains information about the input file to the minimum vertex cover algorithm. 
