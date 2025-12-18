# 1. Kita DEFINISIKAN dulu fungsinya (Bikin SOP)
def sapa_orang(nama):
    print("Halo, " + nama + "!")
    print("Semoga harimu menyenangkan!")
    print("---")

# 2. Program Utama (Main Program)
# Perhatikan: Bagian ini TIDAK menjorok ke dalam
print("Mulai Program...")

# Panggil Mantranya!
sapa_orang("Mooya")
sapa_orang("Elon Musk")
sapa_orang("Galbrena")

# Fungsi Konversi Dolar ke Rupiah
def hitung_rupiah(dolar):
    kurs = 16000  # Anggap 1 Dolar = 16.000 Rupiah
    hasil = dolar * kurs
    return hasil  # PENTING: Kembalikan nilainya!

# Cara Pakai:
uang_saya = hitung_rupiah(10)  # Tukar 10 Dolar
uang_bapak = hitung_rupiah(50) # Tukar 50 Dolar

print("Uang saya: Rp", uang_saya)
print("Uang bapak: Rp", uang_bapak)

# Karena pakai RETURN, hasilnya bisa dijumlahin!
total_harta = uang_saya + uang_bapak
print("Total Harta Keluarga: Rp", total_harta)