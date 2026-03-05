import pandas as pd 

def clean_csv(input_file:str, output_file:str):
    try:
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
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    input_file = "sample.csv"
    output_file = "cleaned_data.csv"
    clean_csv(input_file, output_file)