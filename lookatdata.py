import pandas as pd
import numpy as np

# Read the CSV file
data = pd.read_csv('testdata.csv')

# Display the number of rows and columns in the dataset
print('Number of rows: ' + str(data.shape[0]))
print('Number of columns: ' + str(data.shape[1]))

# Display the column names and data types
print('\nColumn names and data types:')
print(data.dtypes)

# Display basic statistical data for numeric columns
numeric_data = data.select_dtypes(include=[np.number])
print('\nBasic statistical data for numeric columns:')
print(numeric_data.describe())

# Describe non-numeric fields
non_numeric_data = data.select_dtypes(exclude=[np.number])
for col in non_numeric_data.columns:
    print('\n' + col)
    value_counts = non_numeric_data[col].value_counts()
    percent_counts = value_counts / len(non_numeric_data) * 100
    print(pd.concat([value_counts, percent_counts], axis=1, keys=['Count', 'Percentage']))