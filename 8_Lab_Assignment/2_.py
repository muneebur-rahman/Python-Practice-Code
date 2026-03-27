# Ask user for file names
source_file = input("Enter source Python file: ")
destination_file = input("Enter destination file: ")

# Read source file and remove comments
with open(source_file, 'r') as file:
    lines = file.readlines()

new_lines = []

for line in lines:
    # Remove full-line comments
    if not line.strip().startswith("#"):
        # Remove inline comments
        if "#" in line:
            line = line.split("#")[0]
        new_lines.append(line)

# Write cleaned content to destination file
with open(destination_file, 'w') as file:
    file.writelines(new_lines)

# Print both files
print("\n--- Source File Content ---")
with open(source_file, 'r') as file:
    print(file.read())

print("\n--- Destination File Content (Without Comments) ---")
with open(destination_file, 'r') as file:
    print(file.read())

print("\nFile copied without comments successfully!")