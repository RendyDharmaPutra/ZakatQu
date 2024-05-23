from utils.terminal import clear_screen
from utils.db import read_pemberi
# from utils.db import Tambah_data_Pemberi
# from utils.db import Edit_data_Pemberi
# from utils.db import Hapus_data_Pemberi
from components.table import read_table
from utils.db import cur,conn
from utils.db import QueryInput
from utils.db import Delete_data
from utils.db import Update_data

def pemberi():
    KolomPemberi='nama_pemberi_zakat,nik,alamat,"RT/RW",nomor_telepon,id_status_pembayaran_zakat'
    Pemberi='pemberi_zakat'

    print("Halaman Pemberi")

    read_table("Data Pemberi", read_pemberi())
        
    print("Tambah[1], Edit[2], Hapus[3]")
    pilihan=input("Masukkan fitur yang dipilih : ")
    match pilihan:
        case '1':
            Tambah_data_Pemberi(KolomPemberi,Pemberi)
        case '2':
            Edit_data_Pemberi(KolomPemberi,Pemberi)
        case '3':
            Hapus_data_Pemberi(KolomPemberi,Pemberi)
        case'0':
            print('Apakah anda yakin untuk kembali?')
            input()
            return -1
        case _:
            print("Input tidak valid")


def Tambah_data_Pemberi(KolomPemberi,Pemberi):
    msg=''
    while True:
        query_input=[]


        clear_screen()

        print("Tambah Daftar Pemberi")

        if len(msg) > 0:
            print(msg)

        Konfirmasi=input("Ketik 0 untuk kembali, [enter] untuk lanjut : ")

        if Konfirmasi=='0':
            pemberi()

        elif len(Konfirmasi) > 0 and Konfirmasi != '0':
            msg = "Input tidak valid"   
            continue


        nama_pemberi = input("Masukkan nama pemberi zakat : ")
        nik_pemberi=input("Masukkan NIK pemberi zakat : ")
        alamat_pemberi=input("Masukkan alamat pemberi zakat : ")
        RtRw_pemberi=input("Masukkan RT/RW pemberi zakat : ")
        telepon_pemberi= input("Masukkan nomor telepon pemberi zakat : ")
        status_bayar=2

        query_input.append(f'{nama_pemberi}')
        query_input.append(f'{nik_pemberi}')
        query_input.append(f'{alamat_pemberi}')
        query_input.append(f'{RtRw_pemberi}')
        query_input.append(f'{telepon_pemberi}')
        query_input.append(status_bayar)

        Konfirmasi = input("Tekan Enter Untuk Simpan Data, Tekan 0 Untuk Batal")
        
        if Konfirmasi.lower() == "0":
            pemberi()
        
        else:
            QueryInput(query_input,Pemberi,KolomPemberi)
            print("Data Berhasil Disimpan")

        return nik_pemberi
    

def Edit_data_Pemberi(KolomPemberi,Pemberi):
    msg=''
    while True:
        

        clear_screen()

        print("Edit Daftar Pemberi")

        if len(msg) > 0:
            print(msg)

        Konfirmasi=input("Ketik 0 untuk kembali, [enter] untuk lanjut : ")

        if Konfirmasi=='0':
            pemberi()

        elif len(Konfirmasi) > 0 and Konfirmasi != '0':
            msg = "Input tidak valid"   
            continue

        read_table("Data Pemberi", read_pemberi())

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
        statusBayar=2


        Konfirmasi = input("Tekan Enter Untuk Simpan Data, Tekan 0 Untuk Batal")
        
        if Konfirmasi.lower() == "0":
            pemberi()
        
        else:
            Update_data(Pemberi,f"nama_pemberi_zakat='{nama_pemberi}',nik='{nik}',alamat='{alamat}',\"RT/RW\"='{RtRW}',nomor_telepon='{telepon}',id_status_pembayaran_zakat={statusBayar} WHERE id_pemberi_zakat={id_dipilih}")
            msg="Data Berhasil Diubah"

        return nik

def Hapus_data_Pemberi(KolomPemberi,Pemberi):
    msg=''
    while True:
        

        clear_screen()

        print("Hapus Data Pemberi")

        if len(msg) > 0:
            print(msg)

        Konfirmasi=input("Ketik 0 untuk kembali, [enter] untuk lanjut : ")

        if Konfirmasi=='0':
            pemberi()

        elif len(Konfirmasi) > 0 and Konfirmasi != '0':
            msg = "Input tidak valid"   
            continue

        read_table("Data Pemberi", read_pemberi())
        idPemberi = input('Masukkan id Pemberi yang ingin dihapus: ')
        Konfirmasi=input(f"Apakah anda yakin untuk menghapus Data nomor {idPemberi}?[y/n]")
        
        if Konfirmasi!='y':
            continue

        Delete_data(Pemberi,"id_pemberi_zakat",idPemberi)
        msg="Data Berhasil Dihapus"
