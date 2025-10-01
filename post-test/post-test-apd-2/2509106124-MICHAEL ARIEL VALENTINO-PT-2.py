nama_pelanggan = input("Masukkan nama pelanggan: ")
jumlah_batu_bata = int(input("Masukkan jumlah batu bata: "))
jumlah_semen = int(input("Masukkan jumlah karung semen: "))

harga_bata = 100
harga_semen = 100000

total_awal = (jumlah_batu_bata * harga_bata) + (jumlah_semen * harga_semen)

is_paket_hemat = jumlah_batu_bata == 500 and jumlah_semen == 5
is_paket_ultra_mantap = jumlah_batu_bata == 2000 and jumlah_semen == 16

if is_paket_ultra_mantap:
    diskon = 0.30
    keterangan_diskon = "Paket ultra mantap (30%)"
elif is_paket_hemat:
    diskon = 0.15
    keterangan_diskon = "Paket Hemat (15%)"
else:
    diskon = 0.0
    keterangan_diskon = "Tidak Ada Diskon"

jumlah_diskon = total_awal * diskon
total_akhir = float(total_awal - jumlah_diskon)

# Output
print("="*50)
print("ESTIMASI BIAYA BAHAN BANGUNAN")
print("="*50)
print(f"Nama Pelanggan: {nama_pelanggan}")
print("-"*50)
print("| Barang     | Jumlah   | Harga Satuan        |")
print("-"*50)
print(f"| Batu Bata   | {jumlah_batu_bata:<8}| Rp{harga_bata:<17,}|")
print(f"| Semen       | {jumlah_semen:<8}| Rp{harga_semen:<17,}|")
print("-"*50)
print(f"Total Biaya Awal: Rp {total_awal:,}")
print(f"Diskon yang Didapat: {keterangan_diskon}")
print(f"Jumlah Diskon: Rp {int(jumlah_diskon):,}")
print("-"*50)
print(f"TOTAL BIAYA AKHIR: Rp {int(total_akhir):,}")
print("="*50)
