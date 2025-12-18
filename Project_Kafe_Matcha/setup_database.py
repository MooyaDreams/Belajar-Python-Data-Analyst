import sqlite3

print("--- SEDANG MEMBANGUN SISTEM KAFE... 🏗️ ---")

# 1. Bikin/Konek ke Database
koneksi = sqlite3.connect("kafe_matcha.db")
cursor = koneksi.cursor()

# 2. Bikin Tabel MENU
# Kita simpan: ID, Nama, Kategori (Minuman/Makanan), Harga
cursor.execute('''
    CREATE TABLE IF NOT EXISTS menu (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nama TEXT NOT NULL,
        kategori TEXT NOT NULL,
        harga INTEGER NOT NULL
    )
''')

# 3. Bikin Tabel PESANAN
# Kita simpan: ID, Nama Pelanggan, No Meja, Menu yang dipesan, Status
cursor.execute('''
    CREATE TABLE IF NOT EXISTS pesanan (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nama_pelanggan TEXT,
        no_meja INTEGER,
        pesanan_apa TEXT,
        status TEXT DEFAULT 'Memasak'
    )
''')

# 4. ISI DATA MENU AWAL (SEEDING)
# Biar pas aplikasi dibuka, menunya gak kosong.
print("Sedang mengisi stok menu... 🍵")

# Hapus menu lama dulu (biar gak dobel kalau kode dijalankan 2x)
cursor.execute("DELETE FROM menu")

daftar_menu = [
    ('Matcha Latte Premium', 'Minuman', 25000),
    ('Sakura Tea', 'Minuman', 22000),
    ('Espresso', 'Minuman', 18000),
    ('Salmon Mentai', 'Makanan', 45000),
    ('Takoyaki', 'Makanan', 20000),
    ('Dorayaki Matcha', 'Makanan', 15000)
]

cursor.executemany("INSERT INTO menu (nama, kategori, harga) VALUES (?, ?, ?)", daftar_menu)

# 5. SIMPAN PERUBAHAN
koneksi.commit()
koneksi.close()

print("✅ DATABASE BERHASIL DIBANGUN!")
print("File 'kafe_matcha.db' sudah siap digunakan.")