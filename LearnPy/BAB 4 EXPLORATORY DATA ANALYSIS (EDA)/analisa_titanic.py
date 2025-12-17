import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

print("--- ANALISIS TRAGEDI TITANIC ---")

# 1. LOAD DATASET (Langsung dari internet/library)
# Isinya: survived (0=Mati, 1=Hidup), pclass (Kelas Tiket), sex, age, fare (harga tiket)
df = sns.load_dataset('titanic')

# 2. INTIP DATA (Melihat 5 baris pertama)
print("\n[1] Contoh Data Penumpang:")
print(df.head())

# 3. STATISTIK DESKRIPTIF (Aljabar banget ini!)
# Ini bakal ngasih tau: Rata-rata umur, Harga tiket termurah/termahal, dll.
print("\n[2] Statistik Ringkas:")
print(df.describe())

# 4. JAWAB PERTANYAAN: "Siapa yang lebih banyak selamat? Pria atau Wanita?"
# Kita kelompokkan berdasarkan 'sex', lalu hitung rata-rata 'survived'
peluang_hidup = df.groupby('sex')['survived'].mean()
print("\n[3] Peluang Selamat berdasarkan Gender:")
print(peluang_hidup)
# Kalau hasilnya 0.74 artinya 74% selamat.

# --- VISUALISASI ---

# Grafik 1: Jumlah Penumpang Berdasarkan Kelas (Orang Kaya vs Biasa)
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='class', palette='viridis')
plt.title('Jumlah Penumpang per Kelas')
plt.show()

# Grafik 2: Distribusi Umur Penumpang (Histogram)
plt.figure(figsize=(6, 4))
sns.histplot(data=df, x='age', bins=20, kde=True, color='skyblue')
plt.title('Sebaran Umur Penumpang')
plt.xlabel('Umur')
plt.show()

# ... kode sebelumnya ...

print("\n[4] Analisis Kekejaman Kasta Sosial:")
# Kita lihat rata-rata selamat berdasarkan Kelas Tiket (Pclass)
# 1 = VIP, 2 = Menengah, 3 = Ekonomi
kasta_hidup = df.groupby('pclass')['survived'].mean()
print(kasta_hidup)

# Visualisasi biar dramatis
plt.figure(figsize=(6, 4))
sns.barplot(data=df, x='pclass', y='survived', palette='magma')
plt.title('Peluang Selamat Berdasarkan Kelas Tiket')
plt.ylabel('Peluang Hidup (0-1)')
plt.show()