import streamlit as st
import sqlite3
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
from datetime import datetime
from sklearn.linear_model import LinearRegression 
import plotly.graph_objects as go # Library grafik interaktif (Kita pakai ini sekarang!)

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Matcha Cafe System", page_icon="🍵")

# --- 2. FUNGSI KONEKSI DATABASE (HYBRID) ---

# A. KONEKSI KE SQLITE (Khusus buat ambil Daftar Menu)
def konek_sqlite():
    folder_ini = os.path.dirname(os.path.abspath(__file__))
    file_db = os.path.join(folder_ini, "kafe_matcha.db")
    return sqlite3.connect(file_db)

# B. KONEKSI KE GOOGLE SHEETS (Khusus buat Simpan Pesanan)
def konek_gsheet():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    
    # Cek apakah kita di Laptop (Local) atau Cloud
    if os.path.exists("secrets_kafe.json"):
        creds = ServiceAccountCredentials.from_json_keyfile_name("secrets_kafe.json", scope)
    else:
        # Ini buat nanti pas di Streamlit Cloud
        info_json = st.secrets["gcp_service_account"]
        creds = ServiceAccountCredentials.from_json_keyfile_dict(info_json, scope)

    client = gspread.authorize(creds)
    sheet = client.open("Database Kafe Matcha").sheet1 
    return sheet

# --- 3. UI WEBSITE ---
st.title("🍵 Matcha Cafe System")
st.sidebar.header("Navigasi")
menu_navigasi = st.sidebar.radio("Pilih Halaman:", ["Pesan Makanan", "Dapur (Koki)", "Peramal Cuan 🔮"])

# ==========================================
# HALAMAN 1: PESAN MAKANAN
# ==========================================
if menu_navigasi == "Pesan Makanan":
    st.header("Formulir Pesanan")
    st.write("Silakan pilih menu favoritmu di sini!")
    
    col1, col2 = st.columns(2)
    with col1:
        nama = st.text_input("Nama Pelanggan")
    with col2:
        meja = st.number_input("Nomor Meja", min_value=1, value=1)

    # --- BAGIAN MENU (AMBIL DARI SQLITE) ---
    try:
        koneksi_sql = konek_sqlite()
        cursor = koneksi_sql.cursor()
        cursor.execute("SELECT * FROM menu")
        data_menu = cursor.fetchall()
        koneksi_sql.close()
        
        # Bikin list menu
        list_menu_tampil = []
        kamus_harga = {}
        for item in data_menu:
            label = f"{item[1]} (Rp {item[3]:,})"
            list_menu_tampil.append(label)
            kamus_harga[label] = item[3]

        # Input Pesanan
        pesanan_user = st.multiselect("Mau pesan apa aja?", list_menu_tampil)

        # Hitung Total & Kirim
        if len(pesanan_user) > 0:
            total_harga = 0
            for item_dipilih in pesanan_user:
                total_harga += kamus_harga[item_dipilih]
            
            st.info(f"💰 Total Harga: Rp {total_harga:,}")
            
            if st.button("Kirim Pesanan 🚀"):
                if nama == "":
                    st.error("Eits, isi nama dulu dong!")
                else:
                    # --- SIMPAN KE GOOGLE SHEETS ---
                    try:
                        sheet = konek_gsheet()
                        pesanan_str = ", ".join(pesanan_user)
                        waktu_skrg = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        
                        sheet.append_row([nama, meja, pesanan_str, total_harga, waktu_skrg])
                        
                        st.success(f"✅ Pesanan Kak {nama} berhasil dikirim ke Cloud! ☁️")
                        st.balloons()
                        
                    except Exception as e:
                        st.error(f"Gagal konek ke Google Sheet: {e}")

    except Exception as e:
        st.error(f"Gagal ambil menu dari database: {e}")

    # Tampilkan Menu Lengkap
    st.divider()
    st.subheader("Daftar Menu Lengkap")
    koneksi_sql = konek_sqlite()
    df_menu = pd.read_sql_query("SELECT nama as 'Menu', kategori as 'Jenis', harga as 'Harga' FROM menu", koneksi_sql)
    st.table(df_menu)
    koneksi_sql.close()

# ==========================================
# HALAMAN 2: DAPUR (UNTUK KOKI)
# ==========================================
elif menu_navigasi == "Dapur (Koki)":
    st.header("👨‍🍳 Antrian Dapur")
    st.write("Pantau pesanan yang masuk secara Real-Time.")
    
    if st.button("Refresh Data 🔄"):
        st.rerun()

    try:
        sheet = konek_gsheet()
        data_semua = sheet.get_all_records()
        
        if len(data_semua) == 0:
            st.warning("Belum ada pesanan masuk.")
        else:
            df_pesanan = pd.DataFrame(data_semua)
            df_pesanan = df_pesanan.iloc[::-1] 
            st.dataframe(df_pesanan, use_container_width=True)
            
    except Exception as e:
        st.error(f"Error memuat data dapur: {e}")

# ==========================================
# HALAMAN 3: PERAMAL CUAN (MACHINE LEARNING)
# ==========================================
elif menu_navigasi == "Peramal Cuan 🔮":
    st.header("🔮 Peramal Masa Depan Kafe")
    st.write("Gunakan Machine Learning untuk memprediksi penjualan berdasarkan cuaca!")

    # 1. DATA HISTORIS
    data_latih = {
        'Suhu': [26, 30, 32, 24, 35, 28, 22, 33, 29, 27],
        'Jual': [40, 65, 75, 35, 90, 50, 25, 85, 60, 45]
    }
    df_latih = pd.DataFrame(data_latih)

    with st.expander("Lihat Data Historis"):
        st.dataframe(df_latih)

    # 2. TRAINING MODEL
    model = LinearRegression()
    model.fit(df_latih[['Suhu']], df_latih['Jual'])

    # 3. INPUT USER
    st.divider()
    st.subheader("Cek Prediksi Besok")
    suhu_input = st.slider("Perkiraan Suhu Besok (°C):", 20, 40, 30)

    # 4. PREDIKSI & VISUALISASI
    if st.button("Ramal Sekarang! 🎩"):
        input_df = pd.DataFrame({'Suhu': [suhu_input]})
        
        # Hitung Prediksi
        hasil_prediksi = model.predict(input_df)
        hasil_bulat = int(hasil_prediksi[0])
        
        st.success(f"🌡️ Jika suhu {suhu_input}°C, kemungkinan laku **{hasil_bulat} Gelas**!")
        
        # --- VISUALISASI INTERAKTIF (PLOTLY) ---
        fig = go.Figure()

        # A. Data Asli (Titik Biru)
        fig.add_trace(go.Scatter(
            x=df_latih['Suhu'], 
            y=df_latih['Jual'],
            mode='markers',
            name='Data Asli',
            marker=dict(color='blue', size=10)
        ))

        # B. Garis Ramalan (Garis Merah)
        fig.add_trace(go.Scatter(
            x=df_latih['Suhu'], 
            y=model.predict(df_latih[['Suhu']]),
            mode='lines',
            name='Trend Garis',
            line=dict(color='red', width=2)
        ))

        # C. Prediksi Kamu (Bintang Hijau)
        fig.add_trace(go.Scatter(
            x=[suhu_input],
            y=[hasil_bulat],
            mode='markers',
            name='Prediksi Kamu',
            marker=dict(color='green', size=20, symbol='star')
        ))

        fig.update_layout(
            title="Analisis Prediksi Penjualan",
            xaxis_title="Suhu Udara (°C)",
            yaxis_title="Penjualan (Gelas)",
            hovermode="x unified"
        )

        st.plotly_chart(fig, use_container_width=True)