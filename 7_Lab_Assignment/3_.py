# 3. Write a Python function to multiply all the numbers in a list.
# Sample List : (8, 2, 3, -1, 7)
# Expected Output : -336

def multiply_list(numbers):
    total=1
    for num in numbers:
        total*=num
    return total

sample= [8, 2, 3, -1, 7]
result=multiply_list(sample)
print("Result: ",result)