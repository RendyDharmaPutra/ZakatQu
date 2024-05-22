from utils.db import conn, cur
from utils.db import searchPemberi
from utils.db import QueryInput
from utils.db import UpdatePemberi
from utils.db import read_pemberi
from utils.db import read_pembayaran
from utils.db import read_pembayaran_with_join
from utils.db import Update_data
from utils.terminal import clear_screen

from datetime import date

def pembayaran(akun):
    NamaTabel = 'pembayaran_zakat'
    NamaKolom = 'besar_pemberian, tanggal_pemberian, id_amil_zakat, id_pemberi_zakat, id_bentuk_zakat, id_jenis_zakat'

    print("Halaman Pemberi")
    for i in read_pembayaran():
        print(i)
    
    print("Tambah[1], Edit[2], Hapus[3], Kembali[0]")
    InputPengguna = input("Masukkan fitur yang dipilih : ")


    match InputPengguna:
        case '1':
            Tambah_pembayaran(akun, NamaTabel, NamaKolom)
        case '2':
            Edit_pembayaran(akun, NamaTabel, NamaKolom)
        case '3':
            Hapus_pembayaran(akun)
        case '0':
            print("Apakah Yakin Untu Kembali ?")
            input()
            return
          
def Tambah_pembayaran(akun, NamaTabel, NamaKolom):
    
    Notifikasi = ''
    
    while True:
        InputQuery = []
        
        
        clear_screen()
        
        print("Tambah Pembayaran")

        if len(Notifikasi) > 0:
            print(Notifikasi)
            
        Konfirmasi = input("Masukkan 0 untuk keluar dari fitur : ")
        
        if Konfirmasi == '0':
            return -1
        
        elif len(Konfirmasi) > 0 and Konfirmasi != '0':
            Notifikasi = "Input tidak valid"
            
            continue
            
            
        # Jangan diupdate sampai  hasil dari inputKeteranganZakat bisa disolve untuk dimasukkan ke inputquery secara langsung 
        NamaPemberi = InputNamaPemberi()
        JenisZakat, BentukZakat, JumlahZakat = InputKeteranganZakat()

        InputQuery.append(f'{JumlahZakat}')
        InputQuery.append(date.today().strftime("%d-%m-%Y"))
        InputQuery.append(akun[0][0])
        InputQuery.append(NamaPemberi)
        InputQuery.append(int(BentukZakat))
        InputQuery.append(int(JenisZakat))
        
        Konfirmasi = input("Tekan Enter Untuk Simpan Data, Tekan 0 Untuk Batal")
        
        if Konfirmasi.lower() == "0":
            continue
        
        else:
            QueryInput(InputQuery, NamaTabel, NamaKolom)
            UpdatePemberi(NamaPemberi)
            Notifikasi = "Data Sudah Disimpan"


def InputNamaPemberi():
    
    
    for i in read_pemberi():
        print(i)
    
    
    InputIdPemberi = input("Masukkan Id Pemberi Zakat : ")
    
    return read_pemberi(InputIdPemberi)[0][0]

def InputKeteranganZakat():
    
    
    print("[(1) Zakat Fitrah], [(2) Zakat Mal]")
    
    InputJenisZakat = input("Masukkan Jenis Zakat : ")
    
    
    while InputJenisZakat:
        
        match InputJenisZakat:
            
            case "1":
                
                
                print("[(1) Beras], [(2) Uang]")
                InputBentukZakat = input("Masukkan Bentuk Zakat : ")
                
                
                while InputBentukZakat:
                    
                    match InputBentukZakat:
                        
                        case "1":
                            JumlahZakat = int(input("Masukkan Jumlah dalam Gram (Gr): "))
                            break
                        
                        case "2":
                            JumlahZakat = int(input("Masukkan Jumlah dalam Ribuan (Rp): "))
                            break
                        
                        case _:
                            print("InputSalah")
                break
            
            case "2":
                
                
                print("[(2) Uang], [(2) Emas]")
                InputBentukZakat = input("Masukkan Bentuk Zakat : ")
                
                
                while InputBentukZakat:
                    
                    match InputBentukZakat:
                        
                        case "2":
                            JumlahZakat = int(input("Masukkan Jumlah dalam Ribuan (Rp): "))
                            break
                        
                        case "3":
                            JumlahZakat = int(input("Masukkan Jumlah dalam Gram (Gr): "))
                            break
                        
                        case _:
                            print("InputSalah")
                            
                break
            
            case _:
                print("InputSalah")
                
    return InputJenisZakat, InputBentukZakat, JumlahZakat

