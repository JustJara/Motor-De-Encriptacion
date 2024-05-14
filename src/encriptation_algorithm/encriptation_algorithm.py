'''
File with the encriptation algorithm logic

Archivo con la lógica del algoritmo de encriptación
'''
import psycopg2
import sys
import random
import math
import re

sys.path.append('encryption_engine/src') 
from controller.database_controller import DatabaseController

class EmptyMessageError(Exception):
    '''

    Custom exception to indicate that the entered message cannot be empty

    Excepción personalizada para indicar que el mensaje ingresado no puede estar vacío

    '''
    def __init__(self):

        '''

        To raise this exception, the message entered must be empty

        Para lanzar esta excepción, el mensaje ingresado debe estar vacío

        '''
        self.message = 'El mensaje ingresado no puede estar vacío'

    def __str__(self) -> str:
        return (self.message)

class InvalidPublicKey(Exception):
    '''

    Custom exception to indicate that the entered public key is invalid


    Excepción personalizada para indicar que la clave pública ingresada es inválida

    '''
    def __init__(self,message: str = 'La clave pública debe ser ingresada como una lista de tres números separados por comas. Ejemplo: [123, 456, 789]'):

        '''
        To raise this exception, the entered public key must be invalid

        Para lanzar esta excepción, la clave pública ingresada debe ser inválida

        '''
        super().__init__()
        
        self.message = message

    def __str__(self) -> str:
        return self.message

class EmptyPublicKey(Exception):
    '''
    
    Custom exception to indicate that the entered public key is empty


    Excepción personalizada para indicar que la clave pública ingresada está vacía

    '''
    def __init__(self):
        '''
        
        To raise this exception, the entered public key must be empty

        Para lanzar esta excepción, la clave pública ingresada debe estar vacía

        '''
        super().__init__()
        self.message = 'La clave no puede estar vacía, intente ingresando una clave válida: ej. [123, 456, 789]'

    def __str__(self) -> str:
        return self.message

class NonPrimeNumber(Exception):
    '''
    
    Custom exception to indicate that the entered numbers are not prime

    Excepción personalizada para indicar que los números ingresados no son primos
    
    '''
    def __init__(self):
        '''
        To raise this exception, the entered numbers must not be prime
        
        Para lanzar esta excepción, los números ingresados no deben ser primos
        '''
        super().__init__()
        self.message = 'Los números ingresados no son primos. Recuerde que un número primo es divisible por si mismo y por 1 únicamente'

    def __str__(self) -> str:
        return self.message
    
class ExistingUser(Exception):

    '''
    Custom exception to indicate that the entered username has been already registered

    Excepción personalizada para indicar que el nombre de usuario ingresado ya ha sido registrado
    '''

    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self.message = 'El nombre de usuario ingresado ya ha sido registrado anteriormente. Intente ingresando otro nombre de usuario'

    def __str__(self) -> str:
        return self.message
class EmptyInputValuesError(Exception):
    '''

    Custom exception to indicate that the entered values are empty

    Excepción personalizada para indicar que los valores ingresados están vacíos

    '''
    def __init__(self):
        '''
        
        To raise this exception, a entered value must be empty
        
        Para lanzar esta excepción, un valor ingresado debe estar vacío

        '''
        super().__init__()
        self.message = 'No puedes dejar espacios vacíos, intenta ingresando valores en cada campo'

    def __str__(self) -> str:
        return self.message

class User:
    '''
    Allows the creation of a user object with a username and password for data storage.

    Permite la creación de un objeto de tipo usuario con un nombre de usuario y una contraseña para el almacenamiento de datos.
    '''

    def __init__(self,username: str, password: str):

        self.username : str = username
        self.password : str = password
        self.encrypted_messages : dict = {}        

