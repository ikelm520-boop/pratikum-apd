# def perkenalan():
#     print("Halo aku Nabil")
      
# perkenalan()

# # Membuat Fungsi
# def salam():
#   print ("Halo, Ridho")
# def kali():
#   x = 5*5
#   print(x)

# #Pemanggilan Fungsi
# salam()
# salam()
# salam()
# kali()
# kali()
# kali()  

# #Pembuatan Fungsi Dengan Parameter
# def luas_persegi_panjang(panjang, lebar):
#   luas = panjang * lebar
#   print ("luas persegi panjang adalah" , luas)

# #Pemanggilan Fungsi luas_persegi_panjang
# luas_persegi_panjang(4, 5)

# def luas_persegi(sisi):
  
#   luas = sisi * sisi
#   return luas

# # pemanggilan fungsi luas persegi
# print ("Luas persegi :", luas_persegi(8))

# # membuat variabel global
# Nama = "Hambali"
# Mata_Kuliah = "Algoritma dan Pemrograman Dasar"

# # membuat variabel lokal
# def info():
#   Nama = "Informatika"
#   Mata_Kuliah = "Logika Informatika"

# # mengakses variabel lokal
#   print("Prodi:", Nama)
#   print("Mata Kuliah:", Mata_Kuliah)

# # mengakses variabel global
# print("Prodi:", Nama)
# print("Mata Kuliah:", Mata_Kuliah)

# info()

# def faktorial(n):
# # Basis (Base Case): Kondisi berhenti
#   if n == 1 or n == 0:
#     return 1
# # Rekursi (Recursive Case): Fungsi memanggil dirinya sendiri
#   else:
#     return n * faktorial(n - 1)
# # Memanggil fungsi
# hasil = faktorial(5)
# print(f"Hasil dari 5! adalah: {hasil}")

film = [marvel]

def show_data():
  if len(film) <= 0:
   print("Belum Ada data")
  else:
    print("ID | Judul Film")
  for indeks in range(len(film)):
    print(indeks, "|", film[indeks])

def insert_data():
   film_baru = input("Judul Film: ")
   film.append(film_baru)
   print("Film berhasil ditambahkan!")