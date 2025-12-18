import streamlit as st
import sqlite3
import pandas as pd
import os

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Matcha Cafe System", page_icon="🍵")

# --- 2. FUNGSI KONEKSI DATABASE ---
def konek_db():
    # Biar gak nyasar, kita pake alamat lengkap filenya
    folder_ini = os.path.dirname(os.path.abspath(__file__))
    file_db = os.path.join(folder_ini, "kafe_matcha.db")
    return sqlite3.connect(file_db)

# --- 3. JUDUL & SIDEBAR (NAVIGASI) ---
st.title("🍵 Matcha Cafe System")
st.sidebar.header("Navigasi")
menu_navigasi = st.sidebar.radio("Pilih Halaman:", ["Pesan Makanan", "Dapur (Koki)"])

# ==========================================
# HALAMAN 1: PESAN MAKANAN (UNTUK PELANGGAN)
# ==========================================
if menu_navigasi == "Pesan Makanan":
    st.header("Formulir Pesanan")
    st.write("Silakan pilih menu favoritmu di sini!")
    
    # A. Input Data Diri (Kiri Kanan biar rapi)
    col1, col2 = st.columns(2)
    with col1:
        nama = st.text_input("Nama Pelanggan")
    with col2:
        meja = st.number_input("Nomor Meja", min_value=1, value=1)

    # B. Ambil Menu dari Database
    koneksi = konek_db()
    cursor = koneksi.cursor()
    cursor.execute("SELECT * FROM menu")
    data_menu = cursor.fetchall() # Isinya list menu
    koneksi.close()

    # C. Bikin Daftar Menu biar bisa dipilih
    # Kita ubah formatnya jadi: "Matcha Latte (Rp 25,000)"
    list_menu_tampil = []
    kamus_harga = {} # Ini buat nyimpen harga di memori ("Matcha Latte" -> 25000)
    
    for item in data_menu:
        # item[1] = nama, item[3] = harga
        label = f"{item[1]} (Rp {item[3]:,})"
        list_menu_tampil.append(label)
        kamus_harga[label] = item[3]

    # D. Input Pesanan (Pake Multiselect biar gampang)
    pesanan_user = st.multiselect("Mau pesan apa aja?", list_menu_tampil)

    # E. Hitung Total & Tombol Kirim
    if len(pesanan_user) > 0:
        total_harga = 0
        for item_dipilih in pesanan_user:
            total_harga += kamus_harga[item_dipilih]
        
        st.info(f"💰 Total Harga: Rp {total_harga:,}")
        
        # Tombol Kirim
        if st.button("Kirim Pesanan 🚀"):
            if nama == "":
                st.error("Eits, isi nama dulu dong!")
            else:
                # SIMPAN KE DATABASE (Jantungnya aplikasi)
                koneksi = konek_db()
                pesanan_str = ", ".join(pesanan_user) # Jadiin satu kalimat panjang
                koneksi.execute("INSERT INTO pesanan (nama_pelanggan, no_meja, pesanan_apa) VALUES (?, ?, ?)", 
                               (nama, meja, pesanan_str))
                koneksi.commit()
                koneksi.close()
                
                st.success(f"✅ Pesanan Kak {nama} di Meja {meja} berhasil dikirim!")
                st.balloons() # Balon lagiii! 🎈

    # F. Tampilkan Menu Lengkap di Bawah (Pake Pandas biar tabelnya cantik)
    st.divider()
    st.subheader("Daftar Menu Lengkap")
    koneksi = konek_db()
    df_menu = pd.read_sql_query("SELECT nama as 'Menu', kategori as 'Jenis', harga as 'Harga' FROM menu", koneksi)
    st.table(df_menu)
    koneksi.close()

# ==========================================
# HALAMAN 2: DAPUR (UNTUK KOKI)
# ==========================================
elif menu_navigasi == "Dapur (Koki)":
    st.header("👨‍🍳 Antrian Dapur")
    st.write("Pantau pesanan yang masuk secara Real-Time.")
    
    if st.button("Refresh Data 🔄"):
        st.rerun()

    # Ambil semua pesanan dari database
    koneksi = konek_db()
    # Kita ambil yang terbaru paling atas (ORDER BY id DESC)
    df_pesanan = pd.read_sql_query("SELECT * FROM pesanan ORDER BY id DESC", koneksi)
    koneksi.close()
    
    # Tampilkan Dataframenya (Excel interaktif)
    st.dataframe(df_pesanan, use_container_width=True)