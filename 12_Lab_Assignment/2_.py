import pandas as pd

# Read Excel file
df = pd.read_excel("employee.xlsx")

# a) Employees in Automotive domain
print("\nEmployees in Automotive domain:")
print(df[df['Department'] == 'Automotive'])

# b) Details by Employee ID
emp_id = int(input("\nEnter Employee ID: "))
print("\nEmployee Details:")
print(df[df['Employee ID'] == emp_id])

# c) List of Developers
print("\nList of Developers:")
print(df[df['Designation'] == 'Developer'])