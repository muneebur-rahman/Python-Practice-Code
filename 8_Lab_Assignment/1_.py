# Ask user for file names
source_file = input("Enter source file name: ")
destination_file = input("Enter destination file name: ")

# Open source file in read mode
with open(source_file, 'r') as file:
    content = file.read()

# Convert content to uppercase
upper_content = content.upper()

# Write to destination file
with open(destination_file, 'w') as file:
    file.write(upper_content)

print("File copied successfully in uppercase!")