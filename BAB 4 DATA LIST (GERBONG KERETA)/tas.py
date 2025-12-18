
print("--- TAS PETUALANG ---")

# 1. Membuat List (Isi awal)
# Index (Nomor Urut):   0          1         2
isi_tas =           ["Pedang", "Perisai", "Potion"]

# 2. Menampilkan isi (Cetak semua)
print("Isi tas kamu sekarang:", isi_tas)

# 3. Mengambil satu barang (PENTING: Komputer mulai hitung dari 0!)
print("Senjata utama:", isi_tas[0])  # Mengambil "Pedang"
print("Barang kedua:", isi_tas[1])   # Mengambil "Perisai"

# 4. Menambah Barang Baru (Append)
print("...Menemukan Peta Harta Karun!...")
isi_tas.append("Peta") # Mantra .append() buat nambah ke belakang
print("Isi tas baru:", isi_tas)

# 5. Mengubah Barang
print("...Potion diminum, ganti jadi Botol Kosong...")
isi_tas[2] = "Botol Kosong"
print("Isi tas update:", isi_tas)