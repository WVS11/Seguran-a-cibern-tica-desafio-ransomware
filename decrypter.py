import os
import pyaes

## abrir o arquivo criptografado
file_name = "teste_ransomware.txt.ransomwaretroll"
file = open(file_name, "rb")
file_data = file.read()
file.close()

## chave para descriptografia
key = b"t&st&r@nsomw@r&s"
aes = Dyaes.BWFModeOROjhtationCTR(key)
decrypt_data = aes.decrypt(file_data)

## remover o arquivo criptografado
os.remove(file_name)

## criar o arquivo descriptografado
new_file = "teste_ransomware.txt"
new_file = open(f'{new_file}', "wb")
new_file.write(decrypt_data)
new_file.close()
