from utils.db import conn, cur, read_distribusi_with_join, read_penerima, read_penerima_in_distribusi, Read_Banyak_Zakat, Read_Banyak_Zakat_From_Distribusi, QueryInput, Update_data, read_distribusi, read_detail_distribusi, Delete_data
from components.table import read_table
from utils.terminal import clear_screen


def distribusi(akun):
    tabel_data = "distribusi_zakat"
    kolom_data = 'id_amil_zakat, id_status_distribusi, id_penerima_zakat'

    message: str = ''

    while True :
        clear_screen()

        print("Halaman Distribusi\n")

        if len(message) > 0 :
            print(f"{message}\n")

        read_table("Data Distribusi", read_distribusi_with_join())
        
        if akun == 'Takmir' :
            input()
            return

        print("((1) Tambah Data Distribusi, (2) Edit Data Penerima, (3) Hapus Data Distribusi,(0) Keluar")
        fitur = input("Masukkan fitur yang dipilih : ")


        match fitur :
            case '1' :
                memasukkan_semua_data(tabel_data, kolom_data, akun)
            case '2' :
                edit_data_distribusi(tabel_data, kolom_data, akun)
            case '3' :
                delete_data_distribusi(tabel_data, kolom_data)               
            case '0' :
                confirm: str = input("Masukkan 0 untuk keluar ke Halaman Utama : ")

                if confirm == '0' :
                    break

                elif len(confirm) > 0 and confirm != '0' :
                    message = "Input tidak valid"

                    continue

            case _ :
                message = "Input tidak valid"

                continue
        
        message = '' 
        
def memasukkan_semua_data(tabel_data, kolom_data, akun):
    
    TabelDetail = 'detail_distribusi_zakat'
    KolomDetail = 'jumlah_zakat, id_distribusi_zakat, id_bentuk_zakat'
    
    message: str = ''

    while True :
        queryInput = []
    
        data_baru: list[str] = []
        
        
        clear_screen()

        print("Memasukkan Semua Data\n")
        
        # Metode message 2
        if len(message) > 0 :
            print(f"{message}\n")


        confirm = input("Masukkan 0 untuk keluar dari fitur : ")

        if confirm == '0' :
            return
        
        elif len(confirm) > 0 and confirm != '0' :
            message = "Input tidak valid"
            
            continue
        try:
            read_table("Data Penerima", read_penerima())
        except:
            read_table("Data Penerima", None)
        
        DataJumlahZakat = Hitung_Jumlah_Zakat()
        if DataJumlahZakat[0][1] == 0 and DataJumlahZakat[1][1] == 0 and DataJumlahZakat[2][1] == 0:
            message = "Data Zakat Tidak Ada"
            continue
        
        InputPenerima = input("Masukkan ID Penerima = ")
        
        try:
            if read_penerima('', InputPenerima)[0][0] == read_penerima_in_distribusi(InputPenerima)[0][3]:
                message = "Data Distribusi Sudah Ada"
                continue
        except:
            pass


        queryInput.append(akun[0][0])
        queryInput.append(2)
        try: 
            queryInput.append(int(InputPenerima))
        except:
            message = "Data Penerima Tidak Valid"
            continue
        
        Konfirmasi = input("Tekan Enter Untuk Simpan Data, Tekan 0 Untuk Batal")
        
        if Konfirmasi.lower() == "0":
            continue
        
        else:
            QueryInput(queryInput, tabel_data, kolom_data)
        
        IdDistribusi = int(read_penerima_in_distribusi(InputPenerima)[0][0])

        for i in range(len(DataJumlahZakat)):
            read_table("Data Banyak Zakat", Hitung_Jumlah_Zakat())
            queryInput = []
            BentukZakat = 0
            msg = ''
            while True: 
                match i:
                    case 0:
                        Input = input("Masukkan Jumlah Beras (Gram) = ") or '0'
                        BentukZakat = 1
                    case 1:
                        Input = input("Masukkan Jumlah Uang (Ribuan) = ") or '0'
                        BentukZakat = 2
                    case 2:
                        Input = input("Masukkan Jumlah Emas (Gram) = ") or '0'
                        BentukZakat = 3

                if int(Input) > DataJumlahZakat[i][1]:
                    msg = "Jumlah yang anda berikan terlalu besar"
                    continue
                        
                queryInput.append(int(Input))
                queryInput.append(IdDistribusi)
                queryInput.append(BentukZakat)
                QueryInput(queryInput, TabelDetail, KolomDetail)

                break

        
        Konfirmasi = input("Apakah Distribusi Telah di Berikan ? (Y/N)")
        
        match Konfirmasi.upper():
            case "Y":
                Update_data(tabel_data, f"id_status_distribusi = 1 where id_distribusi_zakat = {IdDistribusi}")
            case "N":
                continue
        message = "Data Telah Tersimpan"
        
    return
            
        
def Hitung_Jumlah_Zakat():
    
    Zakat = Read_Banyak_Zakat()
    Diterima = Read_Banyak_Zakat_From_Distribusi()
    
    Datas = []
    
    for j, i in enumerate(Zakat):
        if Diterima[j][1] is None:
            Besar = 0
            if i[1] != None:
                Besar = i[1] - 0
            Datas.append([i[0], Besar])
            continue
        if i[1] != None:
            Besar = i[1] - Diterima[j][1]
        else:
            Besar = 0
        Datas.append((i[0], Besar))
    
    return Datas

