import matplotlib.pyplot as plt

print("Menganalisis Tren Saham...")

# 1. Data (List biasa)
bulan = ["Januari", "Februari", "Maret", "April", "Mei"]
harga_saham = [5000, 5200, 4800, 6000, 7500] 
# (Ceritanya Maret turun, terus April-Mei to the moon 🚀)

# 2. GAMBAR GRAFIK GARIS (Line Chart)
# marker='o' -> Kasih titik bulet di setiap bulan biar jelas
# linestyle='-' -> Garis sambung
# color='green' -> Warna hijau (Cuan!)
plt.plot(bulan, harga_saham, marker='o', linestyle='-', color='red')
    
# 3. PERCANTIK GRAFIK (Penting buat Laporan ke Bos)
plt.title("Pergerakan Harga Saham MOOYA Corp (2025)")
plt.xlabel("Bulan")
plt.ylabel("Harga (Rp)")
plt.grid(True)  # Tambahkan garis kotak-kotak (Grid) ala software trading

# 4. TAMPILKAN
plt.show()