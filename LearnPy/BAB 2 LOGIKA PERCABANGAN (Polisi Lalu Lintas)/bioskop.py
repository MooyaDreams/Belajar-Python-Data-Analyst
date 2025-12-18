print("--- SISTEM TIKET BIOSKOP ---")

umur_str = input("Berapa umur kamu? ")
umur = int(umur_str)  # Jangan lupa mantra konversi!

# Logika Percabangan
if umur >= 17:
    print("Silakan masuk! Selamat menonton film horor.")
    print("Jangan lupa beli popcorn ya.")
elif umur >= 13:
    print("Kamu boleh masuk, tapi cuma nonton film Remaja ya.")
else:
    print("Maaf dek, kamu belum cukup umur. Pulang gih minum susu.")
    
print("--- Cek Selesai ---")