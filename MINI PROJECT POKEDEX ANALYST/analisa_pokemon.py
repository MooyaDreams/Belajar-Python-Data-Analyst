# PERBAIKAN 1: Tambahkan .pyplot
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
import os

print("--- ANALISIS KEKUATAN POKEMON ---")

# 2. Setup Lokasi File
folder_ini = os.path.dirname(os.path.abspath(__file__))
file_csv = os.path.join(folder_ini, "pokemon.csv")

# 3. Baca File CSV
df = pd.read_csv(file_csv)

print("\n[1] Data Pokemon:")
print(df)

# --- TANTANGAN ANALISIS ---

# 4. Siapa Pokemon dengan Attack Tertinggi? 
# PERBAIKAN 2: Tambahkan kurung () biar dihitung
max_attack = df['Attack'].max() 
print(f"\nAttack Paling Tinggi: {max_attack}")

# 5. Cari Rata-rata Speed
rata_speed = df['Speed'].mean()
print(f"Rata-rata Kecepatan: {rata_speed}")

# 6. Bandingkan: Pokemon Legendary vs Biasa
kekuatan_legend = df.groupby('Legendary')['Attack'].mean()
print("\nPerbandingan Kekuatan Legend:")
print(kekuatan_legend)

# --- TANTANGAN GAMBAR ---

print("\nSedang menggambar grafik...")

plt.figure(figsize=(10, 5)) 
# PERBAIKAN 3: Ganti 'Nama Pokemon' jadi 'Nama' (Sesuai header CSV)
sns.barplot(data=df, x='Nama', y='Defense', hue='Nama', legend=False, palette='coolwarm')
plt.title("Perbandingan Pertahanan (Defense) Pokemon")
plt.show()