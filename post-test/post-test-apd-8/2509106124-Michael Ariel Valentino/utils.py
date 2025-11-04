import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def input_angka(prompt):
    angka = input(prompt)
    if not angka.isdigit():
        print("Input harus berupa angka!")
        return None
    return int(angka)