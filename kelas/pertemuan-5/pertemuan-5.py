# praktikum = ["Mahasiswa", 20, True, 45.10, ['APD',25]]

# print(praktikum[4][1])


# # list awal
# studyclub = ["Data Science", "Robotics", "Multimedia", "Network"]
# print(studyclub)
# # Kita akan mengganti elemen di indeks ke-2, yakni "Multimedia"
# studyclub[3] = "mikel"
# print(studyclub)


# matakuliah = ['PTI', 'APD','Kalkulus','Diskrit']
# print(matakuliah)
# # menghapus elemen pada indeks ke-2, yakni "Kalkulus"
# del matakuliah[2]
# print(matakuliah)

# matakuliah = ['PTI', 'APD','Kalkulus','Diskrit']
# print(matakuliah)
# # menghapus elemen dengan nilai "Kalkulus"
# matakuliah.remove('APD')
# print(matakuliah)

# matakuliah = ['PTI', 'APD','Kalkulus','Diskrit']
# print(matakuliah)
# # Menghapus & mengambil elemen 'Kalkulus' pada indeks ke-2
# sampah = matakuliah.pop(2)
# print(matakuliah)
# print(sampah) 

# matakuliah = ['PTI', 'APD','Kalkulus','Diskrit','Bahasa Inggris',
# 'Orsikom','Basis Data']
# # Menampilkan list mulai dari indeks 1 hingga 5 dengan loncatan 2
# print(matakuliah[0:6:3])

# a = [1, 2, 3]
# b = [4, 5, 6]
# # menggabungkan kedua list dengan operator (+)
# c = a + b
# print(c)

# a = ["teknik", "informatika"]
# # mengulang isi list dengan operator (*) sebanyak 3 kali
# c = a*3
# print(c)

# kelas = [
# ["Ridho", "Lian", "Nabil"],
# ["Daffa", "Dante", "Santoso"],
# ["Pernanda", "Riyadi", "Ahnaf"],
# ]

# print(kelas[2][2])

# mahasiswa = [["Daffa", "Dante", "Santoso"], ["Pernanda", "Triya", "Ahnaf"]]
# # perulangan for untuk mendapatkan semua elemen
# for i in mahasiswa:
#     print(i)
#     for j in i :
#         print (j)

# anggota = ("riyadi", 20, True, 3.96, ["APD",25],("samarinda",12))
# print(anggota)

# tugas = ('rangkuman', 'arduino','scrapping')
# # beri variabel setiap values
# (PTI, orsikom, basisdata) = tugas
# print(PTI)
# print(orsikom)
# print(basisdata)

# barang = ('triangle','bola', 'meja', 'handphone', 'televisi')
# # beri variabel setiap values
# (segitiga, bulat, *kotak) = barang
# print(segitiga)
# print(bulat)
# print(kotak[0])

# barang = ('triangle','bola', 'meja', 'handphone', 'televisi')
# angka=(1,2,3)
# # simpan di dalam variabel baru
# gabung=barang+angka
# print(gabung)

# barang = [['triangle' , 'bola'], ['meja', 'handphone'], ['televisi','laptop']]
# for nama_barang in barang:
#     print(nama_barang)
#     for j in i :
#         print (j)

mahasiswa = [["jawa","toraja"],[1],("batak")]
for i in mahasiswa:  