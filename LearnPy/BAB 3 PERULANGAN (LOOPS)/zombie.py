kenyang = "belum"

while kenyang == "belum":
    jawab = input("Makan otak lagi? (ya/tidak): ")
    
    # Cek Logika Ketat
    if jawab == "tidak":
        kenyang = "sudah"
        print("Oke, zombie kenyang. Tidur.")
    elif jawab == "ya":
        print("Nyam nyam... Enak banget!")
    else:
        # Ini kalau user jawab aneh-aneh
        print("Heh! Jawabnya cuma boleh 'ya' atau 'tidak'!")

print("--- PROGRAM SELESAI ---")