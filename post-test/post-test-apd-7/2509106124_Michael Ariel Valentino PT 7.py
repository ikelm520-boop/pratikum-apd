import os

users = [
    ["admin", "admin123", "admin"]
]

pemain = [
    ["bang gilbert/lian", "Spiker", 7, "081234567890", "Inti"],
    ["mikeng", "Tosser", 3, "089876543210", "Inti"],
    ["asoy", "Libero", 31, "082233445566", "Inti"],
    ["erpang", "Tosser", 20, "082300942134", "Cadangan"]
]

staf = [
    ["Pak kiel", "Pelatih", "082112223333"],
    ["Bu meimei", "Manajer", "081355557777"],
    ["Pak attar", "Medis", "081282864935"]
]


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def register():
    clear()
    print("=== REGISTRASI USER BARU ===")
    username = input("Username: ")
    password = input("Password: ")

    for user in users:
        if user[0] == username:
            print("Username sudah digunakan!")
            return

    users.append([username, password, "user"])
    print("Registrasi berhasil! Silakan login.")


def login():
    clear()
    print("=== LOGIN ===")
    username = input("Username: ")
    password = input("Password: ")

    for user in users:
        if user[0] == username and user[1] == password:
            print(f"Login berhasil sebagai {user[2]}!")
            return user[2]

    print("Login gagal. Username atau password salah.")
    return None


def input_angka(prompt):
    angka = input(prompt)
    if not angka.isdigit():
        print("Input harus berupa angka!")
        return None
    return int(angka)


def tambah_pemain():
    clear()
    print("--- Tambah Pemain Baru ---")
    nama = input("Nama pemain: ")
    posisi = input("Posisi (Tosser/Spiker/Libero): ")
    nomor = input_angka("Nomor punggung: ")
    if nomor is None:
        return
    kontak = input("Nomor kontak: ")
    status = input("Status (Inti/Cadangan): ")
    pemain.append([nama, posisi, nomor, kontak, status])
    print(f"Pemain {nama} berhasil ditambahkan!")


def tampilkan_pemain():
    clear()
    print("=== Daftar Pemain ===")
    if not pemain:
        print("Belum ada pemain.")
    else:
        for p in pemain:
            print(f"{p[0]} | Posisi: {p[1]} | No: {p[2]} | Kontak: {p[3]} | Status: {p[4]}")


def ubah_pemain():
    tampilkan_pemain()
    if not pemain:
        return
    nama_cari = input("\nMasukkan nama pemain yang ingin diubah: ")
    for p in pemain:
        if p[0].lower() == nama_cari.lower():
            print("Kosongkan untuk tidak mengubah.")
            nama = input(f"Nama ({p[0]}): ") or p[0]
            posisi = input(f"Posisi ({p[1]}): ") or p[1]
            nomor = input(f"No Punggung ({p[2]}): ")
            nomor = int(nomor) if nomor.isdigit() else p[2]
            kontak = input(f"Kontak ({p[3]}): ") or p[3]
            status = input(f"Status ({p[4]}): ") or p[4]
            p[:] = [nama, posisi, nomor, kontak, status]
            print("Data pemain berhasil diubah!")
            return
    print("Pemain tidak ditemukan!")


def hapus_pemain():
    tampilkan_pemain()
    if not pemain:
        return
    nama_cari = input("\nMasukkan nama pemain yang ingin dihapus: ")
    for p in pemain:
        if p[0].lower() == nama_cari.lower():
            pemain.remove(p)
            print(f"Pemain {p[0]} berhasil dihapus.")
            return
    print("Pemain tidak ditemukan!")

def tambah_staf():
    clear()
    print("--- Tambah Staf Baru ---")
    nama = input("Nama staf: ")
    jabatan = input("Jabatan: ")
    kontak = input("Nomor kontak: ")
    staf.append([nama, jabatan, kontak])
    print(f"Staf {nama} berhasil ditambahkan!")


def tampilkan_staf():
    clear()
    print("=== Daftar Staf ===")
    if not staf:
        print("Belum ada staf.")
    else:
        for s in staf:
            print(f"{s[0]} | Jabatan: {s[1]} | Kontak: {s[2]}")


def ubah_staf():
    tampilkan_staf()
    if not staf:
        return
    nama_cari = input("\nMasukkan nama staf yang ingin diubah: ")
    for s in staf:
        if s[0].lower() == nama_cari.lower():
            print("Kosongkan untuk tidak mengubah.")
            nama = input(f"Nama ({s[0]}): ") or s[0]
            jabatan = input(f"Jabatan ({s[1]}): ") or s[1]
            kontak = input(f"Kontak ({s[2]}): ") or s[2]
            s[:] = [nama, jabatan, kontak]
            print("Data staf berhasil diubah!")
            return
    print("Staf tidak ditemukan!")


def hapus_staf():
    tampilkan_staf()
    if not staf:
        return
    nama_cari = input("\nMasukkan nama staf yang ingin dihapus: ")
    for s in staf:
        if s[0].lower() == nama_cari.lower():
            staf.remove(s)
            print(f"Staf {s[0]} berhasil dihapus.")
            return
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
