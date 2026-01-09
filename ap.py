import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("sales.csv")
print(df)
df["total"] = df["harga"] * df["jumlah"]
total_pendapatan = df["total"].sum()
print("Total Pendapatan:", total_pendapatan)
produk_terlaris = df.groupby("produk")["jumlah"].sum().sort_values(ascending=False)
print(produk_terlaris)
pendapatan_kategori = df.groupby("kategori")["total"].sum()
print(pendapatan_kategori)
produk_terlaris.plot(
    kind="bar",
    title="Produk Terlaris",
    xlabel="Produk",
    ylabel="Jumlah Terjual"
)
plt.show()
pendapatan_kategori.plot(
    kind="pie",
    autopct="%1.1f%%",
    title="Pendapatan per Kategori"
)
plt.ylabel("")
plt.show()