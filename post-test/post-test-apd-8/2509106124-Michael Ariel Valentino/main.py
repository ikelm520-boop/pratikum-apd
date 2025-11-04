from auth import login, register
from pemain import tambah_pemain, tampilkan_pemain, ubah_pemain, hapus_pemain
from staf import tambah_staf, tampilkan_staf, ubah_staf, hapus_staf

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