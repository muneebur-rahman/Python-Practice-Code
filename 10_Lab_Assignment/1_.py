import pandas as pd

# Read CSV file
df = pd.read_csv("books.csv")

# a) Print complete report
print("\n--- Complete Book Report ---")
print(df)

# b) Books of a given author
author = input("\nEnter author name: ")
print("\nBooks by author:")
print(df[df['author'] == author])

# c) Books of a given publisher
publisher = input("\nEnter publisher name: ")
print("\nBooks by publisher:")
print(df[df['publisher'] == publisher])

# d) Cheapest and costliest book
print("\nCheapest Book:")
print(df.loc[df['price'].idxmin()])

print("\nCostliest Book:")
print(df.loc[df['price'].idxmax()])

# e) Sort by year
print("\nBooks sorted by Year:")
print(df.sort_values(by='year'))