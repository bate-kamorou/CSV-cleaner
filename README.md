# CSV Cleaner Utility

A simple Python command-line tool to clean CSV files.

## Features

- Removes duplicate rows
- Fills missing values
- Handles basic errors
- Saves cleaned CSV file

## Installation

Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### create a virtual environment

```bash
    python -m venv venv
```

### Then, install the required dependencies:

``` bash
    pip install pandas
```

## Usage

``` bash
    python cleaner.py input.csv output.csv
```

### Example

``` bash
    python cleaner.py sample.csv cleaned_sample.csv
```

This will read `sample.csv`, clean the data, and save the cleaned version as `cleaned_sample.csv`.