def Edit_pembayaran(akun, NamaTabel, NamaKolom):
    
    Notifikasi = ''
    
    while True:
        
        clear_screen()
        
        print("Edit Pembayaran")

        if len(Notifikasi) > 0:
            print(Notifikasi)
            
        Konfirmasi = input("Masukkan 0 untuk keluar dari fitur : ")
        
        if Konfirmasi == '0':
            return -1
        
        elif len(Konfirmasi) > 0 and Konfirmasi != '0':
            Notifikasi = "Input tidak valid"
            
            continue
        
        for i in read_pembayaran_with_join():
            print(i)
            
        InputIdPembayaran = input("Masukkan Id Pembayaran : ")
        DataTerpanggil = read_pembayaran_with_join(InputIdPembayaran)
        if DataTerpanggil:
            print('Data saat ini:')
            print(f'id pembayaran zakat saat ini : {DataTerpanggil[0][0]}')
            print(f'nama pemberi zakat saat ini: {DataTerpanggil[0][1]}')
            print(f'jumlah pemberian zakat saat ini: {DataTerpanggil[0][2]}')
            print(f'tanggal pemberian zakat : {DataTerpanggil[0][3]}')
            print(f'jenis zakat saat ini: {DataTerpanggil[0][4]}')
            print(f'bentuk zakat saat ini: {DataTerpanggil[0][5]}')
            print(f'pengurus pembayaran : {DataTerpanggil[0][6]}')
            
            Konfirmasi = input("Tekan Enter Bila Data Sudah Benar, Tekan 0 Untuk Batal")
            
            if Konfirmasi.lower() == "0":
                continue
            else:
                DataTerpanggil = read_pembayaran(InputIdPembayaran)
        else:
            Konfirmasi = "Data tidak ditemukan"
            continue
        
        
        # [(26, 2500, datetime.date(2024, 5, 21), 1, (3), 1, 1)]
        Id_Pemberi = InputNamaPemberi() or DataTerpanggil[0][4]
        Jenis_Zakat = UpdateJenisZakat() or DataTerpanggil[0][6]
        Bentuk_Zakat = UpdateBentukZakat(Jenis_Zakat) or DataTerpanggil[0][5]
        Jumlah_Pemberian = UpdateJumlahZakat(Bentuk_Zakat) or DataTerpanggil[0][1]
        
        
        Query = f"id_pemberi_zakat = {Id_Pemberi}, id_jenis_zakat = {Jenis_Zakat}, id_bentuk_zakat = {Bentuk_Zakat}, besar_pemberian = {Jumlah_Pemberian} where id_pembayaran = {InputIdPembayaran}"
        
        Update_data(NamaTabel, Query)
        
        Notifikasi = "Data Berhasil Diubah"
        
def UpdateBentukZakat(Jenis_Zakat):
    
    Notifikasi = ''
    
    while True:
        
        if len(Notifikasi) > 0:
            print(Notifikasi)
        
        if Jenis_Zakat == 1:
            print("[(1) Beras], [(2) Uang]")
            InputBentukZakat = input("Masukkan Bentuk Zakat : ")
            match InputBentukZakat:
                case "":
                    return None
                case "1":
                    return 1
                case "2":
                    return 2
                case _:
                    Notifikasi = "Input tidak valid"
                    continue
        elif Jenis_Zakat == 2:
            print("[(2) Uang], [(3) Emas]")
            InputBentukZakat = input("Masukkan Bentuk Zakat : ")
            match InputBentukZakat:
                case "":
                    return None
                case "2":
                    return 2
                case "3":
                    return 3
                case _:
                    Notifikasi = "Input tidak valid"
                    continue

def UpdateJumlahZakat(Bentuk_Zakat):
    
    Notifikasi = ''
    
    while True:
        
        if len(Notifikasi) > 0:
            print(Notifikasi)
        
        match Bentuk_Zakat:
            case 1:
                JumlahZakat = input("Masukkan Jumlah dalam Gram (Gr): ")
                match JumlahZakat:
                    case "":
                        return None
                    case _:
                        return int(JumlahZakat)
            case 2:
                JumlahZakat = input("Masukkan Jumlah dalam Ribuan (Rp): ")
                match JumlahZakat:
                    case "":
                        return None
                    case _:
                        return int(JumlahZakat)
            case 3:
                JumlahZakat = input("Masukkan Jumlah dalam Gram (g): ")
                match JumlahZakat:
                    case "":
                        return None
                    case _:
                        return int(JumlahZakat)
            case _:
                Notifikasi = "Input tidak valid"
                continue

def UpdateJenisZakat():
    
    Notifikasi = ''
    
    while True:
        
        if len(Notifikasi) > 0:
            print(Notifikasi)
        
        print("[(1) Zakat Fitrah], [(2) Zakat Mal]")
        
        InputJenisZakat = input("Masukkan Jenis Zakat : ")
        match InputJenisZakat:
            case "":
                return None
            case "1":
                return 1
            case "2":
                return 2
            case _:
                Notifikasi = "Input tidak valid"
                continue
        

def UpdateNamaPemberi():
    
    
    for i in read_pemberi():
        print(i)
    
    
    InputIdPemberi = input("Masukkan Id Pemberi Zakat : ")
    
    if InputIdPemberi:
        return read_pemberi(InputIdPemberi)[0][0]
    elif not InputIdPemberi:
        return None
        
        
        
    
    
    
    
    