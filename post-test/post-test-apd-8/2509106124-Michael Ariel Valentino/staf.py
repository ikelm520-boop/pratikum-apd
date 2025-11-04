from utils import clear
from prettytable import PrettyTable

staf = [
    ["Pak kiel", "Pelatih", "082112223333"],
    ["Bu meimei", "Manajer", "081355557777"],
    ["Pak attar", "Medis", "081282864935"]
]

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
        table = PrettyTable(["Nama", "Jabatan", "Kontak"])
        for s in staf:
            table.add_row(s)
        print(table)

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