import pandas as pd
import matplotlib.pyplot as plt

# 1. Datanya sama kayak kemarin
data_toko = {
    "Hari": ["Senin", "Selasa", "Rabu", "Kamis", "Jumat"],
    "Keuntungan": [200000, 150000, 350000, 250000, 400000]
}
df = pd.DataFrame(data_toko)

# 2. PROSES VISUALISASI (Melukis)
print("Sedang menggambar grafik...")

# Tentukan sumbu X (Hari) dan Y (Keuntungan)
plt.bar(df["Hari"], df["Keuntungan"], color='skyblue')

# Kasih Judul biar jelas
plt.title("Grafik Keuntungan Mooya Mart")
plt.xlabel("Hari Operasional")
plt.ylabel("Rupiah (IDR)")

# 3. TAMPILKAN
plt.show()