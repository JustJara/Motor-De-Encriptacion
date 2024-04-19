import sys
sys.path.append("src")

import encriptation_algorithm.encriptation_algorithm as encriptation_algorithm
from encriptation_algorithm.encriptation_algorithm import EncriptationEngine
from encriptation_algorithm.encriptation_algorithm import EmptyMessageError
from encriptation_algorithm.encriptation_algorithm import InvalidPublicKey
from encriptation_algorithm.encriptation_algorithm import EmptyPublicKey
from encriptation_algorithm.encriptation_algorithm import NonPrimeNumber
from encriptation_algorithm.encriptation_algorithm import EmptyInputValuesError

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup

class MainScreen(Screen):
    '''
    Class builds and manages the main screen of the application.

    Clase construye y gestiona la pantalla principal de la aplicación.
    '''

    def __init__(self, **kwargs):

        '''
        This method initializes the layout attribute of the class and adds the widgets to the layout.

        Este método inicializa el atributo layout de la clase y agrega los widgets al layout.
        '''

        super(MainScreen, self).__init__(**kwargs)

        self.layout = GridLayout(cols=1, padding=20, spacing=20)
        
        self.layout.add_widget(Label(text="Bienvenido al motor de encriptación", font_size=50))
        self.layout.add_widget(Label(text="¿Qué desea hacer hoy?", font_size=35))

        self.layout.add_widget(Button(text="Encriptar un mensaje", font_size=50, on_press=self.switch_to_encryption))
        self.layout.add_widget(Button(text="Desencriptar un mensaje", font_size=50, on_press=self.switch_to_decryption))
        self.layout.add_widget(Button(text="Salir", font_size=50, on_press=self.exit_app))
        self.add_widget(self.layout)

    def switch_to_encryption(self, instance):
        '''
        This method switches the screen to the encryption screen.

        Este método cambia la pantalla actual a la pantalla de encriptación.
        '''
        app.screen_manager.current = 'pre_encryption'

    def switch_to_decryption(self, instance):
        '''
        This method switches the screen to the decryption screen.

        Este método cambia la pantalla actual a la pantalla de desencriptación.
        '''
        app.screen_manager.current = 'decryption'

    def exit_app(self, instance):
        '''
        This method closes the application.

        Este método cierra la aplicación.
        '''
        App.get_running_app().stop()

