import os

users = {
    "admin": {"password": "admin123", "role": "admin"}
}

pemain = {
    "bang gilbert/lian": {"posisi": "Spiker", "nomor": 7, "kontak": "081234567890", "status": "Inti"},
    "mikeng": {"posisi": "Tosser", "nomor": 3, "kontak": "089876543210", "status": "Inti"},
    "asoy": {"posisi": "Libero", "nomor": 31, "kontak": "082233445566", "status": "Inti"},
    "erpang": {"posisi": "Tosser", "nomor": 20, "kontak": "082300942134", "status": "Cadangan"}
}

staf = {
    "Pak kiel": {"jabatan": "Pelatih", "kontak": "082112223333"},
    "Bu meimei": {"jabatan": "Manajer", "kontak": "081355557777"},
    "Pak attar": {"jabatan": "Medis", "kontak": "081282864935"}
}

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def input_angka(prompt):
    angka = input(prompt)
    if not angka.isdigit():
        print("Input harus berupa angka!")
        return None
    return int(angka)

def register():
    clear()
    print("=== REGISTRASI USER BARU ===")
    username = input("Username: ")
    password = input("Password: ")

    if username in users:
        print("Username sudah digunakan!")
        return

    users[username] = {"password": password, "role": "user"}
    print("Registrasi berhasil! Silakan login.")

def login():
    clear()
    print("=== LOGIN ===")
    username = input("Username: ")
    password = input("Password: ")

    if username in users and users[username]["password"] == password:
        print(f"Login berhasil sebagai {users[username]['role']}!")
        return users[username]["role"]
    else:
        print("Login gagal. Username atau password salah.")
        return None

def tambah_pemain():
    clear()
    print("--- Tambah Pemain Baru ---")
    nama = input("Nama pemain: ")
    if nama in pemain:
        print("Pemain sudah terdaftar!")
        return
    posisi = input("Posisi (Tosser/Spiker/Libero): ")
    nomor = input_angka("Nomor punggung: ")
    if nomor is None:
        return
    kontak = input("Nomor kontak: ")
    status = input("Status (Inti/Cadangan): ")
    pemain[nama] = {"posisi": posisi, "nomor": nomor, "kontak": kontak, "status": status}
    print(f"Pemain {nama} berhasil ditambahkan!")

def tampilkan_pemain():
    clear()
    print("=== Daftar Pemain ===")
    if not pemain:
        print("Belum ada pemain.")
    else:
        for nama, data in pemain.items():
            print(f"{nama} | Posisi: {data['posisi']} | No: {data['nomor']} | Kontak: {data['kontak']} | Status: {data['status']}")

def ubah_pemain():
    tampilkan_pemain()
    nama_cari = input("\nMasukkan nama pemain yang ingin diubah: ")
    if nama_cari in pemain:
        print("Kosongkan untuk tidak mengubah.")
        posisi = input(f"Posisi ({pemain[nama_cari]['posisi']}): ") or pemain[nama_cari]['posisi']
        nomor = input(f"No Punggung ({pemain[nama_cari]['nomor']}): ")
        nomor = int(nomor) if nomor.isdigit() else pemain[nama_cari]['nomor']
        kontak = input(f"Kontak ({pemain[nama_cari]['kontak']}): ") or pemain[nama_cari]['kontak']
        status = input(f"Status ({pemain[nama_cari]['status']}): ") or pemain[nama_cari]['status']
        pemain[nama_cari] = {"posisi": posisi, "nomor": nomor, "kontak": kontak, "status": status}
        print("Data pemain berhasil diubah!")
    else:
        print("Pemain tidak ditemukan!")

def hapus_pemain():
    tampilkan_pemain()
    nama_cari = input("\nMasukkan nama pemain yang ingin dihapus: ")
    if nama_cari in pemain:
        del pemain[nama_cari]
        print(f"Pemain {nama_cari} berhasil dihapus.")
    else:
        print("Pemain tidak ditemukan!")

def tambah_staf():
    clear()
    print("--- Tambah Staf Baru ---")
    nama = input("Nama staf: ")
    if nama in staf:
        print("Staf sudah terdaftar!")
        return
    jabatan = input("Jabatan: ")
    kontak = input("Nomor kontak: ")
    staf[nama] = {"jabatan": jabatan, "kontak": kontak}
    print(f"Staf {nama} berhasil ditambahkan!")

def tampilkan_staf():
    clear()
    print("=== Daftar Staf ===")
    if not staf:
        print("Belum ada staf.")
    else:
        for nama, data in staf.items():
            print(f"{nama} | Jabatan: {data['jabatan']} | Kontak: {data['kontak']}")

def ubah_staf():
    tampilkan_staf()
    nama_cari = input("\nMasukkan nama staf yang ingin diubah: ")
    if nama_cari in staf:
        print("Kosongkan untuk tidak mengubah.")
        jabatan = input(f"Jabatan ({staf[nama_cari]['jabatan']}): ") or staf[nama_cari]['jabatan']
        kontak = input(f"Kontak ({staf[nama_cari]['kontak']}): ") or staf[nama_cari]['kontak']
        staf[nama_cari] = {"jabatan": jabatan, "kontak": kontak}
        print("Data staf berhasil diubah!")
    else:
        print("Staf tidak ditemukan!")

def hapus_staf():
    tampilkan_staf()
    nama_cari = input("\nMasukkan nama staf yang ingin dihapus: ")
    if nama_cari in staf:
        del staf[nama_cari]
        print(f"Staf {nama_cari} berhasil dihapus.")
    else:
        print("Staf tidak ditemukan!")

def menu_admin():
    while True:
        print("""
====== MENU ADMIN TIM VOLI ======
1. Tambah Pemain
2. Tambah Staf
3. Lihat Pemain
4. Lihat Staf
5. Ubah Pemain
6. Ubah Staf
7. Hapus Pemain
8. Hapus Staf
9. Logout
=================================
""")
        pilihan = input("Pilih menu: ")
        if pilihan == "1":
            tambah_pemain()
        elif pilihan == "2":
            tambah_staf()
        elif pilihan == "3":
            tampilkan_pemain()
        elif pilihan == "4":
            tampilkan_staf()
        elif pilihan == "5":
            ubah_pemain()
        elif pilihan == "6":
            ubah_staf()
        elif pilihan == "7":
            hapus_pemain()
        elif pilihan == "8":
            hapus_staf()
        elif pilihan == "9":
            break
        else:
            print("Pilihan tidak valid!")

def menu_user():
    while True:
        print("""
====== MENU USER TIM VOLI ======
1. Lihat Pemain
2. Lihat Staf
3. Logout
================================
""")
        pilihan = input("Pilih menu: ")
        if pilihan == "1":
            tampilkan_pemain()
        elif pilihan == "2":
            tampilkan_staf()
        elif pilihan == "3":
            break
        else:
            print("Pilihan tidak valid!")

while True:
    print("""
=== SELAMAT DATANG DI SISTEM TIM VOLI ===
1. Login
2. Register
0. Keluar
""")
    pilih = input("Pilih menu: ")

    if pilih == "1":
        role = login()
        if role == "admin":
            menu_admin()
        elif role == "user":
            menu_user()
    elif pilih == "2":
        register()
    elif pilih == "0":
        print("Program selesai. Terima kasih!")
        break
    else:
        print("Menu tidak valid!")