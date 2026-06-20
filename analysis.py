import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("../data/ecommerce_sales.csv")
print(df.head())

df['Revenue'] = df['Quantity'] * df['Price']
print("Total Revenue:", df['Revenue'].sum())

top_products = df.groupby('Product')['Revenue'].sum().sort_values(ascending=False)
print("\nTop Products:\n", top_products)

category_revenue = df.groupby('Category')['Revenue'].sum().sort_values(ascending=False)
print("\nCategory Revenue:\n", category_revenue)

category_revenue.plot(kind='bar', title='Revenue by Category')
plt.ylabel('Revenue')
plt.tight_layout()
plt.show()