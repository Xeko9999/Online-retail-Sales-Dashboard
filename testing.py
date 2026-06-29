import pandas as pd

df = pd.read_csv("online_retail.csv", encoding="ISO-8859-1")

df = df[~df["InvoiceNo"].astype(str).str.startswith("C")]
df = df.dropna(subset=["CustomerID", "Description"])
df = df[df["Quantity"] > 0]
df = df[df["UnitPrice"] > 0]

df["Revenue"] = df["Quantity"] * df["UnitPrice"]

df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
df["Year"] = df["InvoiceDate"].dt.year
df["Month"] = df["InvoiceDate"].dt.month
df["Month_Name"] = df["InvoiceDate"].dt.strftime("%b")
df["Year_Month"] = df["InvoiceDate"].dt.to_period("M").astype(str)

df["Description"] = df["Description"].str.strip().str.title()
df["CustomerID"] = df["CustomerID"].astype(int)

print("Cleaned shape:", df.shape)
print("Total Revenue:", df["Revenue"].sum())
print(df.isna().sum())

df.to_excel("online_retail_clean.xlsx", index=False, engine="openpyxl")

print("Saved successfully")