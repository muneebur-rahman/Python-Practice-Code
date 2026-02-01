n=int(input("Enter a Number: "))
temp=n
sum=0
while temp>0:
    digit=temp%10
    sum=sum+digit*digit*digit
    temp=temp//10
if sum==n:
    print(f"{n} is an Armstrong Number")
else:
    print(f"{n} is not an Armstrong Number")