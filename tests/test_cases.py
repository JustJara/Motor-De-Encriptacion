import unittest
import encriptation_algorithm as encriptation_algorithm

'''
This class contains the test cases for the encryption and decription of the messages
'''
class encryptionTests(unittest.TestCase):

    def test_encryption1(self):
        

        secret_key = "mi_clave_secreta"
        expected_encrypted_message = "5iuJeaccc+WN2Yq1GFlMp2APTxMGXSy89kAXYbfFhN0Oj9tkFLW+KxkUNalmJQIKNUsHZzJjVrb9HUO/FyVgPo2SxQXkIOZ8xgxHnOVzN2s"
        unencripted_message = "probando la encriptación de mi programa"

        encrypted_message = encriptation_algorithm.encrypt(secret_key,unencripted_message)

        self.assertEqual(expected_encrypted_message,encrypted_message)

    def test_encryption2(self):


        secret_key = "mi_clave_secreta"
        expected_encrypted_message = "4o1SGTAXo5lDwVNG4D2WwhiZ4ltKAF4/QehptwKHXJbWmb+J3TuY8ed5sTesD+CaXxH/vcgdxRMnU3J+MLlWUw"
        unencripted_message = "segundo caso de prueba"

        encrypted_message = encriptation_algorithm.encrypt(secret_key,unencripted_message)

        self.assertEqual(expected_encrypted_message,encrypted_message)

    def test_encryption3(self):

        secret_key = "mi_clave_secreta"
        expected_encrypted_message = "N5C01g6oe/D5GX8s+Ckna3kGppSGXMNFkmVwt9eAUFGnvkApH8FT5k+J6W/HD2rP/MqSz30bz5evGMobStZEyg"
        unencrypted_message = "tercer caso de prueba encriptado"

        encrypted_message = encriptation_algorithm.encrypt(secret_key,unencrypted_message)

        self.assertEqual(expected_encrypted_message,encrypted_message)

    def test_decryption1(self):

        secret_key = "mi_clave_secreta"
        original_message = "Hola, que tenga un buen dia"
        encrypted_message = "P8SHQjnqN/eLNJvV4yspRmzgr0eRgq2spyr4Cw2GIc7gTJxNERmu9uBjmJNFmW2dvGPycnlZpG5DeRtzwQgqxw"

        decrypted_message = encriptation_algorithm.decrypt(secret_key,encrypted_message)

        self.assertEqual(original_message,decrypted_message)

    def test_decryption2(self):

        secret_key = "mi_clave_secreta"
        original_message = "No pienses el pasado, se feliz"
        encrypted_message = "36mZNydKt8hwki6vlntItrtAE/wVv97QWpf92Na2Kj+btPlCo965yzHz4w8qi7UTjJkxqqofkOMnSsdxAx5VFw"

        decrypted_message = encriptation_algorithm.decrypt(secret_key,encrypted_message)

        self.assertEqual(original_message,decrypted_message)

    def test_decryption3(self):

        secret_key = "mi_clavesota_belica"
        original_message = "Piensa, luego existe"
        encrypted_message = "jRGI7mP54JIf0FO3iWm+dj7VnmqVgk35LEuS9uw0VbeBCNTskhgC8E6jvdHRNb0QQs8HAwL2fMsm2i+z1N494Q"

        decrypted_message = encriptation_algorithm.decrypt(secret_key,encrypted_message)

        self.assertEqual(original_message,decrypted_message)

    #Error Case #1
    def test_message_empty_to_encrypt(self):

        secret_key = "mi_clavesita_secreta"
        unencrypted_message = ""

        self.assertRaises(encriptation_algorithm.EmptyEncryptMessage,encriptation_algorithm.encrypt(secret_key,unencrypted_message))

    #Error Case #2
    def test_different_secretkey_to_encrypt(self):

        encrypted_message = "jRGI7mP54JIf0FO3iWm+dj7VnmqVgk35LEuS9uw0VbeBCNTskhgC8E6jvdHRNb0QQs8HAwL2fMsm2i+z1N494Q"

        secret_key = "secret_key"


        self.assertRaises(encriptation_algorithm.InvalidSecretKey,encriptation_algorithm.decrypt(secret_key,encrypted_message))
    
    #Error Case #3
    def test_decrypt_message_unencrypted(self):
    
        message_to_decrypt = "hola lola"
        secret_key = "hola_clave"

        self.assertRaises(encriptation_algorithm.MessageIsNotEncrypted, encriptation_algorithm.decrypt(secret_key,message_to_decrypt))
    
    #Error Case #4
    def test_empty_secret_key(self):
    
        message_to_decrypt = "jRGI7mP54JIf0FO3iWm+dj7VnmqVgk35LEuS9uw0VbeBCNTskhgC8E6jvdHRNb0QQs8HAwL2fMsm2i+z1N494Q"
        secret_key = ""

        self.assertRaises(encriptation_algorithm.EmptySecretKey,encriptation_algorithm.decrypt(secret_key,message_to_decrypt))

    #Error Case #5
    def test_encrypt_with_a_symbol_secretkey(self):

        unencrypted_message = "Este mensaje será encriptado"
        secret_key = "ñññ%%/;;"

        self.assertRaises(encriptation_algorithm.InvalidSecretKey,encriptation_algorithm.encrypt(secret_key,unencrypted_message))

    #Error Case #6
    def test_encryption_with_invalid_secretkey_length(self):

        unencrypted_message = "El mensaje no se podrá encriptar por la clave de longitud inválida"
        secret_key = "esta_clave_no_sera_valida_para_encriptar"

        self.assertRaises(encriptation_algorithm.InvalidSecretKey,encriptation_algorithm.encrypt(secret_key,unencrypted_message))

    #Error Case #7
    def test_empty_input_data(self):

        unencrypted_message = ""
        secret_key = ""

        self.assertRaises(encriptation_algorithm.EmptyInputValuesError,encriptation_algorithm.encrypt(unencrypted_message,secret_key))

    #Error Case #8
        
    def test_encryption_without_secretkey(self):

        unencrypted_message = "Cuando una fuerza actua sobre un objeto este se pone en movimiento"
        secret_key=""

        self.assertRaises(encriptation_algorithm.EmptySecretKey,encriptation_algorithm.encrypt(unencrypted_message,secret_key))
    

    #Exceptional Case #1
    def test_encryption_emoji(self):
    
        encrypted_message = "2dvCekIBLhSfQazHulGDQY58c1y95i5KzxrwXoVXAUaBy+B0WBIZ0DZFHTCv9SnHv1mf5ql8r8F20/NZXQpwR+c8rjl/PKFgUuC/y9kKhJ8"
        secret_key = "josue_don_juan"

        original_message = "🥰​🥰​🥰​🥰​🥰​👻"
        decrypted_message = encriptation_algorithm.decrypt(secret_key,encrypted_message)

        self.assertEqual(original_message,decrypted_message)

    #Exceptional Case #2
    def test_encrytion_with_invalid_symbols(self):
    
        unencrypted_message = "ʥʥʥʥʥʥʥʥ"
        secret_key = "pipe_jarra"

        expected_encrypted_message = "jDbi3COvkQdHQEnWHZpPFR+0UwjSh9ov7EpE/TyZ/KxMXrcO+WKfm5pHmYQJ5hMp"
        encrypted_message = encriptation_algorithm.encrypt(secret_key,unencrypted_message)

        self.assertEqual(expected_encrypted_message,encrypted_message)

    #Exceptional Case #3
    def test_number_encryption(self):
    
        message_to_decrypt = "SmClIKLgJhl0x1m/iovsvNFsjl00iof6LsBtb8qQaAJvdN5seAZ0N4M+MCcPQ6XI"
        secret_key = "boliche20*"

        original_message = "00000000000"
        decrypted_message = encriptation_algorithm.decrypt(secret_key,message_to_decrypt)

        self.assertEqual(original_message,decrypted_message)


    #Exceptional Case #4
    def test_encryption_with_symbols(self):

        unencrypted_message = "ÑonguiRombiAstrombißßß"
        secret_key = "astro_mango"

        expected_encrypted_message = "mnTRNBAzsl4pXWQLi5M2iBZsD2HiyR51CfEgmiwNOuBC4AW6g7P0/laQrZajBpDjbR4kdhnK7fu1AWAwPTfwzA"
        encrypted_message = encriptation_algorithm.encrypt(secret_key,unencrypted_message)

        self.assertEqual(expected_encrypted_message,encrypted_message)

    #Exceptional Case #5
    def test_encrypt_encrypted_message(self):

        unencrypted_message = 'UB9bS7pE1fkbqzjsrPrVSID8qynXGZS3g23ImLvKsIi87PEAJKi4et9n+SPWjg70'
        secret_key = 'mezclar_bien'

        expected_encrypted_message = 'gNLOIT1dUEm+2M1wAevcC9jf13Vb6/tm5ydXBwMGpxKwOP2HUYsGqTdhtGENsWX6RdZrmnee6DIhkI+ZlTriX91TFyme4QG80qXM5ixAtLUknUCQ7mQo1Z0TeHtPRQBn'
        encrypted_message = encriptation_algorithm.encrypt(secret_key, unencrypted_message)

        self.assertEqual(expected_encrypted_message, encrypted_message)

    #Exceptional Case #6
    def test_single_letter_message_encryption(self):

        unencrypted_message = 'a'
        secret_key = 'tomasinho'

        expected_encrypted_message = 'j2txUK57JvCfAncz20Bxe12z/5n5Yh43cA+iLQqBfigDcSCiYL5cYP1apx6gp+UL'
        encrypted_message = encriptation_algorithm.encrypt(secret_key, unencrypted_message)

        self.assertEqual(expected_encrypted_message, encrypted_message)

if __name__ == '__main__':
    unittest.main()