import pandas as pd
import matplotlib.pyplot as plt
import os

print("--- VISUALISASI DATA TOKO ---")

# 1. SETUP PATH (Anti Nyasar)
folder_ini = os.path.dirname(os.path.abspath(__file__))
file_csv = os.path.join(folder_ini, "transaksi.csv")

# 2. BACA DATA
df = pd.read_csv(file_csv)

# --- BAGIAN PENTING (DATA CLEANING) ---
# Kolom 'Tanggal' di CSV itu masih dianggap Teks ("2025-01-01")
# Kita harus ubah jadi Object Tanggal biar Python ngerti urutan waktu
df["Tanggal"] = pd.to_datetime(df["Tanggal"])

# Kita hitung dulu Omzet per baris
df["Omzet"] = df["Jumlah"] * df["Harga_Satuan"]

# 3. AGREGASI (Penyatuan Data)
# Karena di tanggal 01 ada 2 transaksi (Kopi & Roti), kita harus GABUNG (Sum)
# biar grafiknya per hari, bukan per transaksi.
data_harian = df.groupby("Tanggal")["Omzet"].sum().reset_index()

print("Data Siap Plot:")
print(data_harian)

# 4. GAMBAR GRAFIK
plt.figure(figsize=(10, 6)) # Mengatur ukuran gambar (biar lebar)

# Sumbu X = Tanggal, Sumbu Y = Omzet
plt.plot(data_harian["Tanggal"], data_harian["Omzet"], marker='o', color='blue', linewidth=2)

plt.title("Tren Omzet Harian Mooya Mart", fontsize=16)
plt.xlabel("Tanggal")
plt.ylabel("Omzet (Rp)")
plt.grid(True) # Garis bantu kotak-kotak

# Format angka di sumbu Y biar gak muncul notasi ilmiah (le+5 dll)
plt.ticklabel_format(style='plain', axis='y')

# Simpan dan Tampilkan
plt.savefig(os.path.join(folder_ini, "grafik_omzet_harian.png"))
plt.show()