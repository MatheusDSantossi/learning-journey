import pandas as pd

df = pd.read_csv("dados/dataset.csv");

# print(df)

print("Which city has the biggest products sale value from the 'Office Supplies' category?")
print("------------------------")
sale_values = df[["Valor_Venda", "Categoria"]]

print(sale_values.groupby("Categoria").head())
