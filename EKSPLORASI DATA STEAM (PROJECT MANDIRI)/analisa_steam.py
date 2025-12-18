import pandas as pd
import os

print("--- ANALISA DATA STEAM GAMES ---")

# 1. SETUP LOKASI FILE (Jurus Anti-Nyasar)
folder_ini = os.path.dirname(os.path.abspath(__file__))
file_csv = os.path.join(folder_ini, "steam-games.csv")

# 2. BACA DATA
# Hati-hati, file asli biasanya ribet encoding-nya. 
# Kita coba cara standar dulu.
print("Sedang membaca file... (Mungkin agak lama karena datanya banyak)")
df = pd.read_csv(file_csv)

# 3. KENALAN SAMA DATA
print("\n[1] 5 Data Teratas:")
print(df.head())

print("\n[2] Info Kolom (Tipe Data & Kekosongan):")
print(df.info())

print("\n[3] Daftar Nama Kolom:")
print(df.columns)