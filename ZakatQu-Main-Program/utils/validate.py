def validate_amil(data) :
    message: str = ''

    for idx, i in enumerate(data) :
        match idx :
            case 0 :
                kolom_data = "Nama"
            case 1 :
                kolom_data = "NIK"
            case 2 :
                kolom_data = "Alamat"
            case 3 :
                kolom_data = "RT/RW"
            case 4 :
                kolom_data = "Nomor Telepon"

        if len(i) == 0 :
            message = f"{kolom_data} tidak boleh kosong!"

    if data[0].isalnum() or data[0].isnumeric() :
        message = "Nama tidak boleh mengandung Angka!"
    elif data[1].isalnum() or data[1].isalpha() :
        message = "NIK tidak boleh mengandung Huruf!"
    elif data[3].isalnum() or data[3].isalpha() :
        message = "RT/RW tidak boleh mengandung Huruf!"
    elif data[4].isalnum or data[4].isalpha() :
        message = "Nomor Telepon tidak boleh mengandung Huruf!"
    

    return message


def validate_empty(data) :
    message: str = ''

    if len(data[0])==0 :
        message = "Nama tidak boleh kosong!"
    elif len(data[1])==0 :
        message = "NIK tidak boleh kosong!"
    elif len(data[2])==0 :
        message = "Alamat tidak boleh kosong!"
    elif len(data[3])==0 :
        message = "RT/RW tidak boleh kosong!"
    elif len(data[4])==0:
        message = "Nomor Telepon tidak boleh kosong!"

    return message

        