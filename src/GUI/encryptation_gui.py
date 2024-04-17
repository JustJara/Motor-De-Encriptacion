import sys
sys.path.append("src")

import encriptation_algorithm.encriptation_algorithm as encriptation_algorithm

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.layout = GridLayout(cols=1, padding=20, spacing=20)
        self.layout.add_widget(Label(text="Bienvenido al motor de encriptación", font_size=50))
        self.layout.add_widget(Label(text="¿Qué desea hacer hoy?", font_size=35))
        self.layout.add_widget(Button(text="Encriptar un mensaje", font_size=50, on_press=self.switch_to_encryption))
        self.layout.add_widget(Button(text="Desencriptar un mensaje", font_size=50, on_press=self.switch_to_decryption))
        self.layout.add_widget(Button(text="Salir", font_size=50, on_press=self.exit_app))
        self.add_widget(self.layout)

    def switch_to_encryption(self, instance):
        app.screen_manager.current = 'encryption'

    def switch_to_decryption(self, instance):
        app.screen_manager.current = 'decryption'

    def exit_app(self, instance):
        App.get_running_app().stop()


class EncryptionScreen(Screen):
    def __init__(self, **kwargs):
        super(EncryptionScreen, self).__init__(**kwargs)

        # Layout principal
        self.layout = GridLayout(cols=1, padding=20, spacing=20)

        # Agregar texto de lo que hace la interfaz directamente en el layout principal
        self.layout.add_widget(Label(text="Pantalla de Encriptación", font_size=50))

        # Grid layout para el texto a encriptar
        self.text_encryption = GridLayout(cols = 2, spacing = 20)

        #Grid layout para la llave pública
        self.set_public_key = GridLayout(cols = 2, spacing = 20)

        # Grid Layout para los números primos
        self.primes = GridLayout(cols = 3, spacing = 20)

        # Grid Layout para el mensaje encriptado
        self.encrypted_message = GridLayout(cols = 2, spacing = 20)

        # Lógica del texto a encriptar
        self.text_encryption.add_widget(Label(text="Inserte el texto que desea encriptar", font_size=30))
        self.unencripted_message = TextInput(font_size=40, size_hint_x=None, width=250)  # Reducir el ancho del TextInput
        self.text_encryption.add_widget(self.unencripted_message)

        # Agregamos el GridLayout de la lógica del texto a encriptar al layout principal
        self.layout.add_widget(self.text_encryption)

        #Lógica de la clave publica
        self.set_public_key.add_widget(Label(text="Inserte la clave pública", font_size=30))
        self.public_key = TextInput(font_size=40, size_hint_x=None, width=250)  # Reducir el ancho del TextInput
        self.set_public_key.add_widget(self.public_key)

        #Agregamos el GridLayout de la lógica de la clave pública al layout principal
        self.layout.add_widget(self.set_public_key)

        # Lógica de los números primos
        self.primes.add_widget(Label(text="Inserte los números primos ", font_size=30))
        self.prime_number1 = TextInput(font_size=70, size_hint_x=None, width=200)  # Reducir el ancho del TextInput
        self.prime_number2 = TextInput(font_size=70, size_hint_x=None, width=200)  # Reducir el ancho del TextInput
        self.primes.add_widget(self.prime_number1)
        self.primes.add_widget(self.prime_number2)

        # Agregamos el GridLayout de la lógica de los números primos al layout principal
        self.layout.add_widget(self.primes)

        # Lógica del mensaje encriptado
        self.encrypted_message.add_widget(Label(text="El mensaje encriptado es: ", font_size=30))

        # Agregamos el GridLayout de la lógica del mensaje encriptado al layout principal
        self.layout.add_widget(self.encrypted_message)

        # Lógica del botón para regresar al menú principal
        self.back_button = Button(text="Volver", font_size=20, size_hint=(None, None), size=(100, 50), pos_hint={'x': 0, 'y': 0})  # Posicionar en la esquina inferior izquierda
        self.back_button.bind(on_press=self.switch_to_main)  # Conectar el botón con la función de cambio de pantalla
        self.layout.add_widget(self.back_button)

        # Agregamos el layout principal al Screen de encriptación
        self.add_widget(self.layout)

    def switch_to_main(self, instance):
        app.screen_manager.current = 'main'


