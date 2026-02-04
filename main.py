catatan = []

def tambah_catatan():
    mapel = input("Masukkan mapel: ").strip()
    topik = input("Masukkan topik: ").strip()
    while True:
        durasi_input = input("Masukkan durasi belajar (menit): ").strip()
        try:
            durasi = int(durasi_input)
            if durasi < 0:
                print("Durasi harus berupa bilangan positif.")
                continue
            break
        except ValueError:
            print("Masukkan angka bulat untuk durasi.")

    catatan.append({
        'mapel': mapel,
        'topik': topik,
        'durasi': durasi
    })
    print("Catatan berhasil ditambahkan.")

def lihat_catatan():
    if not catatan:
        print("Belum ada catatan belajar.")
        return

    print("\nDaftar Catatan Belajar:")
    for idx, c in enumerate(catatan, 1):
        print(f"{idx}. Mapel: {c['mapel']} | Topik: {c['topik']} | Durasi: {c['durasi']} menit")

def total_waktu():
    if not catatan:
        print("Belum ada catatan belajar.")
        return

    total = sum(item.get('durasi', 0) for item in catatan)
    print(f"Total waktu belajar: {total} menit")

def simpan_ke_file():
    import json
    if not catatan:
        print("Tidak ada catatan untuk disimpan.")
        return
    try:
        with open("catatan.json", "w", encoding="utf-8") as f:
            json.dump(catatan, f, ensure_ascii=False, indent=2)
        print("Catatan berhasil disimpan ke 'catatan.json'.")
    except Exception as e:
        print("Gagal menyimpan catatan:", e)

def menu():
    print("\n=== Study Log App ===")
    print("1. Tambah catatan belajar")
    print("2. Lihat catatan belajar")
    print("3. Total waktu belajar")
    print("4. Keluar")

while True:
    menu()
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_catatan()
    elif pilihan == "2":
        lihat_catatan()
    elif pilihan == "3":
        total_waktu()
    elif pilihan == "4":
        print("Terima kasih, terus semangat belajar!")
        break
    else:
        print("Pilihan tidak valid")