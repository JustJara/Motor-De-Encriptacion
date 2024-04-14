'''

This file contains the ConsoleUI class, which is responsible for the user interface by console of the application.

Este archivo contiene la clase ConsoleUI, la cual es responsable de la interfaz de usuario por consola de la aplicación.

'''

import sys

sys.path.append('src')

import encriptation_algorithm.encriptation_algorithm as encriptation_algorithm
from encriptation_algorithm.encriptation_algorithm import EmptyEncryptMessage
from encriptation_algorithm.encriptation_algorithm import InvalidPublicKey
from encriptation_algorithm.encriptation_algorithm import EmptyPublicKey
from encriptation_algorithm.encriptation_algorithm import NonPrimeNumber
from encriptation_algorithm.encriptation_algorithm import EmptyInputValuesError



class ConsoleUI:
    '''

    Class for the user interface by console of the application.

    Clase para la interfaz de usuario por consola de la aplicación.

    '''

    def __init__(self):
        '''
        This method initializes the encriptation_engine attribute of the class.
        '''
        self.encriptation_engine= encriptation_algorithm.EncriptationEngine()

    def encrypt_message(self):
        '''
        This method calls the encode_and_encrypt_message method of the EncriptationEngine class to encrypt a message.

        Este método llama al método encode_and_encrypt_message de la clase EncriptationEngine para encriptar un mensaje.

        '''

        # Ask the user for the message to encrypt / Pide al usuario el mensaje a encriptar
        message = input('Ingrese el mensaje a encriptar: ')
        
        '''
        Calls the encode_and_encrypt_message method of the EncriptationEngine class to encrypt the message /
        Llama al método encode_and_encrypt_message de la clase EncriptationEngine para encriptar el mensaje
        '''
        encrypted_message = self.encriptation_engine.encode_and_encrypt_message(message)
    
        print(f'Mensaje encriptado: {encrypted_message}')

    def encode_and_encrypt_message(self):

        '''
        This method calls the encode_and_encrypt_message_with_inputs method of the EncriptationEngine class to encrypt a message with the inputs of the user.

        Este método llama al método encode_and_encrypt_message_with_inputs de la clase EncriptationEngine para encriptar un mensaje con los datos ingresados por el usuario.

        '''
        try:
            # Ask the user for the message to encrypt / Pide al usuario el mensaje a encriptar
            message = input('Ingrese el mensaje a encriptar: ')

            # Ask the user for the prime numbers and the public key / Pide al usuario los números primos y la llave pública
            prime_number1= int(input('Ingrese el primer número primo: '))
            prime_number2= int(input('Ingrese el segundo número primo: '))
            public_key = int(input('Ingrese la llave pública: '))

            '''
            Calls the encode_and_encrypt_message_with_inputs method of the EncriptationEngine class to encrypt the message /
            Llama al método encode_and_encrypt_message_with_inputs de la clase EncriptationEngine para encriptar el mensaje 
            '''

            encrypted_message = self.encriptation_engine.encode_and_encryp_message_with_inputs(message,prime_number1,prime_number2,public_key)

            print(f'Mensaje encriptado: {encrypted_message}')

        except EmptyEncryptMessage as error:
            print(error)
        except EmptyInputValuesError as error:
            print(error.message)
        except EmptyPublicKey as error:
            print(error.message)
        except NonPrimeNumber as error:
            print(error.message)
        except Exception as error:
            print(error)

    def decrypt_message(self):
        '''
        This method calls the decode_and_decrypt_message method of the EncriptationEngine class to decrypt a message.

        Este método llama al método decode_and_decrypt_message de la clase EncriptationEngine para desencriptar un mensaje.

        Raises
        ------

        InvalidPublicKey
            If the public key does not have the correct format.
            Si la clave pública no tiene el formato correcto.
        '''
        
        '''
        Asks the user for the encrypted message and the public key used to encrypt the message /
        Pide al usuario el mensaje encriptado y la clave pública utilizada para encriptar el mensaje
        '''
        try:
            encrypted_message : list = eval(input('Ingrese el mensaje a desencriptar: '))
            secret_key = (input('Ingrese la clave pública utilizada para encriptar el mensaje: '))

            if self.encriptation_engine.secret_key_format_validator(secret_key) == False:
                raise encriptation_algorithm.InvalidPublicKey('La clave pública debe ser una cadena de texto con el formato especificado')
            else:
                '''
                Calls the decode_and_decrypt_message method of the EncriptationEngine class to decrypt the message /
                Llama al método decode_and_decrypt_message de la clase EncriptationEngine para desencriptar el mensaje
                '''
                public_key, prime_number1, primer_number2 = secret_key.split(',')
                public_key = int(public_key.strip())
                prime_number1 = int(prime_number1.strip())
                prime_number2 = int(primer_number2.strip())
                decrypted_message = self.encriptation_engine.decode_and_decrypt_message(encrypted_message, public_key,prime_number1,prime_number2)
                print(f'Mensaje desencriptado: {decrypted_message}')
        except EmptyPublicKey as error:
            print(error.message)
        except SyntaxError as error:
            print('El mensaje debe ser ingresado como una lista de números separados por comas.')
        except EmptyInputValuesError as error:
            print(error.message)

    def show_functionalities_menu(self):
        '''
        This method shows the functionalities menu of the application.

        Este método muestra el menú de funcionalidades de la aplicación.
        '''

        print('--------------------')
        print('Bienvenido al motor de encripción RSA.')
        print('Según lo que quieras hacer, escribe el número acorde a la opción deseada.')
        print('--------------------')
        print('1. Encriptar mensaje.')
        print('2. Desencriptar mensaje.')
        print('3. Salir')
        print('--------------------')

    def run_application(self):

        '''
        This method runs the application.

        Este método ejecuta la aplicación.
        '''
        encendido = True
        while encendido == True:    
            while True:
                

                self.show_functionalities_menu()

                option1 = int(input('Opción: '))

                if option1 == 1:
                    print('----------------')
                    print('Para encriptar puede utilizar dos funcionalidades de la aplicación:')
                    print('1. Encriptar mensaje con llave pública generada por el motor.')
                    print('2. Encriptar mensaje con llave pública y números primos ingresados por el usuario.')
                    option2 = int(input('Opción: '))
                    if option2 == 1:
                        print('----------------')
                        self.encriptation_engine.fill_prime_set()
                        secret_key = self.encriptation_engine.generate_public_and_private_key()
                        self.encrypt_message()
                        print(f'La llave pública es: {secret_key}')
                    elif option2 == 2:
                        print('----------------')
                        self.encode_and_encrypt_message()
                    else:
                        print('Opción inválida.')

                elif option1 == 2:
                    print('Recuerda que el mensaje debe ser ingresado como una lista de números separados por comas.')
                    print('Ejemplo: [123, 456, 789]')
                    print('Recuerda que la clave pública debe ser ingresada como una cadena de tres números separados por comas.')
                    print('Ejemplo: 123,456,789')
                    print('--------------------')
                    self.decrypt_message()
                elif option1 == 3:
                    print('Saliendo del motor de encripción RSA.')
                    print('¡Vuelve pronto!')
                    encendido = False
                    break
                else:
                    print('Opción inválida.')
                print('--------------------')


