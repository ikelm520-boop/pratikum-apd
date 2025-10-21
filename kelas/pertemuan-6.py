# # Membuat set
# buah = {"apel", "jeruk", "mangga", "apel"}
# print(buah)


# inputTambah = int(input("tambah angka"))
# angka_ganjil.add(10)
# print(angka_ganjil)

# print(angka_ganjil)
# inputTambah = int (input("tambah angka :"))

# kelas = {
#     "nama" : "michael"
#     "nama" : "kiel"
# }

# Daftar_buku = {
# "Buku1" : "Bumi Manusia",
# "Buku2" : "Laut Bercerita"
# }

# print(Daftar_buku["Buku1"])
# print(Daftar_buku)

# Daftar_buku = {
# "Buku2" : "gotame",
# "Buku1" : "batman"
# }

# print(Daftar_buku["Buku1"])
# print(Daftar_buku)

# Biodata = {
#     "Nama" : "Ananda Daffa Harahap",
#     "NIM" : 2409106050,
#     "KRS" : ["Pemrograman Web", "Struktur Data", "Basis Data"],
#     "Mahasiswa_Aktif" : True,
#     "Social Media" : {"instagram" : "daffahrhap"}
# }

# print(f"nama saya adalah {Biodata["Nama"]}") 
# print("Instagram :", Biodata["Social Media"]["Instagram"])

# print("")

 
# print(f"nama saya adalah {Biodata.get("Nama")}")
# print(Biodata.get("Nama"))

# Nilai = { 
#     "Matematika": 80, 
#     "B. Indonesia": 90,
#      "B. Inggris": 81, 
#     "Kimia": 78, 
#     "Fisika": 80 
# } 
 
# # Tanpa menggunakan items() 
# for i in Nilai: 
#     print(i) 
 
# print("")  # pemisah 
 
# # Menggunakan items() 
# for key, value in Nilai.items(): 
#     print(f"Nilai {key}: {value}")

# Film = { 
# "Avenger Endgame" : "Action", 
# "Sherlock Holmes" : "Mystery", 
# "The Conjuring" : "Horror"
# } 
# #Sebelum Ditambah 
# print(Film) 
 
# Film["Zombieland"] = "Comedy" 
# Film.update({"Hours" : "Thriller"}) 
# #Setelah Ditambah 
# print(Film) 
 
# #Sebelum Ditambah 
# {'Avenger Endgame': 'Action', 'Sherlock Holmes': 'Mystery', 
# 'The Conjuring': 'Horror'} 
 
# #Setelah Ditambah 
# {'Avenger Endgame': 'Action', 'Sherlock Holmes': 'Mystery', 
# 'The Conjuring': 'Horror', 'Zombieland': 'Comedy', 'Hours': 
# 'Thriller'}


# data = { 
# "Nama" : "Daffa", 
# "Umur" : 19, 
# "Jurusan" : "Informatika" 
# } 
# #Sebelum Dihapus 

# # cache = data.pop("Nama") 

# # 
# buku = { 
#  "Buku1" : "Bumi Manusia", 
#  "Buku2" : "Laut Bercerita" 
# } 
 

# pinjam2 = buku.copy()

# buku["buku3"] = "jamal"
# pinjam2["buku3"] = "kiel"

# print(buku)
# print(pinjam2)

# key = "apel", "jeruk", "mangga" 
# value = 1, 2, 3
# buah = dict.fromkeys(key, value) 
# print(buah)

# data = { 
# "Nama" : "Daffa", 
# "Umur" : 19, 
# "Jurusan" : "Informatika" 
# } 

# for value in data.values()

# Nilai = { 
# "Matematika" : 80, 
# "B. Indonesia" : 90, 
# "B. Inggris" : 81 
# } 
 
# #sebelum Setdefault 
# print(Nilai) 
 
# print("") 
 
# #menggunakan setdefault 
# print("Nilai : ", Nilai.setdefault("Kimia", 70)) 
 
# print("") 
 
# #setelah menggunakan setdefault 
# print(Nilai)