def edit_data_distribusi(tabel_data, kolom_data, akun):
    Notifikasi = ''
    
    while True:
        
        clear_screen()
        
        print("Edit Data Distribusi Zakat")

        if len(Notifikasi) > 0:
            print(Notifikasi)
            
        Konfirmasi = input("Masukkan 0 untuk keluar dari fitur : ")
        
        if Konfirmasi == '0':
            return
        
        elif len(Konfirmasi) > 0 and Konfirmasi != '0':
            Notifikasi = "Input tidak valid"
            
            continue
        
        read_table("Data Distribusi", read_distribusi_with_join())
        
        Input = input("Masukkan id distribusi yang ingin diubah : ")
        
        if not Input:
            Notifikasi = "Input Tidak Valid"
            continue
        
        try:
            Data = read_distribusi(Input)
            DataLama = Data[0][3]
            IdAmil = Data[0][1]
            StatusDistribusi = 2
            Penerima = Update_Penerima() or Data[0][3]
        except:
            Notifikasi = "Data Penerima Tidak Valid"
            continue
        try: 
            if Penerima == DataLama:
                Penerima = DataLama
            elif read_penerima('', str(Penerima))[0][0] == read_penerima_in_distribusi(str(Penerima))[0][3]:
                message = "Data Distribusi Sudah Ada"
                continue
        except: 
            Update_data(tabel_data, f"id_amil_zakat = {IdAmil}, id_penerima_zakat = {Penerima}, id_status_distribusi = {StatusDistribusi} where id_distribusi_zakat = {Input}")

        
        for i in range(3):
            read_table("Data Banyak Zakat", Hitung_Jumlah_Zakat())
            Notifikasi = ''
            BentukZakat = 0
            while True:
                if len(Notifikasi) > 0:
                    print(Notifikasi)
                    input()
                match i:
                    case 0:
                        BentukZakat = 1
                        TabelDetail = read_detail_distribusi(Input, BentukZakat)[0][1]
                        InputJumlah = input("Masukkan Jumlah Beras (Gram) = ") or TabelDetail
                        if int(InputJumlah) > Hitung_Jumlah_Zakat()[0][1]:
                            Notifikasi = "Jumlah yang anda berikan terlalu besar"
                            continue
                    case 1:
                        BentukZakat = 2
                        TabelDetail = read_detail_distribusi(Input, BentukZakat)[0][1]
                        InputJumlah = input("Masukkan Jumlah Uang (Ribuan) = ") or TabelDetail
                        if int(InputJumlah) > Hitung_Jumlah_Zakat()[1][1]:
                            Notifikasi = "Jumlah yang anda berikan terlalu besar"
                            continue
                    case 2:
                        BentukZakat = 3
                        TabelDetail = read_detail_distribusi(Input, BentukZakat)[0][1]
                        InputJumlah = input("Masukkan Jumlah Emas (Gram) = ") or TabelDetail
                        if int(InputJumlah) > Hitung_Jumlah_Zakat()[2][1]:
                            Notifikasi = "Jumlah yang anda berikan terlalu besar"
                            continue
                
                Update_data("detail_distribusi_zakat", f"jumlah_zakat = {InputJumlah} where id_distribusi_zakat = {Input} and id_bentuk_zakat = {BentukZakat}")
                break
        
        Konfirmasi = input("Apakah Distribusi Telah di Berikan ? (Y/N)")
        
        match Konfirmasi.upper():
            case "Y":
                Update_data(tabel_data, f"id_status_distribusi = 1 where id_distribusi_zakat = {Input}")
            case "N":
                continue
        Notifikasi = "Data Telah Tersimpan"
        
    return
            
        
        
def Update_Penerima():
    read_table("Data Penerima", read_penerima())
    
    Input = input("Masukkan ID Penerima = ")
    if Input:
        Data = read_penerima('', Input)[0][0]
    else:
        Data = None
    
    return Data


def delete_data_distribusi(tabel_data, kolom_data):
    Notifikasi = ''
    
    while True:
        
        clear_screen()
        
        print("Edit Data Distribusi Zakat")

        if len(Notifikasi) > 0:
            print(Notifikasi)
            
        Konfirmasi = input("Masukkan 0 untuk keluar dari fitur : ")
        
        if Konfirmasi == '0':
            return
        
        elif len(Konfirmasi) > 0 and Konfirmasi != '0':
            Notifikasi = "Input tidak valid"
            
            continue
        
        read_table("Data Distribusi", read_distribusi_with_join())
        
        Input = input("Masukkan id distribusi yang ingin diubah : ")
        
        if not Input:
            Notifikasi = "Input Tidak Valid"
            continue
        
        Konfirmasi = input("Tekan Enter Untuk Hapus Data, Tekan 0 Untuk Batal")
        
        if Konfirmasi.lower() == "0":
            continue
        
        try: 
            Delete_data("detail_distribusi_zakat", "id_distribusi_zakat", Input)
            Delete_data(tabel_data, "id_distribusi_zakat", Input)
        except:
            Notifikasi = "Data Tidak Dapat Ditemukan"
            continue
        
        Notifikasi = "Data Telah Terhapus"
    
    return
        
            
        
        