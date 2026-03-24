# 9. Write a Python function that takes a number as a parameter and checks
# whether the number is prime or not.
# Note : A prime number (or a prime) is a natural number greater than 1 and
# that has no positive divisors other than 1 and itself.

def is_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


num = int(input("Enter a number: "))
if is_prime(num):
    print(num, "is a Prime number")
else:
    print(num, "is not a Prime number")