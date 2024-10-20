# SC0039_Exercise_HNO

This Python script reads a CSV file containing copy number variations (CNVs) from breast cancer samples, calculates the length of each segment, and outputs a new CSV file with an additional column for the segment length.

## Table of Contents
- [Description](#description)
- [Requirements](#requirements)
- [Usage](#usage)
- [Input Format](#input-format)
- [Output Format](#output-format)
- [License](#license)

## Description

The script processes a CSV file with the following columns:
- `ID`: Sample ID
- `chrom`: Chromosome
- `loc.start`: Starting point of the segment
- `loc.end`: Ending point of the segment

It adds a new column named `length`, which contains the calculated length of each segment (difference between `loc.end` and `loc.start`).

## Requirements

- Python 3.x
- No external libraries are required; the script uses only the Python standard library.

## Usage

1. Place your input CSV file (e.g., `breast_cancer_samples.csv`) in the same directory as the script.
2. Run the script using the following command:

   ```bash
   python segment_length_calculator.py

## Input format 
The input CSV file should have the following structure:

```
ID,chrom,loc.start,loc.end
Sample1,1,1000,2000
Sample2,2,1500,2500
...
```

## Output format 
The output CSV file will contain an additional length column:
```
ID,chrom,loc.start,loc.end,length
Sample1,1,1000,2000,1000
Sample2,2,1500,2500,1000
...
```

## Licence
This project is licensed under the MIT License. See the LICENSE file for details.


### How to Use This `README.md` File:
1. Copy the text above.
2. Create a new file named `README.md` in the same directory as your Python script.
3. Paste the text into the `README.md` file.
4. Customize any sections as needed, particularly the `License` section if you have specific licensing requirements.

This `README.md` provides a clear overview of your project, how to use the script, the expected input and output formats, and any requirements. Let me know if you need further modifications or additional sections!



