import sqlite3
import pandas as pd

# 1. Konek ke Database (Kalau filenya belum ada, otomatis dibikinin)
koneksi = sqlite3.connect("toko_mooya.db")

# 2. Bikin Tabel 'Produk' (Pura-puranya ini database beneran)
koneksi.execute('''
    CREATE TABLE IF NOT EXISTS produk (
        id INTEGER PRIMARY KEY,
        nama_barang TEXT,
        kategori TEXT,
        harga INTEGER
    )
''')

# 3. Masukin Data (Kita isi gudangnya)
# Biar gak error pas dijalanin berulang, kita hapus dulu isinya sebelum isi baru
koneksi.execute("DELETE FROM produk") 
data_barang = [
    (1, 'Laptop Gaming', 'Elektronik', 15000000),
    (2, 'Mouse Wireless', 'Elektronik', 300000),
    (3, 'Kopi Susu', 'Makanan', 20000),
    (4, 'Keyboard Mekanik', 'Elektronik', 800000),
    (5, 'Roti Bakar', 'Makanan', 15000)
]
koneksi.executemany("INSERT INTO produk VALUES (?, ?, ?, ?)", data_barang)
koneksi.commit()

print("✅ Database Gudang Toko Berhasil Dibuat!")

# --- INI BAGIAN SQL-NYA ---

print("\n[ TANTANGAN 1: Ambil semua barang Elektronik ]")
# SQL Mantra: Cari semua (*) dari tabel produk yang kategorinya Elektronik
# query = "SELECT * FROM produk WHERE kategori = 'Elektronik'"

# SQL Mantra: Kalau kamu mau "Barang Elektronik" DAN "Murah", di SQL kita pake kata sakti AND.
query = "SELECT * FROM produk WHERE kategori = 'Elektronik' AND harga < 1000000"

# Kita pake Pandas buat nampilin hasil SQL-nya biar rapi
hasil = pd.read_sql_query(query, koneksi)
print(hasil)

print("\n[ TANTANGAN 2: Cari barang yang harganya di bawah 1 Juta ]")
query_murah = "SELECT nama_barang, harga FROM produk WHERE harga > 1000000"
hasil_murah = pd.read_sql_query(query_murah, koneksi)
print(hasil_murah)

koneksi.close()