class EncryptionScreenWithoutInputs(Screen):
    '''
    Class builds and manages the encryption screen of the application.

    Esta clase construye y gestiona la pantalla de encriptación de la aplicación.
    '''
    def __init__(self, **kwargs):
        '''
        This method initializes the layout attribute of the class and adds the widgets to the layout.

        Este método inicializa el atributo layout de la clase y agrega los widgets al layout.
        '''

        super(EncryptionScreenWithoutInputs, self).__init__(**kwargs)

        # Layout principal donde están todos los demás widgets y layouts adicionales
        self.main_layout = GridLayout(cols=1, padding=20, spacing=20)
        self.main_layout.add_widget(Label(text="Pantalla de Encriptación", font_size=50))

        # Grid layout para recibir el mensaje a encriptar con su respectivo TextInput y Label
        self.encryption_layout = GridLayout(rows= 2, spacing = 20)
        self.encryption_layout.add_widget(Label(text="Inserte el texto que desea encriptar", font_size=20))
        self.unencripted_message = TextInput(font_size=16, height=300,hint_text='Inserte el texto que desea encriptar')
        self.encryption_layout.add_widget(self.unencripted_message)

        # Grid Layout que contiene el label y el textinput donde se muestra el mensaje encriptado
        self.encrypted_message_layout = GridLayout(rows = 2, spacing = 20)
        self.encrypted_message_layout.add_widget(Label(text="El mensaje encriptado es: ", font_size=20))
        self.text_encrypted_message = TextInput(font_size=16, multiline=False,readonly=True ,height=300,hint_text='Aquí se mostrará el mensaje encriptado') 

        # Grid layout que contiene el label y textinput donde se muestra la clave secreta

        self.secret_key_layout = GridLayout(rows = 2, spacing = 20)
        self.secret_key_label = Label(text="La clave secreta es: ", font_size=20) 
        self.secret_key = TextInput(font_size=16, multiline=False,readonly=True ,height=300,hint_text='Aquí se mostrará la clave secreta')

        self.secret_key_layout.add_widget(self.secret_key_label)
        self.secret_key_layout.add_widget(self.secret_key)
        
        self.encrypted_message_layout.add_widget(self.text_encrypted_message)

        # Grid layout que contienee el botón para volver y ejecutar la lógica de encriptación
        self.buttons_layout  = BoxLayout( spacing = 20)

        self.back_button = Button(text="Volver", font_size=20, size_hint=(None, None), size=(100, 50))
        self.back_button.bind(on_press=self.switch_to_main) 

        self.encrypt_button = Button(text="Encriptar", font_size=20)  
        self.encrypt_button.bind(on_press=self.encrypt_message)

        self.clear_inputs_button = Button(text="Limpiar", font_size=20, size_hint=(None, None), size=(100, 50))
        self.clear_inputs_button.bind(on_press=self.clear_text_inputs)

        self.buttons_layout.add_widget(self.back_button)
        self.buttons_layout.add_widget(self.encrypt_button)
        self.buttons_layout.add_widget(self.clear_inputs_button)

        # Se agregan los layouts de los widgets al layout principal
        self.main_layout.add_widget(self.encryption_layout)
        self.main_layout.add_widget(self.encrypted_message_layout)
        self.main_layout.add_widget(self.secret_key_layout)
        self.main_layout.add_widget(self.buttons_layout)

        # Agregamos el layout principal al Screen de encriptación
        self.add_widget(self.main_layout)

    def switch_to_main(self, instance):
        app.screen_manager.current = 'main'

    def clear_text_inputs(self, instance):
        '''
        This method clears the text inputs of the screen.

        Este método limpia los text inputs de la pantalla.
        '''
        self.unencripted_message.text = ""
        self.text_encrypted_message.text = ""
        self.secret_key.text = ''

    def encrypt_message(self,message: str):

        '''
        This method calls the encryption algorithm to encode and encrypt the message.
        
        Este método llama al algoritmo de encriptación para codificar y encriptar el mensaje.
        '''
        try:
            # Validates if the inputs arent empty / Valida si los inputs no están vacíos
            self.validate_inputs()

            self.encriptation_engine = EncriptationEngine()
            self.encriptation_engine.fill_prime_set()
            secret_key = self.encriptation_engine.generate_public_and_private_key()
            message : str = str(self.unencripted_message.text)

            encrypted_message = self.encriptation_engine.encode_and_encrypt_message(message)
            
            self.text_encrypted_message.text = str(encrypted_message)
            self.secret_key.text = str(secret_key)

        except EmptyInputValuesError as error:
            self.show_popup_encryption_errors(error)
        except EmptyMessageError as error:
            self.show_popup_encryption_errors(error)
        except InvalidPublicKey as error:
            self.show_popup_encryption_errors(error)
        except EmptyPublicKey as error:
            self.show_popup_encryption_errors(error)
        except NonPrimeNumber as error:
            self.show_popup_encryption_errors(error)
        except TypeError as error:
            self.show_popup_encryption_errors(error)
        except ValueError as error:
            self.show_popup_encryption_errors(error)
        except Exception as error:
            self.show_popup_encryption_errors(error)

    def validate_inputs(self):
        '''
        This method validates the inputs of the user.

        Este método valida los inputs del usuario.
        '''
        if self.unencripted_message.text == "":
            raise EmptyInputValuesError

    def show_popup_encryption_errors(self, err):
        contenido = GridLayout(cols=1)
        error_label = Label(text=str(err))  # Establecer un alto fijo o usar size_hint_y=None para permitir que el Label defina su propio alto
        contenido.add_widget(error_label)

        boton_cerrar = Button(text='Cerrar')
        contenido.add_widget(boton_cerrar)

        error_popup = Popup(title='Error', content=contenido)  # Establecer un tamaño inicial
        boton_cerrar.bind(on_press=error_popup.dismiss)
        error_popup.open()
        
