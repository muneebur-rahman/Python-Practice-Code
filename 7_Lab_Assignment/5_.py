# 5. Write a Python function to calculate the factorial of a number (a non-
# negative integer). The function accepts the number as an argument.

def calculate_fact(n):
    fact=1
    if n<0:
        return "Factorial not defined for negative numbers"
    for num in range(1,n+1):
        fact*=num
    return fact


number=int(input("Enter a Number: "))

result=calculate_fact(number)
print(f"Factorial of {number} is: ",result)