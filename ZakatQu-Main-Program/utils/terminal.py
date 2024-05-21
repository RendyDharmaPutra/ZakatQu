import os


def clear_screen():
    # Menggunakan perintah sistem operasi yang sesuai untuk membersihkan layar terminal
    os.system('cls' if os.name == 'nt' else 'clear')
