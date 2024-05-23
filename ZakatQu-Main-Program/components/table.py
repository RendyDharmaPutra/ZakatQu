from rich.console import Console
from rich.table import Table
from rich.text import Text



def read_table(table_title, datas) :
    match table_title :
        case "Data Amil" :
            column = ["id", "Nama", "NIK", "No Telepon"]
        case "Data Pembayaran Zakat" :
            column = ['ID Pembayaran', 'pemberi zakat', 'Besar Pemberian', 'Tanggal Pemberian', 'Bentuk Zakat', 'Jenis Zakat', 'Nama Amil Pengurus']
        case "Data Pemberi":
            column = ['ID Pemberi', 'Nama Pemberi', 'NIK', 'Alamat', 'Nomor Telepon', 'RT/RW', 'Status Pembayaran']
    


    console = Console()


    table = Table(title=table_title, show_header=True, header_style="bold")
    

    for idx, i in enumerate(column) :

        if idx < 1 :
            style = "cyan bold"
        else :
            style = "green"

        table.add_column(i, style=f"{style}", header_style="bold")

    match table_title :
        case "Data Amil" :
            for data in datas : 
                table.add_row(str(data[0]),data[1], data[2], data[-1])
        case "Data Pembayaran Zakat" :
            for data in datas :
                table.add_row(str(data[0]), str(data[1]), str(data[2]), str(data[3]), str(data[4]), str(data[5]), str(data[6]))
        case "Data Pemberi" :
            for data in datas :
                table.add_row(str(data[0]), str(data[1]), str(data[2]), str(data[3]), str(data[4]), str(data[5]), str(data[6]))
                
    console.print(table)