import sys
import random
import math
import re

sys.path.append('src')


# Definimos la clase para capturar la excepcion de un mensaje vacio
class EmptyEncryptMessage(Exception):
    def __init__(self):
        super().__init__('El mensaje ingresado no puede estar vacío')

# Definimos la clase para capturar la excepcion de una clave secreta invalida
class InvalidPublicKey(Exception):
    def __init__(self):
        super().__init__('La clave solo puede contener valores númericos separados por coma')

# Definimos la clase para capturar la excepcion de un mensaje no encriptado
class InvalidPublicKey(Exception):
    def __init__(self):
        super().__init__('La clave solo puede contener valores númericos separados por coma')

# Definimos la clase para capturar la excepcion de una clave secreta vacia
class EmptyPublicKey(Exception):
    def __init__(self):
        super().__init__('La clave no puede estar vacía')

class NonPrimeNumber(Exception):
    def __init__(self):
        super().__init__('Los números ingresados no son primos')

# Definimos la clase para capturar la excepcion de un mensaje vacio
class EmptyInputValuesError(Exception):
    def __init__(self):
        super().__init__('No puedes dejar espacios vacíos')

# Definimos el metodo para encriptar un mensaje

class EncriptationEngine:

    def __init__(self):

        #Conjunto de números primos donde se seleccionarán de forma aleatoria los números primos p y q
        self.prime_set : set = set()

        #Número aleatorio entre 1 y  phi ((prime1 - 1) * (prime2 - 1))
        self.public_key : int = None

        #Inverso de la public_key en modulo phi ((prime1 - 1) * (prime2 - 1))
        self.private_key : int = None

        #Producto entre dos números primos diferentes
        self.RSA_module: int = None

        self.phi : int = None

    # Método utilizado para llenar el conjunto de números primos: es la Criba de Eratóstenes (un método para recopilar números primos)
    def prime_set_filler(self):

        filtered_primes : list = [True] * 250

        filtered_primes[0] = False
        filtered_primes[1] = False

        #Asignar el valor False a los múltiplos de los números primos
        for i in range(2, 250):
            for j in range(i * 2, 250, i):
                filtered_primes[j] = False

        # Llenando el cojunto 'prime_set' con números primos
        for i in range(len(filtered_primes)):
            if filtered_primes[i]:
                self.prime_set.add(i)

    # Escoge un número primo aleatorio y elimina ese número primo del conjunto porque prime_number1!=prime_number2
    def random_prime_picker(self) -> int:
        random_number : int = random.randint(0, len(self.prime_set) - 1)
        iterable_set : set = iter(self.prime_set)

        for _ in range(random_number):
            next(iterable_set)

        # Seleccionar un número primo aleatorio y lo elimina del conjunto
        random_prime_number : int = next(iterable_set)
        self.prime_set.remove(random_prime_number)

        return random_prime_number

    # Genera las claves pública y privada
    def public_and_private_key_generator(self) -> tuple[int] :
        prime_number1 : int = self.random_prime_picker()
        prime_number2 : int = self.random_prime_picker()

        self.RSA_module = prime_number1 * prime_number2

        # El valor de la función multiplicativa de Euler φ(n) apartir de n 
        self.phi : int = (prime_number1 - 1) * (prime_number2 - 1)

        public_key : int = 2
        while True:
            if math.gcd(public_key, self.phi) == 1:
                break
            public_key += 1

        self.public_key = public_key

        #Asigna el valor del inverso de la llave pública en modulo phi
        private_key : int = self.private_key_generator(public_key, self.RSA_module)
        self.private_key = private_key

        return [self.public_key, prime_number1,prime_number2]
    
        
    def private_key_generator(self,public_key:int, phi: int) -> int:

        #Halla el inverso de la llave pública en modulo phi
        self.public_key = public_key
        self.phi = phi
        private_key = 2
        while True:
            if (private_key * public_key) % phi == 1:
                break
            private_key += 1
        return private_key
    
    #Encripta el mensaje indicado por el usuario
    def message_encrypter(self, unencrypted_message:int) -> int:

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

    def message_decrypter(self, encrypted_letter : int,private_key,RSA_module) -> int:

            temporal_private_key : int = private_key
            decrypted_letter : int = 1
    
            #Ciclo para desencriptar el mensaje
            while temporal_private_key > 0:
                decrypted_letter *= encrypted_letter
                decrypted_letter %= RSA_module
                temporal_private_key -= 1
    
            return decrypted_letter
    
    #Se itera sobre cada letra del mensaje se codifica con ASCII y se encripta cada letra con el método message_encrypter
    def message_encoder(self,message: str) -> list[int]:
        
        #Valida si el mensaje no está vacío y lanza una excepción si lo está
        if message == '':
            raise EmptyEncryptMessage
        else:
            encoded_message : list = []
            for letter in message:
                encoded_message.append(self.message_encrypter(ord(letter)))

            return encoded_message
    
    '''Se itera sobre cada letra del mensaje codificado y se decodifica con ASCII para convertirlo a cadena de texto
    y después se desencripta con el método message_decrypter'''
    def message_decoder(self,encoded_message, public_key,prime_number1,prime_number2) -> str:

        if prime_number1 == None or prime_number2 == None:
            raise EmptyInputValuesError
        if encoded_message == '':
            raise SyntaxError('El mensaje no puede estar vacío')

        if public_key == None:
            raise EmptyPublicKey
        else:
            
            
            decoded_message : str = ''
            private_key = self.private_key_generator(public_key, (prime_number1 - 1) * (prime_number2 - 1))
            RSA_module = prime_number1 * prime_number2
            for letter in encoded_message:
                decoded_message += chr(self.message_decrypter(letter,private_key,RSA_module))

            return decoded_message
    

    def secret_key_format_validator(self,cadena) -> bool:
        # Definimos el patrón de la expresión regular
        patron = r'^\d+,\d+,\d+.*$'    

        # Comprobamos si la cadena coincide con el patrón
        if re.match(patron, cadena):
            return True
        else:
            raise InvalidPublicKey

    def message_encrypter_with_inputs(self, unencrypted_letter:int, public_key, RSA_module) -> int:

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

    def message_encoder_with_inputs(self,message: str, prime_number1, prime_number2,public_key) -> list[int]:
        
        #Valida si el mensaje no está vacío y lanza una excepción si lo está
        if message == '':
            raise EmptyEncryptMessage
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
                encoded_message.append(self.message_encrypter_with_inputs(ord(letter),public_key,RSA_module))

            return encoded_message
        
    def is_prime(self,prime_number):
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
    
    
