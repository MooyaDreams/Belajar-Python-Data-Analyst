import pandas as pd

print("--- MENYIAPKAN DATA ---")

# 1. Kita bikin Datanya dulu (Pake Dictionary)
# Bayangkan ini kolom-kolom Excel
data_toko = {
    "Hari": ["Senin", "Selasa", "Rabu", "Kamis", "Jumat"],
    "Pelanggan": [20, 15, 35, 25, 40],
    "Keuntungan": [200000, 150000, 350000, 250000, 400000]
}

# 2. Panggil Pandas buat ubah jadi TABEL CANTIK (DataFrame)
df = pd.DataFrame(data_toko)
# 'df' adalah nama standar programmer buat 'DataFrame'

# 3. Tampilkan
print("\n=== TABEL PENJUALAN MOOYA MART ===")
print(df)

print("\n=== LAPORAN BOS ===")

# Mencari Total (Sum)
total_cuan = df["Keuntungan"].sum()
print(f"Total Keuntungan Seminggu: Rp {total_cuan}")

# Mencari Rata-rata (Mean)
rata_pelanggan = df["Pelanggan"].mean()
print(f"Rata-rata Pelanggan per Hari: {rata_pelanggan} orang")

# Mencari Rekor Tertinggi (Max)
paling_cuan = df["Keuntungan"].max()
print(f"Keuntungan Paling Tinggi: Rp {paling_cuan}")