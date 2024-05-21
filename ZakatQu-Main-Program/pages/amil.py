from utils.db import read_amil

def amil(akun: str):
    while akun == "Takmir" :
        print("Halaman Amil\n")

        data = read_amil()
        print(data)



        input()