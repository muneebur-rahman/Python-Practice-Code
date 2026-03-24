# 8. Write a Python function that takes a list and returns a new list with distinct
# elements from the first list.
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]

def unique_list(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result


sample = [1, 2, 3, 3, 3, 3, 4, 5]
print(f"sample list: {sample}")
result=unique_list(sample)
print(f"Unique List: {result}")