class DecryptationScreen(Screen):
    def __init__(self, **kwargs):
        super(DecryptationScreen, self).__init__(**kwargs)

        # Layout principal
        self.layout = GridLayout(cols=1, padding=20, spacing=20)

        # Agregar texto de lo que hace la interfaz directamente en el layout principal
        self.layout.add_widget(Label(text="Pantalla de Desencriptación", font_size=50))

        # Grid layout para el texto a desencriptar
        self.text_decryption = GridLayout(cols=2, spacing=20)

        #Grid layout para la llave pública
        self.set_public_key = GridLayout(cols = 2, spacing = 20)

        # Grid Layout para los números primos
        self.primes = GridLayout(cols=3, spacing=20)

        # Grid Layout para el mensaje desencriptado
        self.decrypted_message = GridLayout(cols=2, spacing=20)

        #Lógica de la clave publica
        self.set_public_key.add_widget(Label(text="Inserte la clave pública", font_size=30))
        self.public_key = TextInput(font_size=40, size_hint_x=None, width=250)  # Reducir el ancho del TextInput
        self.set_public_key.add_widget(self.public_key)

        #Agregamos el GridLayout de la lógica de la clave pública al layout principal
        self.layout.add_widget(self.set_public_key)

        # Lógica del texto a desencriptar
        self.text_decryption.add_widget(Label(text="Inserte el texto que desea desencriptar", font_size=30))
        self.encripted_message = TextInput(font_size=40, size_hint_x=None, width=250)  # Reducir el ancho del TextInput
        self.text_decryption.add_widget(self.encripted_message)

        # Agregamos el GridLayout de la lógica del texto a encriptar al layout principal
        self.layout.add_widget(self.text_decryption)

        # Lógica de los números primos
        self.primes.add_widget(Label(text="Inserte los números primos ", font_size=30))
        self.prime_number1 = TextInput(font_size=70, size_hint_x=None, width=200)  # Reducir el ancho del TextInput
        self.prime_number2 = TextInput(font_size=70, size_hint_x=None, width=200)  # Reducir el ancho del TextInput
        self.primes.add_widget(self.prime_number1)
        self.primes.add_widget(self.prime_number2)

        # Agregamos el GridLayout de la lógica de los números primos al layout principal
        self.layout.add_widget(self.primes)

        # Lógica del mensaje encriptado
        self.decrypted_message.add_widget(Label(text="El mensaje desencriptado es: ", font_size=30))

        # Agregamos el GridLayout de la lógica del mensaje encriptado al layout principal
        self.layout.add_widget(self.decrypted_message)

        # Lógica del botón para regresar al menú principal
        self.back_button = Button(text="Volver", font_size=20, size_hint=(None, None), size=(100, 50), pos_hint={'x': 0, 'y': 0})  # Posicionar en la esquina inferior izquierda
        self.back_button.bind(on_press=self.switch_to_main)  # Conectar el botón con la función de cambio de pantalla
        self.layout.add_widget(self.back_button)

        # Agregamos el layout principal al Screen de encriptación
        self.add_widget(self.layout)

    def switch_to_main(self, instance):
        app.screen_manager.current = 'main'


class EncryptationApp(App):
    def build(self):
        self.screen_manager = ScreenManager()
        self.main_screen = MainScreen(name='main')
        self.encryption_screen = EncryptionScreen(name='encryption')
        self.decryption_screen = DecryptationScreen(name='decryption')

        self.screen_manager.add_widget(self.main_screen)
        self.screen_manager.add_widget(self.encryption_screen)
        self.screen_manager.add_widget(self.decryption_screen)

        return self.screen_manager


if __name__ == "__main__":
    app = EncryptationApp()
    app.run()
