# Take integers from user and store in a tuple
nums = tuple(map(int, input("Enter integers separated by space: ").split()))

# a) Total number of items
print("Total items:", len(nums))

# b) Last item
print("Last item:", nums[-1])

# c) Tuple in reverse order
print("Reverse order:", nums[::-1])

# d) Check if 5 is present
if 5 in nums:
    print("Yes")
else:
    print("No")

# e) Remove first and last items, sort remaining
new_tuple = nums[1:-1]        # remove first and last
sorted_tuple = tuple(sorted(new_tuple))
print("After removing first & last and sorting:", sorted_tuple)