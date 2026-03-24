# 7. Write a Python function that accepts a string and counts the number of
# upper and lower case letters.
# Sample String : &#39;The quick Brow Fox&#39;
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12

def count_case(s):
    upper = 0
    lower = 0

    for char in s:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1

    print("No. of Upper case characters :", upper)
    print("No. of Lower case Characters :", lower)

# Sample String
sample = "The quick Brow Fox"

# Function call
count_case(sample)