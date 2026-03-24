# 10. Write a Python program to print the even numbers from a given list.
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result : [2, 4, 6, 8]

def even_numbers(lst):
    result = []
    for num in lst:
        if num % 2 == 0:
            result.append(num)
    return result


sample = [1, 2, 3, 4, 5, 6, 7, 8, 9]

result=even_numbers(sample)
print("Even Numbers:", result)