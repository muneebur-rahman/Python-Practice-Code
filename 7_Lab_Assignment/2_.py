# 2. Write a Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)

def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


sample = [8, 2, 3, 0, 7]

# Function call
result = sum_list(sample)
print("Sum:", result)
