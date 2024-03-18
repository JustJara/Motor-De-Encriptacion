import sys
sys.path.append('src')

from tests import test_cases

# Importamos la la libreria de encriptacion PyCryptodome

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# Definimos la clase para capturar la excepcion de un mensaje vacio
class EmptyEncryptMessage(Exception):
    pass

# Definimos la clase para capturar la excepcion de una clave secreta invalida
class InvalidSecretKey(Exception):
    pass

# Definimos la clase para capturar la excepcion de un mensaje no encriptado
class MessageIsNotEncrypted(Exception):
    pass

# Definimos la clase para capturar la excepcion de una clave secreta vacia
class EmptySecretKey(Exception):
    pass

# Definimos la clase para capturar la excepcion de un mensaje vacio
class EmptyInputValuesError(Exception):
    pass

# Definimos el metodo para encriptar un mensaje

def encrypt(secret_key, unencrypted_message):
    
    # Creamos un objeto de cifrado AES en modo CBC con la clave proporcionada para encriptar
    
    cipher = AES.new(secret_key, AES.MODE_CBC)

    # Encriptamos el mensaje con un padding para que tenga un tamaño multiplo de 16 bytes haciendo usa del AES.block_size, para hacer el desencriptado mas facil

    encripted_message : str = cipher.encrypt(pad(unencrypted_message, AES.block_size))

    return encripted_message

# Definimos el metodo para desencriptar un mensaje

def decrypt(secret_key, encrypted_message):

    # Se crea un objeto de cifrado AES en modo CBC con la clave proporcionada para desencriptar
    
    cipher = AES.new(secret_key, AES.MODE_CBC)

    #Desencriptamos el mensaje y eliminamos el padding

    decrypted_message : str = unpad(cipher.decrypt(encrypted_message), AES.block_size)

    return decrypted_message



