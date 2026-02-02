n1=int(input("Enter First Number: "))
n2=int(input("Enter Second Number: "))
n3=int(input("Enter Third Number: "))
if n1>n2:
    if n1>n3:
        print(f"{n1} is largest")
    else:
        print(f"{n3} is largest")
elif n2>n1:
    if n2>n3:
        print(f"{n2} is largeest")
    else:
        print(f"{n3} is largeest")

