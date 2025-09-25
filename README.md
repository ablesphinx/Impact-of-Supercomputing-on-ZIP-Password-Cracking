# Analysis of the Influence of Supercomputing on ZIP File Password Cracking

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

## Overview
This repository contains the complete work of a research project investigating how parallel computing and supercomputing resources impact the efficiency of brute-force attacks against encrypted ZIP files. The study compares:

- Sequential execution
- Limited-core parallelization on a personal computer
- Massive parallelization on the Marenostrum 5 supercomputer

The repository includes:

- Final research document (`docs/`)
- Python scripts for brute-force operations and combination counting (`python_codes/`)
- Experimental datasets and tables with execution times and combinations per second (`data_tables/`)
- Example ZIP files used for testing (`used_zip_files/`)

## Repository Structure

- `data_tables/` Results of password cracking tests and other tables
- `docs/ Final` Final research documents
- `python_codes/` Python scripts for experiments
- `used_zip_files/` Example ZIP files for testing

## Objectives

1. Quantify the effect of parallelization on password cracking time.
2. Identify the impact of password length and character set complexity on security.
3. Provide a practical comparison of brute-force performance across different computational environments.

## Key Findings

### Parallelization
Parallelization significantly improves brute-force performance. Although individual worker speed decreases with more workers, total throughput increases noticeably.
This demonstrates scalability, allowing faster attacks on complex passwords when using massive parallel computing resources like Marenostrum 5 (access restricted to authorized users).

### Password Length and Character Variety
- Longer passwords combining uppercase, lowercase, numbers, and symbols are significantly more resistant to brute-force attacks.
- Short passwords or those with a limited character set are more vulnerable.
- Password position in the search space matters; for example, passwords starting with '0' when using only numbers are tested first, making them easier to crack early.
- Combinations per second remained stable across different password complexities and lengths, showing predictable performance.

### Alphabet Complexity
Larger and more complex character sets (e.g., extended alphabets or non-Latin scripts) exponentially increase the number of possible combinations, making brute-force attacks much less feasible.

### ZIP Crypto Observations
  ZIP Crypto can produce **password collisions**: different passwords may derive the same internal key, causing multiple passwords to successfully decrypt the same file.
  This is due to its modified RC4 encryption and limited key space (2³² combinations). 
  Example: a file with password `aF9m` could also be decrypted by `aaaH` during brute-force testing.

### Performance Across Machines
- Personal laptop (sequential): ~8,000 combinations/second.
- Laptop (6 parallel workers): ~4,500 combinations/second per worker.
- Marenostrum 5 (75 workers): ~1,760 combinations/second per worker, but total throughput is much higher due to massive parallelization.
- Confirms that large-scale parallelization compensates for lower individual worker speed.

**Summary:** Parallelization accelerates brute-force attacks, but password length, complexity, and character set remain the most critical factors for security. ZIP Crypto’s internal key limitations can lead to multiple valid passwords for a single file, emphasizing the need for stronger encryption. All initial objectives were met, and additional insights on password collisions and parallelization efficiency were achieved.

**Future Work:** Investigate ZIP crypto vulnerabilities in-depth and explore optimized parallelization strategies to maximize brute-force efficiency.


## How to Use the Scripts

1. Download or clone the repository.
2. Configure parameters in the Python scripts (password length, character set, number of attempts, etc.).
3. Run the scripts using Python 3.6 or higher.

## Prerequisites

Only standard library modules are required:

- `zipfile`
- `itertools`
- `string`
- `multiprocessing`
- `sys`
- `datetime`
- `os`

No additional packages are needed.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
