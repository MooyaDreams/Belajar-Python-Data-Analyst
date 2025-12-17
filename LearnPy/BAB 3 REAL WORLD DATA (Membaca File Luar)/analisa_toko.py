import pandas as pd
import os  # Library buat ngatur alamat folder di Windows

print("--- ANALISIS DATA TOKO ---")

# --- 1. SETUP ALAMAT FILE (MANTRA ANTI NYASAR) ---
# Cari tau file python ini lagi ada di folder mana di laptop kamu
folder_ini = os.path.dirname(os.path.abspath(__file__))

# Gabungin alamat folder itu sama nama file CSV-nya
# Jadinya nanti: "D:\LearnPy\BAB 3...\transaksi.csv"
file_csv = os.path.join(folder_ini, "transaksi.csv")

print(f"Membaca file dari: {file_csv}") 
# -------------------------------------------------

# --- 2. BACA DATA ---
# Sekarang Pandas baca pake alamat lengkap, jadi gak bakal error lagi
df = pd.read_csv(file_csv)

print("\n[1] Data Transaksi Mentah:")
print(df) 

# --- 3. PROSES DATA (FEATURE ENGINEERING) ---
print("\n[2] Menghitung Total Omzet per Transaksi...")
# Bikin kolom baru 'Total_Omzet' = Jumlah x Harga
df["Total_Omzet"] = df["Jumlah"] * df["Harga_Satuan"]

# --- 4. LAPORAN AKHIR (AGREGASI) ---
# Hitung total semua uang
total_duit = df["Total_Omzet"].sum()

# Hitung penjualan per produk (dikelompokkan)
produk_terlaris = df.groupby("Produk")["Jumlah"].sum()

print("\n" + "="*30)
print("     LAPORAN KEUANGAN MOOYA MART")
print("="*30)
print(f"💰 Total Uang Masuk: Rp {total_duit:,.0f}") 
# (:,.0f itu trik biar angkanya ada koma pemisah ribuan, misal 1,000,000)

print("\n📦 Penjualan Per Produk:")
print(produk_terlaris)
print("="*30)