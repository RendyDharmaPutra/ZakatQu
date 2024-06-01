def validate_amil(data) :
    message: str = ''

    if data[0].isalnum() or data[0].isnumeric() :
        message = "Nama tidak boleh mengandung Angka!"
    elif data[1].isalnum() or data[1].isalpha() :
        message = "NIK tidak boleh mengandung Huruf!"
    elif data[3].isalnum() or data[3].isalpha() :
        message = "RT/RW tidak boleh mengandung Huruf!"
    elif data[4].isalnum or data[4].isalpha() :
        message = "Nomor Telepon tidak boleh mengandung Huruf!"
    

    return message