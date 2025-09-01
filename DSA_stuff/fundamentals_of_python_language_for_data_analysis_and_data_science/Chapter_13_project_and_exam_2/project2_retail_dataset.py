import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dados/dataset.csv");

# print(df[df["Cidade"] == "New York City"])

print("Which city has the biggest products sale value from the 'Office Supplies' category?")
print("------------------------")

office_suplies_df = df[df["Categoria"] == 'Office Supplies']

sale_values = office_suplies_df[["Valor_Venda", "Categoria", "Cidade"]]

cities_summed = sale_values.groupby("Cidade")["Valor_Venda"].sum().idxmax()

print(cities_summed)

# print(sale_values.groupby("Cidade")["Valor_Venda"].sum())

print("What's the total of sales by Order Date?")
print("OBS: Show the result using a bar chart!")
print("------------------------")

sales_by_order_date = df.groupby("Data_Pedido")["Valor_Venda"].sum()
order_date_by_date = df.groupby("Valor_Venda")["Data_Pedido"].sum()

print(sales_by_order_date.to_list())
print(order_date_by_date.to_list())

plt.bar(sales_by_order_date.to_list(), order_date_by_date.to_list())

plt.show()
