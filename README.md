# Analysis of the Influence of Supercomputing on ZIP File Password Cracking

## Overview

This repository contains the complete work for a research project investigating the impact of parallel computing and supercomputing resources on the efficiency of brute-force attacks against encrypted ZIP files. The study compares sequential execution, limited-core parallelization on a personal computer, and massive parallelization on the Marenostrum 5 supercomputer.  

The repository includes:  
- The final research document.  
- Python source code for brute-force operations and combination counting.  
- Experimental datasets and tables detailing execution times and combinations per second.  
- Supporting figures and charts used in the analysis.

To see the final document of the investigation, go to the docs folder.

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

## Conclusions
From the conducted experiments, several conclusions can be drawn from both a technical and cybersecurity perspective.

  #### Parallelization: 
The tests confirmed that parallelization significantly improves brute-force performance. While individual worker speed decreases, the total throughput increases noticeably with more workers. This demonstrates that such a strategy is scalable and allows faster attacks on complex passwords when access to computers with massive parallelization capacity is available. This result fulfills the objective of analyzing the impact of parallelization on decryption time. It is important to note that access to supercomputers like Marenostrum is currently restricted to authorized users, so malicious use is not a real threat to ordinary users’ password security.

  #### Password length and character variety: 
The results also confirm the importance of password length and the diversity of characters. Longer passwords combining uppercase, lowercase, numbers, and symbols are much more resistant to brute-force attacks, while short passwords or those based on a limited set of characters are much more vulnerable. Additionally, as the results show, the position of a password within the set of possible passwords during testing is relevant; for example, when using only numbers, passwords starting with 0 are weaker since the program tests these first. This confirms the objective of identifying which variables most influence password security.

  #### Alphabet complexity: 
The tests highlighted the importance of the character set used. Larger and more complex sets, such as those in languages with extended alphabets or character systems like Japanese, exponentially increase the number of possible combinations, making brute-force attacks much less feasible.

In summary, parallelization can significantly accelerate brute-force attacks, but factors such as length, complexity, and character set remain the most decisive for ensuring password security. These findings fulfill all the initial objectives of the study while also extending and deepening them.

As future work, further analysis could explore the vulnerability of ZIP crypto encryption and optimal parallelization strategies to maximize brute-force efficiency.

## How to Use the Scripts
1. Download or copy the Python scripts from the `python_codes/` folder.
2. Configure any parameters you want directly in the code (e.g., password length, character set, number of attempts).
3. Run the script using Python.   

## Prerequisites

- Python 3.6 or higher

No external Python libraries are required; all dependencies are from the standard library:
- zipfile
- itertools
- string
- multiprocessing
- sys
- datetime
- os

You do not need to install any additional packages to run the provided scripts.