class PreEncryptionScreen(Screen):

    def __init__(self, **kw):
        super().__init__(**kw)

        self.layout = GridLayout(cols=1, padding=20, spacing=20)
        self.layout.add_widget(Label(text='Para encriptar puede utilizar \n dos funcionalidades de la aplicación.' ,halign='center',valign='middle',font_size=50))

        self.decition_buttons_layout = GridLayout(rows=3, padding=20, spacing=20)

        self.button_decition_1 = Button(text='Encriptar mensaje con llave pública generada por el motor y números primos \n seleccionados por el motor.',halign='center',valign='middle', font_size=20)
        self.button_decition_2 = Button(text='Encriptar mensaje con llave pública y números primos ingresados por el usuario.', font_size=20)
        self.back_button = Button(text="Volver", font_size=20, size_hint=(None, None), size=(100, 50))

        self.decition_buttons_layout.add_widget(self.button_decition_1)
        self.decition_buttons_layout.add_widget(self.button_decition_2)
        self.decition_buttons_layout.add_widget(self.back_button)

        self.back_button.bind(on_press=self.switch_to_main)
        self.button_decition_1.bind(on_press=self.switch_to_encryption_without_inputs)
        self.button_decition_2.bind(on_press=self.switch_to_encryption_with_inputs)

        self.layout.add_widget(self.decition_buttons_layout)

        self.add_widget(self.layout)

    def switch_to_main(self, instance):
        app.screen_manager.current = 'main'

    def switch_to_encryption_with_inputs(self, instance):
        app.screen_manager.current = 'encryption_with_inputs'

    def switch_to_encryption_without_inputs(self, instance):
        app.screen_manager.current = 'encryption'

