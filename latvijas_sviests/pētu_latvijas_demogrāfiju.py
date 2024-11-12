import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# Load and clean the data
df = pd.read_csv("IRE040_20241105-180817.csv", delimiter=";")
for year in df.columns[2:]:
    df[year] = pd.to_numeric(df[year], errors="coerce")
df_long = pd.melt(df, id_vars=['Tautība', 'Vecuma grupa'], var_name='Gads', value_name='Populācija')
df_long = df_long[(df_long["Vecuma grupa"] != "65–69 gadi") &
                  (df_long["Vecuma grupa"] != "70–74 gadi") &
                  (df_long["Vecuma grupa"] != "75–79 gadi") &
                  (df_long["Vecuma grupa"] != "80–84 gadi") &
                  (df_long["Vecuma grupa"] != "85 gadi un vairāk") &
                  (df_long["Vecuma grupa"] != "60–64 gadi")]

# Filter data for general population (Pavisam) and for Latvieši and Krievi
df_general = df_long[df_long["Tautība"] == "Pavisam"]
df_latviesi = df_long[df_long["Tautība"] == "Latvieši"]
df_krievi = df_long[df_long["Tautība"] == "Krievi"]

# Merge general population data with Latvieši and Krievi on 'Vecuma grupa' and 'Gads'
df_latviesi = df_latviesi.merge(df_general, on=['Vecuma grupa', 'Gads'], suffixes=('_latviesi', '_total'))
df_krievi = df_krievi.merge(df_general, on=['Vecuma grupa', 'Gads'], suffixes=('_krievi', '_total'))

# Calculate proportion of Latvieši and Krievi relative to the total population
df_latviesi['Proportion'] = df_latviesi['Populācija_latviesi'] / df_latviesi['Populācija_total']
df_krievi['Proportion'] = df_krievi['Populācija_krievi'] / df_krievi['Populācija_total']

# Select relevant columns for clarity
df_latviesi = df_latviesi[['Vecuma grupa', 'Gads', 'Populācija_latviesi', 'Populācija_total', 'Proportion']]
df_krievi = df_krievi[['Vecuma grupa', 'Gads', 'Populācija_krievi', 'Populācija_total', 'Proportion']]

# Display a sample of the results
print("Latvieši Proportion in General Population by Age Group and Year:")
print(df_latviesi.head())
print("\nKrievi Proportion in General Population by Age Group and Year:")
print(df_krievi.head())
# Plot for Latvieši
plt.figure(figsize=(14, 8))
for age_group in df_latviesi["Vecuma grupa"].unique():
    age_group_data = df_latviesi[df_latviesi["Vecuma grupa"] == age_group]
    plt.plot(age_group_data["Gads"], age_group_data["Proportion"], label=f'Latvieši {age_group}')
    # Adding text label at the end of each line
    plt.text(age_group_data["Gads"].iloc[-1], age_group_data["Proportion"].iloc[-1],
             f'{age_group}', verticalalignment='center')

# Customize the Latvieši plot
plt.title("Proportion of Latvieši in General Population by Age Group Over Time")
plt.xlabel("Gads")
plt.ylabel("Proportion of Population")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.show()

# Plot for Krievi
plt.figure(figsize=(14, 8))
for age_group in df_krievi["Vecuma grupa"].unique():
    age_group_data = df_krievi[df_krievi["Vecuma grupa"] == age_group]
    plt.plot(age_group_data["Gads"], age_group_data["Proportion"], label=f'Krievi {age_group}', linestyle='--')
    # Adding text label at the end of each line
    plt.text(age_group_data["Gads"].iloc[-1], age_group_data["Proportion"].iloc[-1],
             f'{age_group}', verticalalignment='center')

# Customize the Krievi plot
plt.title("Proportion of Krievi in General Population by Age Group Over Time")
plt.xlabel("Gads")
plt.ylabel("Proportion of Population")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.show()