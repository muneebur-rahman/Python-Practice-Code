# 10
#traversal
#user input and for loop tuple creation
t=tuple()
totalvalue=int(input("How many element u enter in tupple : "))
for i in range(totalvalue):
    val=int(input(f"Enter element {i+1} :"))
    t=t+(val,)
print(t)