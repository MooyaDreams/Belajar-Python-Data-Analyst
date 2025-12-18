import sqlite3
import os 

def konek_db():
    folder_ini = os.path.dirname(os.path.abspath(__file__))
    file_db = os.path.join(folder_ini, "kafe_matcha.db")
    return sqlite3.connect(file_db)

def tampilkan_menu():
    koneksi = konek_db()
    cursor = koneksi.cursor()
    
    print("\n" + "="*30)
    print(" 🍵 MENU MATCHA CAFE 🍵")
    print("="*30)
    
    cursor.execute("SELECT * FROM menu")
    semua_menu = cursor.fetchall()
    
    print(f"{'ID':<3} | {'Nama Menu':<20} | {'Harga':<10}")
    print("-" * 38)
    
    for menu in semua_menu:
        print(f"{menu[0]:<3} | {menu[1]:<20} | Rp {menu[3]:,}")
    
    print("-" * 38)
    koneksi.close()

# --- FITUR BARU: PESAN MAKANAN ---
def pesan_makanan():
    print("\n--- FORMULIR PESANAN ---")
    nama = input("Nama Pelanggan : ")
    meja = input("Nomor Meja     : ")
    
    # Kita tampilkan menu dulu biar user tau mau pilih nomor berapa
    tampilkan_menu()
    
    # Keranjang Belanja (List kosong buat nampung pesanan sementara)
    keranjang = []
    total_tagihan = 0
    
    koneksi = konek_db()
    cursor = koneksi.cursor()
    
    while True:
        pilihan = input("Pilih ID Menu (ketik '0' jika selesai): ")
        
        if pilihan == '0':
            break
        
        # Cek di Database: Menu nomor ini ada gak? Harganya berapa?
        cursor.execute("SELECT * FROM menu WHERE id = ?", (pilihan,))
        hasil = cursor.fetchone()
        
        if hasil:
            # hasil[1] = nama menu, hasil[3] = harga
            print(f"✅ {hasil[1]} masuk ke keranjang.")
            keranjang.append(hasil[1]) # Masukin nama menu ke list
            total_tagihan += hasil[3]  # Tambah harganya
        else:
            print("❌ Menu tidak ditemukan! Cek ID-nya lagi.")
            
    # Kalau keranjang gak kosong, kita simpan ke Database Pesanan
    if len(keranjang) > 0:
        # Ubah list ['Kopi', 'Roti'] jadi tulisan "Kopi, Roti"
        pesanan_str = ", ".join(keranjang) 
        
        cursor.execute("INSERT INTO pesanan (nama_pelanggan, no_meja, pesanan_apa) VALUES (?, ?, ?)", 
                       (nama, meja, pesanan_str))
        koneksi.commit()
        
        print("\n" + "="*30)
        print("STRUK PESANAN")
        print(f"Pelanggan : {nama} (Meja {meja})")
        print(f"Item      : {pesanan_str}")
        print(f"Total     : Rp {total_tagihan:,}")
        print("Status    : 🍳 Sedang Dimasak")
        print("="*30)
    else:
        print("\nKamu belum pesan apa-apa. Gak jadi makan? 😢")

    koneksi.close()

# --- FITUR BARU: CEK STATUS (DAPUR) ---
def cek_dapur():
    koneksi = konek_db()
    cursor = koneksi.cursor()
    
    print("\n--- DAFTAR ANTRIAN DAPUR ---")
    cursor.execute("SELECT * FROM pesanan")
    antrian = cursor.fetchall()
    
    for pesanan in antrian:
        # pesanan[1]=nama, pesanan[2]=meja, pesanan[3]=menu, pesanan[4]=status
        print(f"Meja {pesanan[2]} ({pesanan[1]}): {pesanan[4]} -> {pesanan[3]}")
        
    koneksi.close()

# --- PROGRAM UTAMA ---
while True:
    print("\nSELAMAT DATANG DI MATCHA CAFE SYSTEM")
    print("1. Lihat Menu")
    print("2. Pesan Makanan")
    print("3. Cek Dapur (Untuk Koki)")
    print("4. Keluar")
    
    pilihan = input("Mau ngapain? (1-4): ")
    
    if pilihan == '1':
        tampilkan_menu()
    elif pilihan == '2':
        pesan_makanan() # <--- Panggil fungsi baru
    elif pilihan == '3':
        cek_dapur()     # <--- Panggil fungsi baru
    elif pilihan == '4':
        print("Arigatou Gozaimasu! 🙏")
        break
    else:
        print("Pilihan salah!")