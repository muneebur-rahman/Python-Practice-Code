import pandas as pd

# Create data
data = {
    'State': ['Maharashtra', 'Gujarat', 'Karnataka', 'Rajasthan', 'Punjab'],
    'Area': [307713, 196244, 191791, 342239, 50362],   # in sq km
    'Population': [124000000, 70000000, 68000000, 81000000, 30000000]
}

df = pd.DataFrame(data)

# a) Complete information
print("\n--- State Information ---")
print(df)

# b) State with largest area
print("\nState with Largest Area:")
print(df.loc[df['Area'].idxmax()]['State'])

# c) State with largest population
print("\nState with Largest Population:")
print(df.loc[df['Population'].idxmax()]['State'])

# d) Calculate population density
df['Density'] = df['Population'] / df['Area']

print("\n--- With Population Density ---")
print(df)

# e) State with highest density
print("\nState with Highest Population Density:")
print(df.loc[df['Density'].idxmax()]['State'])