class EncryptionScreenWithInputs(Screen):
    '''
    Class builds and manages the encryption screen of the application.

    Esta clase construye y gestiona la pantalla de encriptación de la aplicación.
    '''
    def __init__(self, **kwargs):
        '''
        This method initializes the layout attribute of the class and adds the widgets to the layout.

        Este método inicializa el atributo layout de la clase y agrega los widgets al layout.
        '''

        super(EncryptionScreenWithInputs, self).__init__(**kwargs)

        # Layout principal donde están todos los demás widgets y layouts adicionales
        self.main_layout = GridLayout(cols=1, padding=20, spacing=20)
        self.main_layout.add_widget(Label(text="Pantalla de Encriptación", font_size=50))

        # Grid layout para recibir el mensaje a encriptar con su respectivo TextInput y Label
        self.encryption_layout = GridLayout(rows= 2, spacing = 20)
        self.encryption_layout.add_widget(Label(text="Inserte el texto que desea encriptar", font_size=20))
        self.unencripted_message = TextInput(font_size=16, height=300,hint_text='Inserte el texto que desea encriptar')
        self.encryption_layout.add_widget(self.unencripted_message)

        #Grid layout para la llave pública con su respectivo label y textinput
        self.public_key_layout = GridLayout(rows = 2, spacing = 20)
        self.public_key_layout.add_widget(Label(text="Inserte la clave pública", font_size=20))
        self.public_key = TextInput(font_size=16, height=300, multiline=False,hint_text='Inserte la clave pública (Número entero)')  
        self.public_key_layout.add_widget(self.public_key)

        # Grid layout que contiene el label y otro grid layout con los textinput de los números primos
        self.primes_numbers_layout = GridLayout(rows = 2, spacing = 20)
        self.primes_numbers_layout.add_widget(Label(text="Inserte los números primos ", font_size=20))

        # Grid layout que contiene los textinput de los números primos
        self.primes_layout = GridLayout(cols = 2, spacing = 20)
        self.prime_number1 = TextInput(font_size=16, height=300,multiline= False,hint_text='Inserte el primer número primo')  
        self.prime_number2 = TextInput(font_size=16, height=300,multiline=False, hint_text='Inserte el segundo número primo')  
        self.primes_layout.add_widget(self.prime_number1)
        self.primes_layout.add_widget(self.prime_number2)
        self.primes_numbers_layout.add_widget(self.primes_layout)

        # Grid Layout que contiene el label y el textinput donde se muestra el mensaje encriptado
        self.encrypted_message_layout = GridLayout(rows = 2, spacing = 20)
        self.encrypted_message_layout.add_widget(Label(text="El mensaje encriptado es: ", font_size=20))
        self.text_encrypted_message = TextInput(font_size=16, multiline=False,readonly=True ,height=300,hint_text='Aquí se mostrará el mensaje encriptado') 
        
        self.encrypted_message_layout.add_widget(self.text_encrypted_message)

        # Grid layout que contienee el botón para volver y ejecutar la lógica de encriptación
        self.buttons_layout  = BoxLayout( spacing = 20)

        self.back_button = Button(text="Volver", font_size=20, size_hint=(None, None), size=(100, 50))
        self.back_button.bind(on_press=self.switch_to_main) 

        self.encrypt_button = Button(text="Encriptar", font_size=20)  
        self.encrypt_button.bind(on_press=self.encrypt_message)

        self.clear_inputs_button = Button(text="Limpiar", font_size=20, size_hint=(None, None), size=(100, 50))
        self.clear_inputs_button.bind(on_press=self.clear_text_inputs)

        self.buttons_layout.add_widget(self.back_button)
        self.buttons_layout.add_widget(self.encrypt_button)
        self.buttons_layout.add_widget(self.clear_inputs_button)

        # Se agregan los layouts de los widgets al layout principal
        self.main_layout.add_widget(self.encryption_layout)
        self.main_layout.add_widget(self.public_key_layout)
        self.main_layout.add_widget(self.primes_numbers_layout)
        self.main_layout.add_widget(self.encrypted_message_layout)
        self.main_layout.add_widget(self.buttons_layout)

        # Agregamos el layout principal al Screen de encriptación
        self.add_widget(self.main_layout)

    def switch_to_main(self, instance):
        app.screen_manager.current = 'main'

    def clear_text_inputs(self, instance):
        '''
        This method clears the text inputs of the screen.

        Este método limpia los text inputs de la pantalla.
        '''
        self.unencripted_message.text = ""
        self.public_key.text = ""
        self.prime_number1.text = ""
        self.prime_number2.text = ""
        self.text_encrypted_message.text = ""

    def encrypt_message(self, instance):
        '''
        This method calls the encryption algorithm to encode and encrypt the message.
        
        Este método llama al algoritmo de encriptación para codificar y encriptar el mensaje.
        '''

        try:
            # Validates if the inputs arent empty / Valida si los inputs no están vacíos
            self.validate_inputs()
            # Getting prime numbers / Obteniendo números primos
            prime_number1 : int = int(self.prime_number1.text)
            prime_number2 : int = int(self.prime_number2.text)

            message : str = str(self.unencripted_message.text)
            public_key : int = int(self.public_key.text) 

            encrypted_message = EncriptationEngine().encode_and_encrypt_message_with_inputs(message, prime_number1, prime_number2, public_key)
            
            self.text_encrypted_message.text = str(encrypted_message)

        except EmptyInputValuesError as error:
            self.show_popup_encryption_errors(error)
        except EmptyMessageError as error:
            self.show_popup_encryption_errors(error)
        except InvalidPublicKey as error:
            self.show_popup_encryption_errors(error)
        except EmptyPublicKey as error:
            self.show_popup_encryption_errors(error)
        except NonPrimeNumber as error:
            self.show_popup_encryption_errors(error)
        except TypeError as error:
            self.show_popup_encryption_errors(error)
        except ValueError as error:
            self.show_popup_encryption_errors(error)
        except Exception as error:
            self.show_popup_encryption_errors(error)
            
    def validate_inputs(self):
        '''
        This method validates the inputs of the user.

        Este método valida los inputs del usuario.
        '''
        
        unencripted_message : bool = self.unencripted_message.text == ""
        public_key : bool = self.public_key.text == ""
        prime_number1 : bool = self.prime_number1.text == ""
        prime_number2 : bool = self.prime_number2.text == ""

        empty_inputs : list[bool]= [unencripted_message, public_key, prime_number1, prime_number2]

        for input in empty_inputs:
            if input:
                raise EmptyInputValuesError
            
        if not self.public_key.text.isnumeric():
            raise InvalidPublicKey('La clave pública debe ser un número entero')
            
    def show_popup_encryption_errors(self, err):
        contenido = GridLayout(cols=1)
        error_label = Label(text=str(err))  # Establecer un alto fijo o usar size_hint_y=None para permitir que el Label defina su propio alto
        contenido.add_widget(error_label)

        boton_cerrar = Button(text='Cerrar')
        contenido.add_widget(boton_cerrar)

        error_popup = Popup(title='Error', content=contenido)  # Establecer un tamaño inicial
        boton_cerrar.bind(on_press=error_popup.dismiss)
        error_popup.open()

