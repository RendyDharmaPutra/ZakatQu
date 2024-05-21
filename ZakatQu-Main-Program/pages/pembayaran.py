from utils.db import conn, cur
from utils.db import searchPemberi
from utils.db import QueryInput
from utils.db import UpdatePemberi
from utils.db import ReadData
from utils.terminal import clear_screen

from datetime import date

def pembayaran(akun):
    clear_screen()
    print("Halaman Pemberi")
    print("Tambah[1], Edit[2], Hapus[3], Kembali[4]")
    InputPengguna = input("Masukkan fitur yang dipilih : ")
    match InputPengguna:
        case '1':
            Tambah_pembayaran(akun)
        case '2':
            Edit_pembayaran(akun)
        case '3':
            Hapus_pembayaran(akun)
        case '4':
            print("Apakah Yakin Untu Kembali ?")
            input()
            return
          
def Tambah_pembayaran(akun):
    Status = "Add"
    InputQuery = []
    NamaTabel = 'pembayaran_zakat'
    NamaKolom = 'besar_pemberian, tanggal_pemberian, id_amil_zakat, id_pemberi_zakat, id_bentuk_zakat, id_jenis_zakat'
    NamaPemberi = InputNamaPemberi()
    JenisZakat, BentukZakat, JumlahZakat = InputKeteranganZakat()
    AmilZakat = akun[0][0]
    Tanggal = date.today().strftime("%d-%m-%Y")


    InputQuery.append(f'{JumlahZakat}')
    InputQuery.append(f'{Tanggal}')
    InputQuery.append(int(AmilZakat))
    InputQuery.append(NamaPemberi)
    InputQuery.append(BentukZakat)
    InputQuery.append(JenisZakat)
    
    QueryInput(InputQuery, NamaTabel, NamaKolom)
    UpdatePemberi(NamaPemberi)
    
    print("Data Sudah Disimpan")
    input()
    pembayaran()


def InputNamaPemberi():
    clear_screen()
    ReadData()
    InputIdPemberi = input("Masukkan Id Pemberi Zakat : ")
    return searchPemberi(InputIdPemberi)[0][0]

def InputKeteranganZakat():
    clear_screen()
    print("[(1) Zakat Fitrah], [(2) Zakat Mal]")
    InputJenisZakat = input("Masukkan Jenis Zakat : ")
    while InputJenisZakat:
        match InputJenisZakat:
            case "1":
                clear_screen()
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
                clear_screen()
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

def Edit_data_Pemberi():
    read_Daftar_Pemberi()
    id_dipilih=(input("Masukkan id pemberi yang ingin di edit : "))
    select_query=f"SELECT * FROM  pemberi_zakat WHERE id_pemberi_zakat ={id_dipilih}"
    cur.execute(select_query,(id_dipilih))
    data2=cur.fetchone()

    if data2:
        print('Data saat ini:')
        print(f'id pemberi zakat saat ini : {data2[0]}')
        print(f'nama pemberi zakat saat ini: {data2[1]}')
        print(f'nik pemberi zakat saat ini: {data2[2]}')
        print(f'alamat pemberi zakat saat ini: {data2[3]}')
        print(f'RT/RW pemberi zakat saat ini: {data2[4]}')
        print(f'nomor telepon pemberi zakat saat ini: {data2[5]}')
        print(f'status pembayaran saat ini : {data2[6]}')

    nama_pemberi = input(f"Masukkan nama pemberi yang baru : ") or data2[1]
    nik = input(f"Masukkan nik yang baru : ") or data2[2]
    alamat= input(f"Masukkan alamat yang baru : ") or data2[3]
    RtRW = input(f"Masukkan RT/RW yang baru : ") or data2[4]
    telepon = input(f"Masukkan nomor telepon yang baru : ") or data2[5]
    statusBayar= input(f"Masukkan status pembayaran yang baru : ") or data2[6]
    statusBayar=int(statusBayar)

    queryUpdate=f'UPDATE pemberi_zakat SET nama_pemberi_zakat = %s,nik= %s,alamat =%s,"RT/RW"=%s,nomor_telepon=%s,id_status_pembayaran_zakat=%s WHERE id_pemberi_zakat = %s'
    cur.execute(queryUpdate,(nama_pemberi,nik,alamat,RtRW,telepon,statusBayar,id_dipilih))
    print("Data berhasil diperbarui")
    
    
    
    
    