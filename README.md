# Analysis of the Influence of Supercomputing on ZIP File Password Cracking

## Overview

This repository contains the complete work for a research project investigating the impact of parallel computing and supercomputing resources on the efficiency of brute-force attacks against encrypted ZIP files. The study compares sequential execution, limited-core parallelization on a personal computer, and massive parallelization on the Marenostrum 5 supercomputer.  

The repository includes:  
- The final research document.  
- Python source code for brute-force operations and combination counting.  
- Experimental datasets and tables detailing execution times and combinations per second.  
- Supporting figures and charts used in the analysis.

  ## Repository Structure
The repository is organized as follows:

- **`data_tables/`**: Contains all tables with results of password cracking tests, including variations by password length and character sets.
- **`docs/`**: Includes reports and documents detailing the methodology, theoretical background, and analysis of results.
- **`python_codes/`**: Python scripts used to perform the password cracking simulations and generate the tables.
- **`used_zip_files/`**: Example ZIP files used for testing the scripts.

## Objectives

The main objectives of this research are:  
1. Quantify the effect of parallelization on the time required to crack passwords.  
2. Identify the impact of password length and character set complexity on security.  
3. Provide a practical comparison of brute-force performance across different computational environments.  

## Methodology

- Brute-force attacks were performed on ZIP files with passwords of lengths 4, 5, and 6 characters using different character sets: lowercase, lowercase + uppercase, letters + numbers, and letters + numbers + symbols.  
- Custom Python scripts were used to implement both sequential and parallel brute-force attacks.  
- Execution times and combinations processed per second were recorded and analyzed. 

## How to Use the Scripts
1. Download or copy the Python scripts from the `python_codes/` folder.
2. Configure any parameters you want directly in the code (e.g., password length, character set, number of attempts).
3. Run the script using Python.   
