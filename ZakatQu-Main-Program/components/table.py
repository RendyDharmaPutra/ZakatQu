from rich.console import Console
from rich.table import Table
from rich.text import Text



def read_table(table_title, datas) :

    if table_title == "Data Amil" :
        column = ["id", "Nama", "NIK", "No Telepon"]


    console = Console()


    table = Table(title=table_title, show_header=True, header_style="bold")
    

    for idx, i in enumerate(column) :

        if idx < 1 :
            style = "cyan bold"
        else :
            style = "green"

        table.add_column(i, style=f"{style}", header_style="bold")


    for data in datas : 
        table.add_row(str(data[0]),data[1], data[2], data[-1])

    console.print(table)