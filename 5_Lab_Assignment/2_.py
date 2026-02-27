# Store prices in a tuple
prices = tuple(map(int, input("Enter prices separated by space: ").split()))

# a) Total number of items sold
print("Total items sold:", len(prices))

# b) Cheapest item price
print("Cheapest item price:", min(prices))

# c) Costliest item price
print("Costliest item price:", max(prices))

# d) Prices in ascending order
print("Prices in ascending order:", tuple(sorted(prices)))

# e) Number of costliest items sold
costliest = max(prices)
print("Number of costliest items sold:", prices.count(costliest))