# 4. Write a Python program to reverse a string.
# Sample String : &quot;1234abcd&quot;
# Expected Output : &quot;dcba4321&quot;

def reverse_string(s):
    return s[::-1]


sample = "1234abcd"

output = reverse_string(sample)
print("Reversed String:", output)