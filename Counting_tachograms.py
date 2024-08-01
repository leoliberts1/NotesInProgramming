import pandas as pd

# Load the CSV file
df = pd.read_csv('Data_for_mapon/TECNICOS_SECURITAS.csv', delimiter=';')

# Filter the rows where 'Tacho model' is not empty or null
filtered_df = df[df['Tacho model'].notna() & (df['Tacho model'] != '')]

# Count the number of such rows
count = len(filtered_df)

print(f"Number of cars with a Tacho model: {count}")
