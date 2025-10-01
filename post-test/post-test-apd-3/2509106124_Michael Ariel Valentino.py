print("=== Penghitung Gaji Karyawan PT. BOM ===")
nama = input("Nama karyawan: ")
jabatan = input("Jabatan (peracik petasan/pengantar petasan): ").lower()
hari = int(input("Hari kerja: "))
jam = int(input("Jam kerja per hari: "))
lembur = int(input("Jumlah lembur: "))

harga_petasan = 5000
bayar_jam = 0
bayar_lembur = 0

if jabatan == "peracik petasan":
    if hari >= 18 and jam >= 6 and lembur >= 2:
        bayar_jam, bayar_lembur = 20000, 10000
    elif hari >= 24 and jam >= 8 and lembur >= 4:
        bayar_jam, bayar_lembur = 25000, 15000
    else:
        bayar_jam, bayar_lembur = 15000, 10000

elif jabatan == "pengantar petasan":
    if hari >= 16 and jam >= 5 and lembur >= 4:
        bayar_jam, bayar_lembur = 20000, 15000
    elif hari >= 20 and jam >= 7 and lembur >= 7:
        bayar_jam, bayar_lembur = 25000, 20000
    else:
        bayar_jam, bayar_lembur = 15000, 12000
else:
    print("Jabatan tidak ada!")
    exit()

total = ((bayar_jam * jam) * hari) + (lembur * bayar_lembur)

# output
print("\n--- Detail Gaji ---")
print(f"Nama          : {nama}\n"
      f"Jabatan       : {jabatan}\n"
      f"Harga per pcs : Rp {harga_petasan}\n"
      f"Hari kerja    : {hari}\n"
      f"Jam kerja     : {jam}\n"
      f"Jumlah lembur : {lembur}\n"
      f"Bayar per jam : Rp {bayar_jam}\n"
      f"Bayar lembur  : Rp {bayar_lembur}\n"
      f"Total gaji    : Rp {total}")