import random # Library bawaan Python buat ngocok angka (RNG)

print("--- SELAMAT DATANG DI MONSTER BATTLE ---")
print("Siapkan mentalmu, Pahlawan!")

# 1. DATA PEMAIN (Player)
player_nama = input("Masukkan nama ksatria: ")
# Ganti HP kamu jadi 200 (Tank Badak)
player_hp = 200
player_max_hp = 200
# List Jurus (Cuma buat tampilan menu nanti)
menu_aksi = ["1. Serang Dasar", "2. Magic Heal", "3. Kabur"]

# 2. DATA MUSUH (Monster)
monster_nama = "Raja Iblis Python"
# Ganti dari 150 jadi 80 aja, biar lembek
monster_hp = 80 
monster_max_hp = 80

# Fungsi untuk menghitung damage serangan (biar random)
def hitung_serangan(nama_penyerang):
    if nama_penyerang == "GM Mooya":
        print("⚡ GOD MODE AKTIF! MENGHANCURKAN REALITAS...")
        return 100 # Sekali pukul langsung sekarat
    
    # Random damage antara 10 sampai 25
    damage = random.randint(10, 25)
    
    # Kritis! (Peluang 20%) -> Materi Peluang kemarin kepake nih!
    kritis = random.randint(1, 10) # Kocok dadu 1-10
    if kritis > 8: # Kalau keluar angka 9 atau 10
        damage = damage * 2 # Damage lipat ganda!
        print(f"WOW! {nama_penyerang} melakukan CRITICAL HIT! 💥")
        
    return damage

# Fungsi untuk Healing (Nambah darah)
def pakai_potion():
    heal = random.randint(15, 30)
    print("✨ Syuuu... Kamu meminum potion.")
    return heal

print("\n" + "="*20)
print("PERTARUNGAN DIMULAI!")
print("="*20)

# Loop berjalan selama KEDUANYA masih hidup
while player_hp > 0 and monster_hp > 0:
    # 1. TAMPILKAN STATUS (HUD)
    print("\n------------------------------")
    print(f"💀 {monster_nama}: {monster_hp}/{monster_max_hp} HP")
    print(f"🛡️ {player_nama}: {player_hp}/{player_max_hp} HP")
    print("------------------------------")

    # 2. MENU AKSI (Tampilkan List Menu)
    print("Giliranmu! Mau ngapain?")
    for aksi in menu_aksi:
        print(aksi)
    
    # 3. INPUT PLAYER
    pilihan = input("Pilih (1/2/3): ")

    # 4. LOGIKA PLAYER (Pake Fungsi yang tadi dibuat)
    if pilihan == "1":
        # Serang!
        dmg = hitung_serangan(player_nama)
        monster_hp = monster_hp - dmg
        print(f"⚔️ Kamu menyerang! Monster kena {dmg} damage.")

    elif pilihan == "2":
        # Heal
        tambah_darah = pakai_potion()
        player_hp = player_hp + tambah_darah
        # Cek biar HP gak kelebihan (Materi Logic if)
        if player_hp > player_max_hp:
            player_hp = player_max_hp
        print(f"💖 Darah bertambah {tambah_darah} point.")

    elif pilihan == "3":
        # Kabur
        print("🏃 Kamu lari terbirit-birit kayak ayam...")
        break # Mantra BREAK untuk matikan Loop seketika

    else:
        print("❌ Pilihan ngaco! Kamu bengong di medan perang.")

    # 5. GILIRAN MONSTER (Cek dulu monster masih hidup gak?)
    if monster_hp > 0 and pilihan != "3":
        print("...")
        # Monster membalas!
        dmg_monster = hitung_serangan(monster_nama)
        player_hp = player_hp - dmg_monster
        print(f"🔥 {monster_nama} membalas! Kamu kena {dmg_monster} damage.")

# --- DILUAR LOOP (GAME OVER / WIN) ---
print("\n" + "="*20)
if player_hp > 0 and monster_hp <= 0:
    print(f"🎉 VICTORY! {monster_nama} telah dikalahkan!")
    print(f"Selamat, {player_nama}! Kamu adalah Pahlawan sejati.")
elif player_hp <= 0:
    print("💀 GAME OVER...")
    print(f"{player_nama} telah gugur dalam tugas.")
else:
    print("Pertarungan berakhir. (Kabur)")