import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("dados/dataset.csv");

# print(df[df["Cidade"] == "New York City"])

print("Which city has the biggest products sale value from the 'Office Supplies' category?")
print("------------------------")

office_suplies_df = df[df["Categoria"] == 'Office Supplies']

sale_values = office_suplies_df[["Valor_Venda", "Categoria", "Cidade"]]

cities_summed = sale_values.groupby("Cidade")["Valor_Venda"].sum().idxmax()

print(cities_summed)

# print(sale_values.groupby("Cidade")["Valor_Venda"].sum())

print("What's the total of sales by Order Date -> Year?")
print("OBS: Show the result using a bar chart!")
print("------------------------")

df["Data_Pedido"] = pd.to_datetime(df["Data_Pedido"], format="mixed")
df.set_index('Data_Pedido', inplace=True)

# Month
# sales_by_order_date = df["Valor_Venda"].resample("M").max()
# Year
sales_by_order_date = df["Valor_Venda"].resample("Y").max()

# sales_by_order_date.plot(kind='bar', figsize=(10, 6))
# plt.xlabel("Date")
# plt.ylabel("Maximum Sales")
# plt.title("Maximum Sales by Date")
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

print("What's the total of sales by state?")
print("OBS: Show the result using a bar chart!")
print("------------------------")

total_of_sale_by_state = df.groupby("Estado")["Valor_Venda"].sum()

# total_of_sale_by_state.plot(kind="bar", figsize=(10, 6))
# plt.xlabel("State")
# plt.ylabel("Sales")
# plt.title("Total of sales by state")
# plt.show()

print("What's the 10 cities with the biggest total of sales?")
print("OBS: Show the result using a bar chart!")
print("------------------------")

total_sales_by_city = df.groupby("Cidade")["Valor_Venda"].sum().sort_values(ascending=False).head(10)

print(total_sales_by_city)

# total_sales_by_city.plot(kind="bar", figsize=(10, 6))
# plt.xlabel("Cities")
# plt.ylabel("Sales")
# plt.title("The 10 biggest Sales Cities")
# plt.show()

print("Which segment had the biggest Total of Sale?")
print("OBS: Show the result using a pie chart!")
print("------------------------")

# A simple function to transform the value into a percentage
def absolute_value(val):
    a = np.round(val / 100 * df.groupby("Segmento")["Valor_Venda"].sum(), 0)
    return a

biggest_total_sales_segment = df.groupby("Segmento")["Valor_Venda"].sum().sort_values(ascending=False)

biggest_total_sales_segment.plot(kind="pie", figsize=(10, 6))
# plt.pie(biggest_total_sales_segment, autopct=absolute_value)
# plt.xlabel("Segments")
# plt.legend(biggest_total_sales_segment.index.astype(str))
# plt.va
# plt.show()

print("(Baby level) What the Total of Sales by segment and Year?")
print("------------------------")

print(df)
total_sale_by_segment = df.groupby("Segmento")["Valor_Venda"].sum()
total_sale_by_year = df.groupby("Segmento")["Valor_Venda"].sum()

df["Data_Pedido"] = pd.to_datetime(df["Data_Pedido"], format="mixed")
df.set_index('Data_Pedido', inplace=True)

# Year
sales_by_order_date = df["Valor_Venda"].resample("Y").max()

fig, ax = plt.subplots()
total_sale_by_segment.plot(ax=ax)
sales_by_order_date.plot(ax=ax)

plt.show()
