# Genomics of grey wolf in Central Europe, Diploma thesis 
This GitHub repository was created to store scripts and results related to a thesis called "Genomics of the grey wolf in Central Europe"
  The repository is divided into five directories, which contain documents for each part of the thesis: ANGSD_GL, Datasets_info, Relatedness, NGSadmix, PCAngsd.

This repository contains files in the following formats: _.txt, .cov, .R, .py, .png, .pdf, .csv, .xlsx._ The scripts are written in R(_.R_) and Python (_.py_) programming languages. 
The following README.md section describes the directories of this repository.  

## ANGSD_GL
This directory contains commands for calculating genotype likelihoods (GL) and a python script for merging the output of the GL calculation.
### _GL_commands.txt_
The commands in this text file generates these outputs: _.txt, .arg, .mafs.gz_, and _.beagle.gz_, the computation is parallelized across chromosomes (38). 
### _merge.py_
This Python script is used to merge Beagle files, which were one of the outputs from GL calculations using ANGSD software. 

## Datasets_info
This directory contains tables of information about the individual samples used in the work.
### _DT_dataset_info_table.xlsx_
This _.xlsx_ file contains complete information about the samples, it has three sheets that correspond to the _.csv_ files that follow in this directory.
### _filtered_dataset_info.csv_
This _.csv_ file contains information about the filtered dataset (110 samples).
### _full_dataset_info.csv_
This _.csv_ file contains information about the full dataset (165 samples).
### _imput_mvc.csv_
This _.csv_ file contains information about the input file to the minimum vertex cover algorithm. 

## NGSadmix
This directory contains results, used scripts and commands from the anylitic part where cluster analysis via NGSadmix was performed.
### _Filtered_dataset_results_
This directory contains visualizations of the NGSadmix analysis results for filtered dataset,
for K3, K4, K5, K6, K8 in _.pdf_ format.
### _Full_dataset_results_
This directory contains visualizations of the NGSadmix analysis results for full dataset,
for K3, K4, K5, K6, K8 in _.pdf_ format.
### _run_commands.txt_
### _visualization_NGSadmix_skript.R_

## PCAngsd
This directory contains results, used scripts and commands from the anylitic part where cluster analysis via PCAngsd was performed.
### Filtered_dataset_results
This directory contains visualizations of the PCA analysis results for filtered dataset,
the PC1vsPC2 view in _.png_ and _.pdf_ format and the PC1vsPC3 view in _.png_ and _.pdf_ format. 
### Full_dataset_results
This directory contains visualizations of the PCA analysis results for full dataset,
the PC1vsPC2 view in _.png_ and _.pdf_ format and the PC1vsPC3 view in _.png_ and _.pdf_ format.
### _PCAngsd_run_command.txt_
### _out_covmat.cov_
### _pca.py_
### _pca_3.py_
### _pca_out.cov_

## Relatedness
This directory contains results, used scripts and commands from the anylitic part where wolf relatedness was tested.
### _NgsRelate_output_matrix.cov_
This file contains the matrix that is the output of the NgsRelate tool.
### _NgsRelate_run_command.txt_
This text file contains the run command to calculate relatedness using the NgsRelate tool.
### _input_NgsRelate_commands.txt_
This command was used to create an input file for the relatedness analysis using the NgsRelate tool.
### _mvc_script.py_
This python script is used for minimum vertex cover approximation and it was the final step in the analytical part of determination of relatedness.
