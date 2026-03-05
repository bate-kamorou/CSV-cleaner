import pandas as pd 
import sys
import os

def clean_csv(input_file:str, output_file:str):
    try:
        # check if the input file exists
        if not os.path.exists(input_file):
            print(f"Error: The file {input_file} does not exist.")
            return
        
        # load tCSV
        df = pd.read_csv(input_file)
        print("CSV loaded successfully.")
        print("Original Data:")
        print(df.head())

        # get the info of the data
        print("\nData Info ℹ️:")   
        print(df.info())

        # get the summary statistics of the data
        print("\nSummary Statistics 📊:")
        print(df.describe())

        print("\nMissing values in each column 🕵️:")
        print(df.isnull().sum())

        # Remove duplicate rows
        df = df.drop_duplicates()
        
        # fill missing values 
        df = df.fillna("unknown")

        df.to_csv(output_file, index=False)
        print("\nData cleaned successfully. Duplicates removed and missing values filled.✅")
        print(f"\nCleaned data saved to {output_file}.")

    # error handling
    except pd.errors.EmptyDataError:
        print(f"❌ Error: The input file: {input_file} is empty.")
    except pd.errors.ParserError:
        print(f"❌ Error: The input file: {input_file} has a parsing error.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # sys.argv
    if len(sys.argv) != 3:
        print("Usage: python cleaner.py <input_file_name> <output_file_name>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    clean_csv(input_file, output_file)