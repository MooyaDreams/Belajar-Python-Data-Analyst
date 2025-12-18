import pandas as pd
import os

print("--- OPERASI PEMBERSIHAN DATA ---")

# 1. BACA DATA
folder_ini = os.path.dirname(os.path.abspath(__file__))
file_csv = os.path.join(folder_ini, "steam-games.csv")
df = pd.read_csv(file_csv)

# Kita intip dulu musuhnya kayak apa
print("[1] Contoh Harga Sebelum Dibersihkan:")
print(df['discounted_price'].head(10)) 

# 2. BIKIN FUNGSI PEMBERSIH (Sabun Cuci)
def cuci_harga(harga):
    # Cek dulu, kalau datanya kosong (NaN), biarin aja
    if pd.isna(harga):
        return 0.0
    
    # Ubah jadi teks dulu biar aman
    harga = str(harga)
    
    # Kalau ada kata "Free", berarti harganya 0
    if "Free" in harga:
        return 0.0
    
    # Hapus simbol aneh (₹ dan ,)
    # Hati-hati, dataset ini kayaknya pake Rupee (₹)
    harga_bersih = harga.replace("₹", "").replace(",", "")
    
    # Coba ubah jadi angka
    try:
        return float(harga_bersih)
    except:
        return 0.0 # Kalau masih error, anggap aja 0

# 3. TERAPKAN SABUN KE KOLOM HARGA
print("\nSedang menggosok data harga... 🧼")
# .apply() itu nyuruh Python: "Terapkan fungsi 'cuci_harga' ke SETIAP BARIS di kolom ini"
df['harga_angka'] = df['discounted_price'].apply(cuci_harga)

print("[2] Contoh Harga SETELAH Dibersihkan:")
print(df[['discounted_price', 'harga_angka']].head(10))

print("\n[3] Cek Statistik Harga Baru:")
print(df['harga_angka'].describe())

# 4. SIMPAN DATA BERSIH (Biar besok gak usah ngebersihin lagi)
file_bersih = os.path.join(folder_ini, "steam_bersih.csv")
df.to_csv(file_bersih, index=False)
print(f"\n✅ Data bersih disimpan ke: {file_bersih}")