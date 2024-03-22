import sys

sys.path.append('src')

import encriptation_algorithm.encriptation_algorithm as encriptation_algorithm


class ConsoleUI:

    def __init__(self) -> None:
        self.encriptation_engine = encriptation_algorithm.EncriptationEngine()

    def message_encrypter(self):

        message = input('Ingrese el mensaje a encriptar: ')

        encrypted_message = self.encriptation_engine.message_encoder(message)
    
        print(f'Mensaje encriptado: {encrypted_message}')

    def message_encrypter_with_inputs(self):

        message = input('Ingrese el mensaje a encriptar: ')

        prime_number1= int(input('Ingrese el primer número primo: '))
        prime_number2= int(input('Ingrese el segundo número primo: '))
        public_key = int(input('Ingrese la llave pública: '))

        encrypted_message = self.encriptation_engine.message_encoder_with_inputs(message,prime_number1,prime_number2,public_key)
    
        print(f'Mensaje encriptado: {encrypted_message}')


    def message_decrypter(self):
        
        encrypted_message : list = eval(input('Ingrese el mensaje a desencriptar: '))
        secret_key = (input('Ingrese la clave pública utilizada para encriptar el mensaje: '))
        if secret_key == '':
            raise encriptation_algorithm.EmptySecretKey('La clave pública no puede estar vacía')
        elif self.encriptation_engine.secret_key_format_validator(secret_key) == False:
            raise encriptation_algorithm.InvalidPublicKey('La clave pública debe ser una cadena de texto con el formato especificado')
        else:
            public_key, prime_number1, primer_number2 = secret_key.split(',')
            public_key = int(public_key.strip())
            prime_number1 = int(prime_number1.strip())
            prime_number2 = int(primer_number2.strip())
            decrypted_message = self.encriptation_engine.message_decoder(encrypted_message, public_key,prime_number1,prime_number2)
            print(f'Mensaje desencriptado: {decrypted_message}')




    def show_functionalities_menu(self):

        print('--------------------')
        print('Bienvenido al motor de encripción RSA.')
        print('Según lo que quieras hacer, escribe el número acorde a la opción deseada.')
        print('--------------------')
        print('1. Encriptar mensaje.')
        print('2. Desencriptar mensaje.')
        print('3. Salir')
        print('--------------------')


    def run_application(self):

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
                    self.encriptation_engine.prime_set_filler()
                    secret_key = self.encriptation_engine.public_and_private_key_generator()
                    self.message_encrypter()
                    print(f'La llave pública es: {secret_key}')
                elif option2 == 2:
                    print('----------------')
                    self.message_encrypter_with_inputs()
                else:
                    print('Opción inválida.')

            elif option1 == 2:
                print('Recuerda que el mensaje debe ser ingresado como una lista de números separados por comas.')
                print('Ejemplo: [123, 456, 789]')
                print('Recuerda que la clave pública debe ser ingresada como una cadena de tres números separados por comas.')
                print('Ejemplo: 123,456,789')
                print('--------------------')
                self.message_decrypter()
            elif option1 == 3:
                print('Saliendo del motor de encripción RSA.')
                print('¡Vuelve pronto!')
                break
            else:
                print('Opción inválida.')
            print('--------------------')


