import unittest
import motor_encripcion
class EncriptionTests(unittest.TestCase):

    def test_encriptacion1(self):
        

        clave_secreta = "mi_clave_secreta"
        mensaje_encriptado_esperado = "5iuJeaccc+WN2Yq1GFlMp2APTxMGXSy89kAXYbfFhN0Oj9tkFLW+KxkUNalmJQIKNUsHZzJjVrb9HUO/FyVgPo2SxQXkIOZ8xgxHnOVzN2s"
        mensaje_a_encriptar = "probando la encriptación de mi programa"

        mensaje_encriptado = motor_encripcion.encriptar(clave_secreta,mensaje_a_encriptar)

        self.asserEqual(mensaje_encriptado_esperado,mensaje_encriptado)

    def test_encriptacion2(self):


        clave_secreta = "mi_clave_secreta"
        mensaje_encriptado_esperado = "4o1SGTAXo5lDwVNG4D2WwhiZ4ltKAF4/QehptwKHXJbWmb+J3TuY8ed5sTesD+CaXxH/vcgdxRMnU3J+MLlWUw"
        mensaje_a_encriptar = "segundo caso de prueba"

        mensaje_encriptado = motor_encripcion.encriptar(clave_secreta,mensaje_a_encriptar)

        self.asserEqual(mensaje_encriptado_esperado,mensaje_encriptado)

    def test_encriptacion3(self):

        clave_secreta = "mi_clave_secreta"
        mensaje_encriptado_esperado = "N5C01g6oe/D5GX8s+Ckna3kGppSGXMNFkmVwt9eAUFGnvkApH8FT5k+J6W/HD2rP/MqSz30bz5evGMobStZEyg"
        mensaje_a_encriptar = "tercer caso de prueba encriptado"

        mensaje_encriptado = motor_encripcion.encriptar(clave_secreta,mensaje_a_encriptar)

        self.asserEqual(mensaje_encriptado_esperado,mensaje_encriptado)

    def test_desencriptacion1(self):

        clave_secreta = "mi_clave_secreta"
        mensaje_original = "Hola, que tenga un buen dia"
        mensaje_encriptado = "P8SHQjnqN/eLNJvV4yspRmzgr0eRgq2spyr4Cw2GIc7gTJxNERmu9uBjmJNFmW2dvGPycnlZpG5DeRtzwQgqxw"

        mensaje_desencriptado = motor_encripcion.desencriptar(clave_secreta,mensaje_encriptado)

        self.assertEqual(mensaje_original,mensaje_desencriptado)

    def test_desencriptacion2(self):

        clave_secreta = "mi_clave_secreta"
        mensaje_original = "No pienses el pasado, se feliz"
        mensaje_encriptado = "36mZNydKt8hwki6vlntItrtAE/wVv97QWpf92Na2Kj+btPlCo965yzHz4w8qi7UTjJkxqqofkOMnSsdxAx5VFw"

        mensaje_desencriptado = motor_encripcion.desencriptar(clave_secreta,mensaje_encriptado)

        self.assertEqual(mensaje_original,mensaje_desencriptado)

    def test_desencriptacion3(self):

        clave_secreta = "mi_clave_secreta"
        mensaje_original = "Piensa, luego existe"
        mensaje_encriptado = "jRGI7mP54JIf0FO3iWm+dj7VnmqVgk35LEuS9uw0VbeBCNTskhgC8E6jvdHRNb0QQs8HAwL2fMsm2i+z1N494Q"

        mensaje_desencriptado = motor_encripcion.desencriptar(clave_secreta,mensaje_encriptado)

        self.assertEqual(mensaje_original,mensaje_desencriptado)

    #Caso de error #1
    def test_mensaje_a_encriptar_vacio(self):

        clave_secreta = "mi_clave_secreta"
        mensaje_a_encriptar = ""

        self.assertRaises(motor_encripcion.EmptyEncryptMessage,motor_encripcion.encriptar(clave_secreta,mensaje_a_encriptar))

    #Caso de error #2
    def test_clave_distinta_de_encriptacion(self):

        mensaje_encriptado = "jRGI7mP54JIf0FO3iWm+dj7VnmqVgk35LEuS9uw0VbeBCNTskhgC8E6jvdHRNb0QQs8HAwL2fMsm2i+z1N494Q"

        clave_secreta = "clave_secreta"


        self.assertRaises(motor_encripcion.InvalidSecretKey,motor_encripcion.desencriptar(clave_secreta,mensaje_encriptado))
    
    #Caso error #3
    def test_desencriptar_mensaje_sin_encriptar(self):
    
        mensaje_a_desencriptar = "hola lola"
        clave_secreta = "mi_clave_secreta"

        self.assertRaises(motor_encripcion.MessageIsNotEncrypted, motor_encripcion.desencriptar(clave_secreta,mensaje_a_desencriptar))
    
    #Caso error #4
    def test_desencriptar_sin_clave(self):
    
        mensaje_a_desencriptar = "jRGI7mP54JIf0FO3iWm+dj7VnmqVgk35LEuS9uw0VbeBCNTskhgC8E6jvdHRNb0QQs8HAwL2fMsm2i+z1N494Q"
        clave_secreta = ""

        self.assertRaises(motor_encripcion.EmptySecretKey,motor_encripcion.desencriptar(clave_secreta,mensaje_a_desencriptar))

    #Caso error #5
    def test_encriptar_con_clave_con_simbolos(self):

        mensaje_a_encriptar = "Este mensaje será encriptado"
        clave_secreta = "ñññ%%/;;"

        self.assertRaises(motor_encripcion.InvalidSecretKey,motor_encripcion.encriptar(clave_secreta,mensaje_a_encriptar))

    #Caso error #6
    def test_encriptacion_con_clave_de_longitud_invalida(self):

        mensaje_a_encriptar = "El mensaje no se podrá encriptar por la clave de longitud inválida"
        clave_secreta = "esta_clave_no_sera_valida_para_encriptar"

        self.assertRaises(motor_encripcion.InvalidSecretKey,motor_encripcion.encriptar(clave_secreta,mensaje_a_encriptar))

    

    #Caso excepcional #1
    def test_encriptacion_emoji(self):
    
        mensaje_encriptado = "2dvCekIBLhSfQazHulGDQY58c1y95i5KzxrwXoVXAUaBy+B0WBIZ0DZFHTCv9SnHv1mf5ql8r8F20/NZXQpwR+c8rjl/PKFgUuC/y9kKhJ8"
        clave_secreta = "mi_clave_secreta"

        mensaje_original = "🥰​🥰​🥰​🥰​🥰​👻"
        mensaje_desencriptado = motor_encripcion.desencriptar(clave_secreta,mensaje_encriptado)

        self.assertEqual(mensaje_original,mensaje_desencriptado)

    #Caso excepcional #2
    def test_encriptacion_simbolos_invalidos(self):
    
        mensaje_a_encriptar = "ʥʥʥʥʥʥʥʥ"
        clave_secreta = "mi_clave_secreta"

        mensaje_encriptado_esperado = "jDbi3COvkQdHQEnWHZpPFR+0UwjSh9ov7EpE/TyZ/KxMXrcO+WKfm5pHmYQJ5hMp"
        mensaje_encriptado = motor_encripcion.encriptar(clave_secreta,mensaje_a_encriptar)

        self.assertEqual(mensaje_encriptado_esperado,mensaje_encriptado)

    #Caso excepcional #3
    def test_encriptacion_numeros(self):
    
        mensaje_a_desencriptar = "SmClIKLgJhl0x1m/iovsvNFsjl00iof6LsBtb8qQaAJvdN5seAZ0N4M+MCcPQ6XI"
        clave_secreta = "mi_clave_secreta"

        mensaje_original = "00000000000"
        mensaje_desencriptado = motor_encripcion.desencriptar(clave_secreta,mensaje_a_desencriptar)

        self.assertEqual(mensaje_original,mensaje_desencriptado)


    #Caso excepcional #4
    def test_encriptacion_con_simbolos(self):

        mensaje_a_encriptar = "ÑonguiRombiAstrombißßß"
        clave_encriptacion = "mi_clave_secreta"

        mensaje_encriptado_esperado = "mnTRNBAzsl4pXWQLi5M2iBZsD2HiyR51CfEgmiwNOuBC4AW6g7P0/laQrZajBpDjbR4kdhnK7fu1AWAwPTfwzA"
        mensaje_encriptado = motor_encripcion.encriptar(clave_encriptacion,mensaje_a_encriptar)

        self.assertEqual(mensaje_encriptado_esperado,mensaje_encriptado)

    #Caso excepcional #5
    def test_encriptar_mensaje_encriptado(self):

        mensaje_a_encriptar = 'UB9bS7pE1fkbqzjsrPrVSID8qynXGZS3g23ImLvKsIi87PEAJKi4et9n+SPWjg70'
        clave_encriptacion = 'mi_clave_secreta'

        mensaje_encriptado_esperado = 'gNLOIT1dUEm+2M1wAevcC9jf13Vb6/tm5ydXBwMGpxKwOP2HUYsGqTdhtGENsWX6RdZrmnee6DIhkI+ZlTriX91TFyme4QG80qXM5ixAtLUknUCQ7mQo1Z0TeHtPRQBn'
        mensaje_encriptado = motor_encripcion.encriptar(clave_encriptacion, mensaje_a_encriptar)

        self.assertEqual(mensaje_encriptado_esperado, mensaje_encriptado)



if __name__ == '__main__':
    unittest.main()