class DecryptationScreen(Screen):
    def __init__(self, **kwargs):
        super(DecryptationScreen, self).__init__(**kwargs)

        # Layout principal donde están todos los demás widgets y layouts adicionales
        self.main_layout = GridLayout(cols=1, padding=20, spacing=20)
        # Agregar texto de lo que hace la interfaz directamente en el layout principal
        self.main_layout.add_widget(Label(text="Pantalla de Desencriptación", font_size=50))


        # Grid Layout que contiene el label y el textinput donde se socilita el texto a desencriptar
        self.decrypt_grid_layout = GridLayout(rows=2, spacing=20)
        self.decrypt_grid_layout.add_widget(Label(text="Inserte el texto que desea desencriptar", font_size=30))
        self.encripted_message = TextInput(font_size=16, height=300,hint_text='Inserte el texto que desea desencriptar. Ej: [123, 456, 789]')
        self.decrypt_grid_layout.add_widget(self.encripted_message)

        #Grid layout para la llave pública
        self.public_key_grid_layout = GridLayout(rows = 2, spacing = 20)
        self.public_key_grid_layout.add_widget(Label(text="Inserte la clave secreta", font_size=30))
        self.secret_key = TextInput(font_size=16, height=300, multiline=False,hint_text='Inserte la clave secreta. Ej: [123, 456, 789]')
        self.public_key_grid_layout.add_widget(self.secret_key)

        # Grid Layout
        self.decrypted_message_grid_layout = GridLayout(rows=2, spacing=20)
        self.decrypted_message_grid_layout.add_widget(Label(text="El mensaje desencriptado es: ", font_size=30))
        self.decrypted_message = TextInput(font_size=16, height=300, readonly=True, hint_text='Aquí se mostrará el mensaje desencriptado')
        self.decrypted_message_grid_layout.add_widget(self.decrypted_message)

        # Grid layout que contiene los 3 botones para volver, desencriptar y limpiar los inputs
        self.buttons_layout  = BoxLayout( spacing = 20)

        self.back_button = Button(text="Volver", font_size=20, size_hint=(None, None), size=(100, 50))
        self.back_button.bind(on_press=self.switch_to_main) 

        self.dencrypt_button = Button(text="Desencriptar", font_size=20)
        self.dencrypt_button.bind(on_press=self.decrypt_message)

        self.clear_inputs_button = Button(text="Limpiar", font_size=20, size_hint=(None, None), size=(100, 50))
        self.clear_inputs_button.bind(on_press=self.clear_text_inputs)

        self.buttons_layout.add_widget(self.back_button)
        self.buttons_layout.add_widget(self.dencrypt_button)
        self.buttons_layout.add_widget(self.clear_inputs_button)

        #Se agrega cada layout al layout principal
        self.main_layout.add_widget(self.decrypt_grid_layout)
        self.main_layout.add_widget(self.public_key_grid_layout)
        self.main_layout.add_widget(self.decrypted_message_grid_layout)
        self.main_layout.add_widget(self.buttons_layout)

        self.add_widget(self.main_layout)

    def switch_to_main(self, instance):
        app.screen_manager.current = 'main'

    def clear_text_inputs(self, instance):
        '''
        This method clears the text inputs of the screen.

        Este método limpia los text inputs de la pantalla.
        '''
        self.encripted_message.text = ""
        self.secret_key.text = ""
        self.decrypted_message.text = ""

    def decrypt_message(self, instance):
        '''
        This method calls the decryption algorithm to decode and decrypt the message.
        
        Este método llama al algoritmo de desencriptación para decodificar y desencriptar el mensaje.
        '''
        try:
            # Validates if the inputs arent empty / Valida si los inputs no están vacíos
            self.validate_decrypt_inputs()
            # Getting prime numbers / Obteniendo números primos
            encrypted_message  = (self.encripted_message.text)
            secret_key : str = str(self.secret_key.text)


            if not encrypted_message.startswith('[') or not encrypted_message.endswith(']'):
                raise Exception('El mensaje debe ser ingresado como una lista de números separados por comas.')

            elif EncriptationEngine().secret_key_format_validator(secret_key) == False:
                raise InvalidPublicKey('La clave pública debe ser una cadena de texto con el formato especificado')
            else:
                '''
                Calls the decode_and_decrypt_message method of the EncriptationEngine class to decrypt the message /
                Llama al método decode_and_decrypt_message de la clase EncriptationEngine para desencriptar el mensaje

                '''
                encrypted_message = encrypted_message.strip('[]')

                # Dividir la cadena en elementos individuales
                elementos = encrypted_message.split(', ')

                # Convertir cada elemento en la lista a un entero
                list_encrypted_message = [int(elemento) for elemento in elementos]

                public_key, prime_number1, primer_number2 = secret_key.split(',')
                public_key = int(public_key.strip('[').strip(']').strip())
                prime_number1 = int(prime_number1.strip('[]').strip(']').strip())
                prime_number2 = int(primer_number2.strip('[]').strip(']').strip())

                decrypted_message = EncriptationEngine().decode_and_decrypt_message(list_encrypted_message, public_key,prime_number1,prime_number2)
                self.decrypted_message.text = str(decrypted_message)

            

        except EmptyInputValuesError as error:
            self.show_popup_decryption_errors(error)
        except EmptyMessageError as error:
            self.show_popup_decryption_errors(error)
        except InvalidPublicKey as error:
            self.show_popup_decryption_errors(error)
        except EmptyPublicKey as error:
            self.show_popup_decryption_errors(error)
        except NonPrimeNumber as error:
            self.show_popup_decryption_errors(error)
        except TypeError as error:
            self.show_popup_decryption_errors(error)
        except ValueError as error:
            self.show_popup_decryption_errors(error)
        except Exception as error:
            self.show_popup_decryption_errors(error)

    def validate_decrypt_inputs(self):

        '''
        This method validates the inputs of the user.

        Este método valida los inputs del usuario.
        '''
        
        encrypted_message : bool = self.encripted_message.text == ""
        public_key : bool = self.secret_key.text == ""

        empty_inputs : list[bool]= [encrypted_message, public_key]

        for input in empty_inputs:
            if input:
                raise EmptyInputValuesError
            
    def show_popup_decryption_errors(self, err):
        contenido = GridLayout(cols=1)
        error_label = Label(text=str(err))
        contenido.add_widget(error_label)

        boton_cerrar = Button(text='Cerrar')
        contenido.add_widget(boton_cerrar)

        error_popup = Popup(title='Error', content=contenido)
        boton_cerrar.bind(on_press=error_popup.dismiss)
        error_popup.open()

class EncryptationApp(App):
    def build(self):
        
        self.screen_manager = ScreenManager()
        self.main_screen = MainScreen(name='main')
        self.pre_encryption_screen = PreEncryptionScreen(name='pre_encryption')
        self.encryption_screen_without_inputs = EncryptionScreenWithoutInputs(name='encryption')
        self.encryption_screen_with_inputs = EncryptionScreenWithInputs(name='encryption_with_inputs')
        self.decryption_screen = DecryptationScreen(name='decryption')

        self.screen_manager.add_widget(self.main_screen)
        self.screen_manager.add_widget(self.pre_encryption_screen)
        self.screen_manager.add_widget(self.encryption_screen_without_inputs)
        self.screen_manager.add_widget(self.encryption_screen_with_inputs)
        self.screen_manager.add_widget(self.decryption_screen)

        return self.screen_manager




if __name__ == "__main__":
    app = EncryptationApp()
    app.run()
