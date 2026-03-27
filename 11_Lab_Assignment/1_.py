import pandas as pd
import matplotlib.pyplot as plt

# Read data
df = pd.read_csv("sales_data.csv")

# a) Line Plot (Total Profit)
plt.figure()
plt.plot(df['month'], df['total_profit'], marker='o')
plt.title("Total Profit per Month")
plt.xlabel("Month")
plt.ylabel("Profit")
plt.show()

# b) Multiline Plot (All products)
plt.figure()
plt.plot(df['month'], df['facecream'], label='Face Cream')
plt.plot(df['month'], df['facewash'], label='Face Wash')
plt.plot(df['month'], df['toothpaste'], label='Toothpaste')
plt.legend()
plt.title("Product Sales Data")
plt.show()

# c) Bar Chart (Face Cream & Face Wash)
x = range(len(df['month']))
plt.figure()
plt.bar(x, df['facecream'])
plt.bar(x, df['facewash'], bottom=df['facecream'])
plt.xticks(x, df['month'])
plt.title("Face Cream & Face Wash Sales")
plt.show()

# d) Pie Chart (Total yearly sales of products)
product_totals = df[['facecream','facewash','toothpaste','bathingsoap','shampoo','moisturizer']].sum()

plt.figure()
plt.pie(product_totals, labels=product_totals.index, autopct='%1.1f%%')
plt.title("Total Sales Distribution")
plt.show()