# 6. Write a Python function to check whether a number falls within a given
# range.
def check_range(num, start, end):
    if start <= num <= end:
        return True
    else:
        return False


print(check_range(5, 1, 10))   # True
print(check_range(15, 1, 10))  # False