class EncriptationEngine:
    '''

    Class for the encryption and decryption of messages using the RSA algorithm


    Clase para la encriptación y desencriptación de mensajes utilizando el algoritmo RSA

    '''

    def __init__(self):


        # Conjunto de números primos donde se seleccionarán de forma aleatoria los números primos p y q
        self.prime_set : set = set()

        # Número aleatorio entre 1 y  phi ((prime1 - 1) * (prime2 - 1))
        self.public_key : int = None

        # Inverso de la public_key en modulo phi ((prime1 - 1) * (prime2 - 1))
        self.private_key : int = None

        # Producto entre dos números primos diferentes
        self.RSA_module: int = None

        self.phi : int = None
        default_user = User('admin','admin')
        self.current_user : User = default_user
        self.db_controller = DatabaseController()
        self.create_table()

    def create_table(self):
        '''
        Creates the table in the database

        Crea la tabla en la base de datos
        '''
        try:
            self.db_controller.create_table()
            return True
        except psycopg2.errors.DuplicateTable as error:
            print('La tabla ya existe en la base de datos')
            return False
            

    def delete_table(self):
        '''
        Deletes the table in the database

        Elimina la tabla en la base de datos
        '''
        self.db_controller.delete_table()

    

    def register_user(self, username: str, password: str) -> bool:
        '''
        Registers a user with a username and password

        Registra un usuario con un nombre de usuario y una contraseña

        Parameters
        ----------

        username : str
            Username to be registered /
            Nombre de usuario a registrar

        password : str
            Password to be registered /
            Contraseña a registrar

        Returns
        -------

        user : User
            User object created with the username and password /
            Objeto de tipo usuario creado con el nombre de usuario y la contraseña
        '''

        # Verifica si el usuario ya existe en la base de datos
        if self.db_controller.check_username_existence(username) == None:

            user : User = User(username, password)

            user_inserted = self.db_controller.register_user_db(user)
            if user_inserted:
                print('Usuario registrado con éxito')
                return True

        else:
            raise psycopg2.errors.UniqueViolation('El nombre de usuario está asociado a otra cuenta. Intente ingresando un nombre de usuario diferente o iniciando sesión.')
        
    def login_user(self,username:str,password:str) -> bool:
        '''
        Logs in a user with a username and password

        Inicia sesión de un usuario con un nombre de usuario y una contraseña

        Parameters
        ----------

        username : str
            Username to be logged in /
            Nombre de usuario a iniciar sesión

        password : str
            Password to be logged in /
            Contraseña a iniciar sesión

        Returns
        -------

        user : User
            User object created with the username and password /
            Objeto de tipo usuario creado con el nombre de usuario y la contraseña
        '''
        user = User(username,password)
        login_user_status = self.db_controller.login_user_db(user)
        if login_user_status == False:
            raise Exception('La contraseña ingresada no es correcta. Intente nuevamente.')
        else:
            self.current_user = user
            return True

    def log_out(self):
        '''
        Logs out the current user

        Cierra sesión del usuario actual
        '''
        self.current_user = User('admin','admin')
        print('Cierre de sesión exitoso')

    def save_user_message(self,secret_key,encrypted_message,original_message):
        '''
        Saves the user message in the database

        Guarda el mensaje del usuario en la base de datos

        Parameters
        ----------

        secret_key : str
            Secret key to be stored in the database /
            Clave secreta a almacenar en la base de datos

        encrypted_message : list[int]
            Encrypted message to be stored in the database /
            Mensaje encriptado a almacenar en la base de datos

        original_message : str
            Original message to be stored in the database /
            Mensaje original a almacenar en la base de datos
        '''

        username = self.current_user.username
        self.db_controller.insert_user_messages(username,secret_key,encrypted_message,original_message)

    def get_user_messages(self):

        '''
        Gets the user messages from the database

        Obtiene los mensajes del usuario de la base de datos

        Returns
        -------

        user_messages : list
            List of user messages /
            Lista de mensajes del usuario
        '''

        username = self.current_user.username
        if username == 'admin':
            return []
        user_messages = self.db_controller.get_user_messages(username)
        return user_messages

    def change_user_passcode(self, old_password, new_password):
        '''
        Changes the user password in the database

        Cambia la contraseña del usuario en la base de datos

        Parameters
        ----------

        old_password : str
            Old password to be changed /
            Contraseña antigua a cambiar

        new_password : str
            New password to be stored in the database /
            Nueva contraseña a almacenar en la base de datos
        '''

        current_passcode = self.current_user.password
        if current_passcode != old_password:
            raise Exception('La contraseña actual no es correcta. Intente nuevamente.')
        if current_passcode == new_password:
            raise Exception('La nueva contraseña no puede ser igual a la anterior. Intente ingresando una nueva contraseña.')
        if new_password == '':
            raise Exception('La nueva contraseña no puede estar vacía. Intente ingresando una nueva contraseña.')
        else:
            username = self.current_user.username
            change_passcode_status = self.db_controller.change_user_passcode(username,new_password)
            if change_passcode_status:
                self.current_user.password = new_password
                print('Contraseña cambiada con éxito')
                return True
            return False

    def delete_user_messages(self):
        '''
        Deletes all the user messages in the database

        Elimina todos los mensajes del usuario en la base de datos
        '''

        username = self.current_user.username
        delete_status = self.db_controller.delete_user_messages(username)
        if delete_status:
            print('Mensajes eliminados con éxito')
            return True
        return False

    def fill_prime_set(self):
        '''

        Method used to fill the set of prime numbers: Sieve of Eratosthenes (a method to collect prime numbers)       

        Método utilizado para llenar el conjunto de números primos: Criba de Eratóstenes (un método para recopilar números primos)

        '''

        filtered_primes : list = [True] * 250

        filtered_primes[0] = False
        filtered_primes[1] = False

        # Asignar el valor False a los múltiplos de los números primos
        for i in range(2, 250):
            for j in range(i * 2, 250, i):
                filtered_primes[j] = False

        # El bucle for Llena el cojunto 'prime_set' con números primos
        for i in range(len(filtered_primes)):
            if filtered_primes[i]:
                self.prime_set.add(i)

    def pick_random_prime(self) -> int:
        '''
        
        Method used to choose a random prime number from prime_set and remove it from the set
        
        Método utilizado para elegir un número primo aleatorio de prime_set y eliminarlo del conjunto

        Returns
        -------
        random_prime_number : int

            Random prime number selected from the set /
            Número primo aleatorio seleccionado del conjunto

        '''

        random_number : int = random.randint(0, len(self.prime_set) - 1)
        iterable_set : set = iter(self.prime_set)

        for _ in range(random_number):
            next(iterable_set)

        # Seleccionar un número primo aleatorio y lo elimina del conjunto
        random_prime_number : int = next(iterable_set)
        self.prime_set.remove(random_prime_number)

        return random_prime_number

    def generate_public_and_private_key(self) -> list[int] :

        '''
        Generates the public and private keys for the RSA algorithm when user wants it to be generated by the program

        Genera las claves pública y privada para el algoritmo RSA cuando el usuario desea que sea generada por el programa

        Returns
        -------

        [ public_key, prime_number1, prime_number2 ] : list[int]
            Returns public key, prime number 1 and prime number 2 /
            Devuelve la clave pública, el número primo 1 y el número primo 2

        '''

        prime_number1 : int = self.pick_random_prime()
        prime_number2 : int = self.pick_random_prime()

        self.RSA_module = prime_number1 * prime_number2

        # El valor de la función multiplicativa de Euler φ(n) apartir de n 
        self.phi : int = (prime_number1 - 1) * (prime_number2 - 1)

        public_key : int = 2
        while True:
            if math.gcd(public_key, self.phi) == 1:
                break
            public_key += 1

        self.public_key = public_key

        # Asigna el valor del inverso de la llave pública en modulo phi
        private_key : int = self.generate_private_key_from_user_input(public_key, self.RSA_module)
        self.private_key = private_key

        return [self.public_key, prime_number1,prime_number2]
        
    def generate_private_key_from_user_input(self,public_key:int, phi: int) -> int:

        ''''
        
        Generates the private key for the RSA algorithm when the user wants to enter the public key

        Genera la clave privada para el algoritmo RSA cuando el usuario desea ingresar la clave pública

        Parameters
        ----------

        public_key : int
            Public key entered by the user /
            Clave pública ingresada por el usuario
        
        phi : int
            (prime_number1 - 1) * (prime_number2 - 1) /
            Euler's totient function value /
            Valor de la función totiente de Euler

        Returns
        -------

        private_key : int
            Returns the private key calculated /
            Devuelve la clave privada calculada
        '''

        # Halla el inverso de la llave pública en modulo phi
        self.public_key = public_key
        self.phi = phi
        private_key = 2
        while True:
            if (private_key * public_key) % phi == 1:
                break
            private_key += 1
        return private_key
    
    def encrypt_letter(self, unencrypted_message:int) -> int:
        '''
        Encrypts the letter given by the method encode_message

        Encripta la letra traída desde el método encode_message

        Parameters
        ----------

        unencrypted_message : int
            Encoded message to be encrypted /
            Mensaje codificado para encriptar

        Returns
        -------

        encrypted_message : int
            Encoded encrypted message /
            Mensaje encriptado codificado
        '''

        encrypted_message : str = ''

        #Se le asigna el valor de la llave pública a una variable temporal para controlar el ciclo
        temporal_public_key :int = self.public_key
        encrypted_message: int = 1

        #Ciclo para encriptar el mensaje
        while temporal_public_key > 0:
            encrypted_message *= unencrypted_message
            encrypted_message %= self.RSA_module
            temporal_public_key -= 1

        
        return encrypted_message

    def decrypt_letter(self, encrypted_letter : int,private_key,RSA_module) -> int:
        '''
        Decrypts the letter given from encode_message method

        Desencripta la letra dada del método encode_message

        Parameters
        ----------

        encrypted_letter : int
            Encrypted letter to be decrypted /
            Letra encriptada a desencriptar
        
        private_key : int
            Private key given by the user /
            Clave privada dada por el usuario

        RSA_module : int
            RSA module given by the user (product of different prime numbers) /
            Módulo RSA dado por el usuario (producto de números primos diferentes)

        Returns
        -------

        decrypted_letter : int
            Decrypted letter /
            Letra desencriptada
        '''

        temporal_private_key : int = private_key
        decrypted_letter : int = 1

        #Ciclo para desencriptar la letra
        while temporal_private_key > 0:
            decrypted_letter *= encrypted_letter
            decrypted_letter %= RSA_module
            temporal_private_key -= 1

        return decrypted_letter
    
    def encode_and_encrypt_message(self,message: str) -> list[int]:
        '''
        Encodes and encrypts the message entered by the user

        Codifica y encripta el mensaje ingresado por el usuario

        Parameters
        ----------

        message : str
            Message to be encrypted entered by the user /
            Mensaje a encriptar ingresado por el usuario


        Returns
        -------

        encrypted_message : list[int]
            Encoded and ecrypted message stored in a list of integers /
            Mensaje codificado y encriptado almacenado en una lista de números enteros

        Raises
        ------

        EmptyEncryptMessage
            When the entered message is empty /
            Cuando el mensaje ingresado está vacío

        '''
        
        #Valida si el mensaje no está vacío y lanza una excepción si lo está
        if message == '':
            raise EmptyMessageError
        else:
            encrypted_message : list = []

            # Ciclo para codificar y encriptar cada letra del mensaje de manera simultánea
            for letter in message:
                encrypted_message.append(self.encrypt_letter(ord(letter)))

            hexadecimal_encrypted_message = self.convert_decimal_to_hexadecimal(encrypted_message)
            return hexadecimal_encrypted_message
    
    def decode_and_decrypt_message(self,hexadecimal_encrypted_message : list[int], public_key : int ,prime_number1 : int,prime_number2 : int) -> str:
        '''
        Decodes and decrypts the message entered by the user

        Decodifica y desencripta el mensaje ingresado por el usuario
        
        Parameters
        ----------

        encrypted_message : list[int]
            Encoded and encrypted message given in a list of integers /
            Mensaje codificado y encriptado dado en una lista de números enteros

        public_key : int
            Public key given by the user /
            Clave pública dada por el usuario

        prime_number1 : int
            First prime number given by the user /
            Primer número primo dado por el usuario

        prime_number2 : int
            Second prime number given by the user /
            Segundo número primo dado por el usuario

        Returns
        -------

        decoded_message : str
            Decoded and decrypted message /
            Mensaje decodificado y desencriptado

        Raises
        ------

        EmptyInputValuesError
            When the entered values are empty /
            Cuando los valores ingresados están vacíos
        
        SyntaxError
            When the entered message is empty /
            Cuando el mensaje ingresado está vacío

        EmptyPublicKey
            When the entered public key is empty /
            Cuando la clave pública ingresada está vacía
        '''

        if prime_number1 == None or prime_number2 == None:
            raise EmptyInputValuesError
        if hexadecimal_encrypted_message == '':
            raise SyntaxError('El mensaje no puede estar vacío')

        if public_key == None:
            raise EmptyPublicKey
        else:
            
            encrypted_message = self.convert_hexadecimal_to_decima(hexadecimal_encrypted_message)
            decoded_message : str = ''

            private_key = self.generate_private_key_from_user_input(public_key, (prime_number1 - 1) * (prime_number2 - 1))
            RSA_module = prime_number1 * prime_number2
            for letter in encrypted_message:
                decoded_message += chr(self.decrypt_letter(letter,private_key,RSA_module))

            return decoded_message
    
    def secret_key_format_validator(self,secret_key) -> bool:
        '''
        Validates the format of the secret key entered by the user

        Valida el formato de la clave secreta ingresada por el usuario        

        Parameters
        ----------

        secret_key : str
            Secret key entered by the user /
            Clave secreta ingresada por el usuario  

        Returns
        -------

        bool
            Returns True if the secret key format is correct, otherwise raises an exception /
            Devuelve True si el formato de la clave secreta es correcto, de lo contrario lanza una excepción

        Raises
        ------

        InvalidPublicKey
            When the format is not valid /
            Cuando el formato no es válido
        '''
        # Definimos el patrón de la expresión regular
        patron = r'^\[\d+,\s*\d+,\s*\d+\]$'

        # Comprobamos si la cadena coincide con el patrón
        if re.match(patron, secret_key):
            return True
        else:
            raise InvalidPublicKey

    def encrypt_letter_with_inputs(self, unencrypted_letter:int, public_key, RSA_module) -> int:
            
            '''
            Encrypts the letter given by the metho encode_and_encrypt_message with the public key and RSA module given by the user

            Encripta la letra dada por el método encode_and_encrypt_message con la clave pública y el módulo RSA dados por el usuario

            Parameters
            ----------

            unencrypted_letter : int
                Encoded letter to be encrypted /
                Letra codificada a encriptar
            
            public_key : int
                Public key given by the user /
                Clave pública dada por el usuario

            RSA_module : int
                RSA module given by the user (product of different prime numbers) /
                Módulo RSA dado por el usuario (producto de números primos diferentes)

            Returns
            -------

            encrypted_message : int
                Encrypted letter /
                Letra encriptada
            '''

            encrypted_message : str = ''

            #Se le asigna el valor de la llave pública a una variable temporal para controlar el ciclo
            temporal_public_key :int = public_key
            encrypted_message: int = 1

            #Ciclo para encriptar el mensaje
            while temporal_public_key > 0:
                encrypted_message *= unencrypted_letter
                encrypted_message %= RSA_module
                temporal_public_key -= 1
    
            
            return encrypted_message

    def encode_and_encrypt_message_with_inputs(self,message: str, prime_number1, prime_number2,public_key) -> list[int]:

        '''
        Encodes and encrypts the message entered by the user with the public key and RSA module given by the user

        Codifica y encripta el mensaje ingresado por el usuario con la clave pública y el módulo RSA dados por el usuario

        Parameters
        ----------

        message : str
            Message to be encrypted entered by the user /
            Mensaje a encriptar ingresado por el usuario

        prime_number1 : int
            First prime number given by the user /
            Primer número primo dado por el usuario

        prime_number2 : int
            Second prime number given by the user /
            Segundo número primo dado por el usuario

        public_key : int
            Public key given by the user /
            Clave pública dada por el usuario

        Returns
        -------

        encrypted_message : list[int]
            Encoded and ecrypted message stored in a list of integers /
            Mensaje codificado y encriptado almacenado en una lista de números enteros
        
        Raises
        ------

        EmptyEncryptMessage
            When the entered message is empty /
            Cuando el mensaje ingresado está vacío
        
        EmptyInputValuesError
            When the entered values are empty /
            Cuando los valores ingresados están vacíos

        EmptyPublicKey
            When the entered public key is empty /
            Cuando la clave pública ingresada está vacía
        
        NonPrimeNumber
            When the entered numbers are not prime /
            Cuando los números ingresados no son primos
        '''
        
        #Valida si el mensaje no está vacío y lanza una excepción si lo está
        if message == '':
            raise EmptyMessageError
        if prime_number1 == None or prime_number2 == None:
            raise EmptyInputValuesError
        if public_key == None:
            raise EmptyPublicKey
        if self.is_prime(prime_number1)== False and self.is_prime(prime_number2) == False:
            raise NonPrimeNumber
        else:
            RSA_module = prime_number1 * prime_number2
            encoded_message : list = []
            for letter in message:
                encoded_message.append(self.encrypt_letter_with_inputs(ord(letter),public_key,RSA_module))

            hexadecimal_encrypted_message = self.convert_decimal_to_hexadecimal(encoded_message)
            return hexadecimal_encrypted_message
        
    def is_prime(self,prime_number) -> bool:
        '''
        Valiadtes if the given numbers are prime

        Validar si los números dados son primos

        Parameters
        ----------
        prime_number : int
            Number to be validated if it is prime /
            Número a validar si es primo

        Returns
        -------

        bool
            Returns True if the number is prime, otherwise returns False /
            Devuelve True si el número es primo, de lo contrario devuelve False
        '''
        if prime_number <= 1:
            return False
        if prime_number <= 3:
            return True
        if prime_number % 2 == 0 or prime_number % 3 == 0:
            return False
        i = 5
        while i * i <= prime_number:
            if prime_number % i == 0 or prime_number % (i + 2) == 0:
                return False
            i += 6
        return True
    
    def convert_decimal_to_hexadecimal(self, encrypted_message: list[int]) -> list[str]:
        '''
        Converts the encrypted message from decimal numbers to hexadecimal             

        Convierte el mensaje encriptado de números decimales a hexadecimal

        Parameters
        ----------

        encrypted_message : list[int]
            Encrypted message in decimal numbers /
            Mensaje encriptado en números decimales

        Returns
        -------

        hexadecimal_encrypted_message : list[str]
            Encrypted message in hexadecimal numbers /
            Mensaje encriptado en números hexadecimales
        '''

        hexadecimal_encrypted_message : list = []
        for letter in encrypted_message:
            hexadecimal_encrypted_message.append(hex(letter).replace('0x',''))

        return hexadecimal_encrypted_message

    def convert_hexadecimal_to_decima(self, encrypted_message: list[str]) -> list[int]:
        '''
        Converts the encrypted message from hexadecimal numbers to decimal

        Convierte el mensaje encriptado de números hexadecimales a decimales

        Parameters
        ----------

        encrypted_message : list[str]
            Encrypted message in hexadecimal numbers /
            Mensaje encriptado en números hexadecimales

        Returns
        -------

        decimal_encrypted_message : list[int]
            Encrypted message in decimal numbers /
            Mensaje encriptado en números decimales
        '''

        decimal_encrypted_message : list = []
        
        #Implementación aquí

        return decimal_encrypted_message

    
