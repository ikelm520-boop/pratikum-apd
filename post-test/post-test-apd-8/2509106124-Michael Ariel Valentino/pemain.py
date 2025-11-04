from utils import clear, input_angka
from prettytable import PrettyTable

pemain = [
    ["bang gilbert/lian", "Spiker", 7, "081234567890", "Inti"],
    ["mikeng", "Tosser", 3, "089876543210", "Inti"],
    ["asoy", "Libero", 31, "082233445566", "Inti"],
    ["erpang", "Tosser", 20, "082300942134", "Cadangan"]
]

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
        table = PrettyTable(["Nama", "Posisi", "No", "Kontak", "Status"])
        for p in pemain:
            table.add_row(p)
        print(table)

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