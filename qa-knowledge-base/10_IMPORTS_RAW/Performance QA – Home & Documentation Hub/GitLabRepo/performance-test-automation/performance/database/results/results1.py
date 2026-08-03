import pandas as pd

# Define file paths
file_paths = [
    'data1.csv',
    'data2.csv'
]

# Load all CSV files into a list of DataFrames 
dataframes = []
for file in file_paths:
        df = pd.read_csv(file)
        print(f"Columns in file {file}: {df.columns.tolist()}")
        dataframes.append(df)

# Check if all dataframes have the 'Name' column 
for i, df in enumerate(dataframes):
    if 'SQL' not in df.columns:
        raise KeyError(f"'SQL' column not found in file {file_paths[i]}")

# Initialize the merged DataFrame with the first DataFrame 
merged_df = dataframes[0]

# Iterate over the remaining DataFrames and merge them
for i, df in enumerate(dataframes[1:], start=1):
    # Add suffixes to columns, except 'Name'
    suffix = f'_{i}'
    df = df.rename(columns={col: f"{col}{suffix}" if col != 'SQL'
else col for col in df.columns})
    merged_df = pd.merge(merged_df, df, on='SQL')

# Calculate the average for each column
#average_columns = ['Average', 'Min', 'Max']  # Adjust this list based on your columns
average_columns = ['Samples', 'Average', 'AvgHits', '90', '95', '99', 'Min', 'Max', 'Bandwidth', 'Error']
print(f"frame column names list: {merged_df.columns.tolist()}")
for col in average_columns:
    cols_to_average = [f"{col}{suffix}" for suffix in ['', *[f'_{i}'for i in range(1, len(dataframes))]]]

    print(f'Columns to Average convert: {cols_to_average}')
 
    merged_df[f'{col}_Avg'] = merged_df[cols_to_average].mean(axis=1)

# Select relevant columns for the final output 
final_columns = ['SQL'] + [f'{col}_Avg' for col in average_columns] 
final_df = merged_df[final_columns]

# Save the final dataframe to a new CSV file 
output_file = 'combined_averages.csv'
final_df.to_csv(output_file, index=False)

print(f'Combined averages saved to {output_file}')
