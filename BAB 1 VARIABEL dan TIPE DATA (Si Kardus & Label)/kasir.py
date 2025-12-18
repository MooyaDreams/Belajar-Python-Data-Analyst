print("--- KASIR PINTAR ---")

# 1. Ini Variabel (Wadah)
nama_barang = "Indomie Goreng"
harga_satuan = 3500

# 2. Input dari user (Ingat: Input itu hasilnya selalu dianggap TEKS/STRING)
jumlah_beli = input("Mau beli berapa bungkus " + nama_barang + "? ")

# 3. KONVERSI (Penting!)
# Karena 'jumlah_beli' masih dianggap teks (misal "2"), kita harus ubah jadi ANGKA (2)
# Caranya pakai mantra: int()
jumlah_angka = int(jumlah_beli)

# 4. Proses Matematika (Aljabar)
total_bayar = harga_satuan * jumlah_angka

# 5. Tampilkan Hasil
print("Total yang harus dibayar: Rp", total_bayar)