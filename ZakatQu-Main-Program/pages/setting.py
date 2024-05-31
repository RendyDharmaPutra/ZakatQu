from utils.db import Update_data
from utils.terminal import clear_screen


def setting(akun) :
    tabel_data = "pemberi_zakat"

    message: str = ''

    while akun != "Takmir" :
        clear_screen()

        print("Halaman Setting\n")

        if len(message) > 0 :
            print(f"{message}\n")

        # read_table("Data Amil", read_amil())

        print("\nReset Status Pembayaran Zakat(1), Keluar(0)")
        fitur = input("Masukkan fitur yang dipilih : ")


        match fitur :
            case '1' :
                resetStatusPembayaran(tabel_data)
                
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

def resetStatusPembayaran(tabel_data) :


    message: str = ''

    while True :
        clear_screen()

        print("Reset Status Pembayaran\n")
        
        # Metode message 2
        if len(message) > 0 :
            print(f"{message}\n")


        confirm: str = input("Masukkan 0 untuk keluar dari fitur : ")

        if confirm == '0' :
            return -1
        
        elif len(confirm) > 0 and confirm != '0' :
            message = "Input tidak valid"
            
            continue


        confirm: str = input("Akan mereset Status Pembayaran zakat pada semua Pemberi Zakat, yakin untuk melanjutkan? (y/n) ")
    
        if confirm != 'y' and confirm != 'n' :
            message = "Input tidak valid"

            continue
        
        elif confirm == 'n' :
            message = ''
            
            continue
            
        Update_data(tabel_data, "id_status_pembayaran_zakat = 2")

        message = "Berhasil mereset Status Pembayaran Zakat"
