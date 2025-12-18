import seaborn as sns
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

print("--- MEMBANGUN OTAK AI... ---")

# 1. SIAPKAN DATA
df = sns.load_dataset('titanic')

# --- DATA CLEANING (AI cuma ngerti Angka, gak ngerti Teks) ---
# Ubah Jenis Kelamin: Male = 0, Female = 1
df['sex_angka'] = df['sex'].map({'male': 0, 'female': 1})

# Isi Umur yang kosong dengan rata-rata (biar gak error)
rata_umur = df['age'].mean()
df['age'] = df['age'].fillna(rata_umur)

# Pilih Fitur (Bahan pertimbangan AI)
# Kita pakai: Kelas Tiket, Gender Angka, Umur, dan Harga Tiket
fitur = ['pclass', 'sex_angka', 'age', 'fare']
target = 'survived' # Kunci jawaban

# Bersihkan data dari yang kosong di kolom fitur
df_bersih = df[fitur + [target]].dropna()

# 2. LATIH AI (TRAINING)
X = df_bersih[fitur] # Soal Ujian
y = df_bersih[target] # Kunci Jawaban

# Panggil Model Decision Tree
model = DecisionTreeClassifier()
model.fit(X, y) # AI sedang 'belajar' menghapal pola

print("✅ AI Selesai Belajar! Sekarang saatnya prediksi...")

# 3. TES NASIB MOOYA
# Silakan ganti data ini sesuai profil kamu!
# [Kelas Tiket (1-3), Gender (0=Pria, 1=Wanita), Umur, Harga Tiket($)]
# Data Profil Kamu
data_kamu = [[1, 1, 20, 10]] # VIP, Wanita, 20th, Tiket Murah

# Bungkus jadi DataFrame biar ada NAMA KOLOMNYA (Biar AI gak ngomel)
# Pastikan nama kolom SAMA PERSIS dengan variabel 'fitur' di atas
kamu_df = pd.DataFrame(data_kamu, columns=['pclass', 'sex_angka', 'age', 'fare'])

# Prediksi pake DataFrame yang udah rapi
prediksi = model.predict(kamu_df)
peluang = model.predict_proba(kamu_df)

print("\n--- HASIL RAMALAN AI ---")
print(f"Profil Penumpang: Kelas {data_kamu[0][0]}, Gender {data_kamu[0][1]}, Umur {data_kamu[0][2]}")

if prediksi[0] == 1:
    print("🎉 HASIL: SELAMAT!")
    print(f"Keyakinan AI: {peluang[0][1]*100:.2f}%")
else:
    print("💀 HASIL: MENINGGAL...")
    print(f"Keyakinan AI: {peluang[0][0]*100:.2f}%")