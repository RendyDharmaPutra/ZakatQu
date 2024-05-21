from utils.db import conn, cur
from utils.db import searchPemberi
from utils.db import searchJenisZakat
from utils.db import searchBentukZakat
from utils.db import QueryInput
from datetime import date

def pembayaran():
    InputQuery = []
    NamaTabel = 'pembayaran_zakat'
    NamaKolom = 'jumlah_pemberian, tanggal_pemberian, id_amil_zakat, id_pemberi_zakat, id_bentuk_zakat, id_jenis_zakat'
    InputNamaPemberi = input("Masukkan Nama : ")
    print("[(1) Zakat Fitrah], [(2) Zakat Mal]")
    InputJenisZakat = input("Masukkan Jenis Zakat : ")
    while InputJenisZakat:
        if InputJenisZakat == "1":
            print("[(1) Beras], [(2) Uang]")
            InputBentukZakat = input("Masukkan Bentuk Zakat : ")
            while InputBentukZakat:
                if InputBentukZakat == "1":
                    JumlahZakat = int(input("Masukkan Jumlah dalam Gram (Gr): "))
                    break
                elif InputBentukZakat == "2":
                    JumlahZakat = int(input("Masukkan Jumlah dalam Ribuan (Rp): "))
                    break
                else:
                    print("InputSalah")
            break
        elif InputJenisZakat == "2":
            print("[(2) Uang], [(2) Emas]")
            InputBentukZakat = input("Masukkan Bentuk Zakat : ")
            while InputBentukZakat:
                if InputBentukZakat == "2":
                    JumlahZakat = int(input("Masukkan Jumlah dalam Ribuan (Rp): "))
                    break
                elif InputBentukZakat == "3":
                    JumlahZakat = int(input("Masukkan Jumlah dalam Gram (Gr): "))
                    break
                else:
                    print("InputSalah")
            break
        else:
            print("InputSalah")
    AmilZakat = 3
    Tanggal = date.today().strftime("%d-%m-%Y")

    InputQuery.append(f'{JumlahZakat}')
    InputQuery.append(f'{Tanggal}')
    InputQuery.append(AmilZakat)
    InputQuery.append(searchPemberi(InputNamaPemberi)[0][0])
    InputQuery.append(searchBentukZakat(InputBentukZakat)[0][0])
    InputQuery.append(searchJenisZakat(InputJenisZakat)[0][0])
    
    QueryInput(InputQuery, NamaTabel, NamaKolom)
    
        
    
    
    
    
    
    
    