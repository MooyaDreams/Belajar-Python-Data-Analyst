import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

print("--- MENGUNGKAP RAHASIA STEAM ---")

# 1. SETUP & BACA FILE BERSIH
folder_ini = os.path.dirname(os.path.abspath(__file__))
file_csv = os.path.join(folder_ini, "steam_bersih.csv")

# Cek dulu filenya ada gak (Jaga-jaga)
if not os.path.exists(file_csv):
    print("❌ Eits, file 'steam_bersih.csv' belum ada!")
    print("Jalankan dulu file 'bersihin_steam.py' ya.")
    exit()

df = pd.read_csv(file_csv)

# 2. MENCARI GAME SULTAN
print("\n[1] MENCARI GAME SULTAN (TERMAHAL)")
game_sultan = df[df['harga_angka'] == df['harga_angka'].max()]
print(game_sultan[['title', 'harga_angka', 'genres']])

# 3. DATA VISUALISASI PIE CHART
def cek_gratis(harga):
    if harga == 0:
        return "Gratis (Free)"
    else:
        return "Berbayar (Paid)"

df['Status'] = df['harga_angka'].apply(cek_gratis)
jumlah_game = df['Status'].value_counts()

print("\n[2] PERBANDINGAN JUMLAH GAME")
print(jumlah_game)

# 4. GAMBAR DIAGRAM KUE (PIE CHART)
print("\nSedang menggambar diagram kue... 🍰")
plt.figure(figsize=(6, 6))
plt.pie(jumlah_game, labels=jumlah_game.index, autopct='%1.1f%%', colors=['skyblue', 'salmon'])
plt.title("Berapa Persen Game Gratis di Steam?")

# --- PERBAIKAN: SAVE DULU BARU SHOW ---
file_pie = os.path.join(folder_ini, "steam_pie_chart.png")
plt.savefig(file_pie) 
print(f"✅ Gambar Pie Chart disimpan ke: {file_pie}")

plt.show() # Ini akan menghapus kanvas setelah ditampilkan
# --------------------------------------

# 5. GAMBAR HISTOGRAM
print("\nSedang menggambar histogram... 📊")
df_wajar = df[(df['harga_angka'] > 0) & (df['harga_angka'] < 5000)]

plt.figure(figsize=(10, 5))
sns.histplot(data=df_wajar, x='harga_angka', bins=30, color='green', kde=True)
plt.title("Sebaran Harga Game (Range 0 - 5000 Rupee)")
plt.xlabel("Harga (Rupee)")

# --- PERBAIKAN: SAVE DULU BARU SHOW ---
file_hist = os.path.join(folder_ini, "steam_histogram.png")
plt.savefig(file_hist)
print(f"✅ Gambar Histogram disimpan ke: {file_hist}")

plt.show()
# --------------------------------------