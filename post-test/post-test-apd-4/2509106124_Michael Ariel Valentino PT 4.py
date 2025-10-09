nim = input("Masukkan NIM: ")

#misi 1
stamina = int(nim[-3:])
chakra = 0
while chakra < 200 and stamina > 0:
    chakra += 5
    stamina -= 3

print(f"\n--- misi 1 ---")
print(f"Chakra: {chakra}, Sisa stamina: {stamina}")
print("Berhasil!" if chakra >= 200 else "Kehabisan stamina!")

#misi 2
tinggi = int(nim[-2:])
gulungan = len(range(3, tinggi + 1, 3))
print(f"\n--- misi 2 ---")
print(f"Tinggi menara {tinggi}m → Gulungan ditemukan: {gulungan}")

#misi 3
koridor = int(nim[-2])
intel, perangkap = 0, 0
for _ in range(koridor):
    for r in range(1, 4):
        if r % 2: intel += 1
        else: perangkap += 1

print(f"\n--- misi 3 ---")
print(f"Data Intelijen: {intel}, Perangkap dijinakkan: {perangkap}")
print("\nSemua misi selesai! 🍥")
