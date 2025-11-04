from utils import clear

users = [["admin", "admin123", "admin"]]

def register():
    clear()
    print("=== REGISTRASI USER BARU ===")
    username = input("Username: ")
    password = input("Password: ")

    for user in users:
        if user[0] == username:
            print("Username sudah digunakan!")
            return

    users.append([username, password, "user"])
    print("Registrasi berhasil! Silakan login.")

def login():
    clear()
    print("=== LOGIN ===")
    username = input("Username: ")
    password = input("Password: ")

    for user in users:
        if user[0] == username and user[1] == password:
            print(f"Login berhasil sebagai {user[2]}!")
            return user[2]

    print("Login gagal. Username atau password salah.")
    return None