import unittest
import sys

sys.path.append('src')

from encriptation_algorithm.encriptation_algorithm import *

'''
This class contains the test cases for the encryption and decription of the messages
'''
class encryptionTests(unittest.TestCase):

    def test_encryption1(self):
        

        public_key : int= 5
        prime_number1 :int= 29
        prime_number2 :int= 127
        expected_encrypted_message = [17, 2212, 225, 2302, 1219, 257, 2302, 2478, 744, 55, 418, 744, 257, 2212, 55, 1552, 2095]
        unencripted_message = 'hay un mercenario'

        encrypted_message = EncriptationEngine().encode_and_encrypt_message_with_inputs(unencripted_message,prime_number1,prime_number2,public_key)

        self.assertEqual(expected_encrypted_message,encrypted_message)

    def test_encryption2(self):

        public_key : int= 5
        prime_number1 :int= 97
        prime_number2 :int= 223
        expected_encrypted_message = [26, 10920, 13029, 6305, 4751, 13833, 3366, 10920, 21167, 8590, 4751, 20153, 10920, 4751, 20153, 10920, 8156, 4751, 18410, 6481, 3366, 8590, 4751, 10331, 12580, 3366, 10920]
        unencripted_message = 'hola profe no nos tire duro'

        encrypted_message = EncriptationEngine().encode_and_encrypt_message_with_inputs(unencripted_message,prime_number1,prime_number2,public_key)

        self.assertEqual(expected_encrypted_message,encrypted_message)
        

    def test_encryption3(self):

        public_key : int= 7
        prime_number1 :int= 97
        prime_number2 :int= 151
        expected_encrypted_message = [6679, 12377, 8066, 13620, 8818, 183, 6679, 3407, 8818, 14215, 8342, 14215, 13674, 183, 1463, 7109, 7694, 1953, 8066, 7830, 183, 13926, 12377, 8342, 1747, 8342, 3488, 8066, 7830]
        unencripted_message = 'profe piedad, muchos trabajos'

        encrypted_message = EncriptationEngine().encode_and_encrypt_message_with_inputs(unencripted_message,prime_number1,prime_number2,public_key)

        self.assertEqual(expected_encrypted_message,encrypted_message)
        

    def test_decryption1(self):

        public_key : int= 7
        prime_number1 :int= 97
        prime_number2 :int= 151
        encrypted_message = [6679, 12377, 8066, 13620, 8818, 183, 6679, 3407, 8818, 14215, 8342, 14215, 13674, 183, 1463, 7109, 7694, 1953, 8066, 7830, 183, 13926, 12377, 8342, 1747, 8342, 3488, 8066, 7830]
        expected_message = 'profe piedad, muchos trabajos'

        decrypted_message = EncriptationEngine().decode_and_decrypt_message(encrypted_message,public_key,prime_number1,prime_number2)

        self.assertEqual(decrypted_message,expected_message)


    def test_decryption2(self):

        public_key : int= 5
        prime_number1 :int= 97
        prime_number2 :int= 223
        encrypted_message = [26, 10920, 13029, 6305, 4751, 13833, 3366, 10920, 21167, 8590, 4751, 20153, 10920, 4751, 20153, 10920, 8156, 4751, 18410, 6481, 3366, 8590, 4751, 10331, 12580, 3366, 10920]
        expected_message = 'hola profe no nos tire duro'

        decrypted_message = EncriptationEngine().decode_and_decrypt_message(encrypted_message,public_key,prime_number1,prime_number2)

        self.assertEqual(decrypted_message,expected_message)

    def test_decryption3(self):

        public_key : int= 5
        prime_number1 :int= 29
        prime_number2 :int= 127
        encrypted_message = [17, 2212, 225, 2302, 1219, 257, 2302, 2478, 744, 55, 418, 744, 257, 2212, 55, 1552, 2095]
        expected_message = 'hay un mercenario'

        decrypted_message = EncriptationEngine().decode_and_decrypt_message(encrypted_message,public_key,prime_number1,prime_number2)

        self.assertEqual(decrypted_message,expected_message)

    #Error Case #1
    def test_message_empty_to_encrypt(self):

        public_key : int= 5
        prime_number1 :int= 29
        prime_number2 :int= 127

        unencrypted_message = ''

        self.assertRaises(EmptyMessageError,EncriptationEngine().encode_and_encrypt_message_with_inputs,unencrypted_message,prime_number1,prime_number2,public_key)

    #Error Case #2
    def test_empty_public_key_to_encrypt(self):

        public_key : int = None
        prime_number1 :int= 29
        prime_number2 :int= 127

        unencrypted_message = 'Son las 5 AM y no recuerdo nada'

        self.assertRaises(EmptyPublicKey,EncriptationEngine().encode_and_encrypt_message_with_inputs,unencrypted_message,prime_number1,prime_number2,public_key)
    
    #Error Case #3
    def test_empty_public_ket_to_decrypt(self):
    
        public_key : int = None
        prime_number1 :int= 181
        prime_number2 :int= 83

        encrypted_message = [5312, 9110, 9947, 4102, 2310, 5164, 14643, 4102, 3743, 4102, 4236, 272, 4102, 7228, 4102, 9947, 9110, 4102, 14562, 3400, 12460, 9256, 3400, 14562, 7838, 9110, 4102, 9947, 5164, 7838, 5164]

        self.assertRaises(EmptyPublicKey,EncriptationEngine().decode_and_decrypt_message,encrypted_message,public_key,prime_number1,prime_number2)
    
    #Error Case #4
    def test_empty_secret_key(self):
    
        public_key : int= 5
        prime_number1 :int= 29
        prime_number2 :int= 127

        encrypted_message = ''

        self.assertRaises(SyntaxError,EncriptationEngine().decode_and_decrypt_message,encrypted_message,public_key,prime_number1,prime_number2)

    #Error Case #5
    def test_encrypt_with_invalid_public_key(self):

        public_key = '17181,83'

        self.assertRaises(InvalidPublicKey,EncriptationEngine().secret_key_format_validator,public_key)

    #Error Case #6
    def test_encrypt_without_prime_number(self):

        public_key : int= 5
        prime_number1 :int= None
        prime_number2 :int= 127

        unencrypted_message = 'Ayuda estoy perdiendo la cordura'

        self.assertRaises(EmptyInputValuesError,EncriptationEngine().encode_and_encrypt_message_with_inputs,unencrypted_message,prime_number1,prime_number2,public_key)

    #Error Case #7
    def test_decrypt_without_prime_number(self):

        public_key : int= 5
        prime_number1 :int= 173
        prime_number2 :int= None

        encrypted_message = [27546, 16233, 36387, 35328, 38571, 38450, 27337, 20975, 28239, 5622, 16233, 38450, 32084, 27337, 6505, 35328, 990, 27337, 36777, 35328, 5622, 38450, 8957, 38571, 38450, 37734, 5622, 6505, 35328, 36387, 6505, 38571]

        self.assertRaises(EmptyInputValuesError,EncriptationEngine().decode_and_decrypt_message,encrypted_message,public_key,prime_number1,prime_number2)

    #Error Case #8
        
    def test_encryption_without_prime_numbers(self):

        unencrypted_message = "Cuando una fuerza actua sobre un objeto este se pone en movimiento"
        public_key= 17
        prime_number1 = 60
        prime_number2 = 20

        self.assertRaises(NonPrimeNumber,EncriptationEngine().encode_and_encrypt_message_with_inputs,unencrypted_message,prime_number1,prime_number2,public_key)
    

    #Exceptional Case #1
    def test_encryption_numbers(self):
    
        public_key : int= 5
        prime_number1 :int= 157
        prime_number2 :int= 79
        expected_encrypted_message = [9327, 6415, 11000, 11000, 1367, 3542, 1367, 2470, 1367, 3542, 2470, 5964]
        unencripted_message = '123385848546'

        encrypted_message = EncriptationEngine().encode_and_encrypt_message_with_inputs(unencripted_message,prime_number1,prime_number2,public_key)

        self.assertEqual(expected_encrypted_message,encrypted_message)

    #Exceptional Case #2
    def test_encrytion_with_single_letter(self):
    
        public_key : int= 5
        prime_number1 :int= 37
        prime_number2 :int= 3
        expected_encrypted_message = [82]
        unencripted_message = 'a'

        encrypted_message = EncriptationEngine().encode_and_encrypt_message_with_inputs(unencripted_message,prime_number1,prime_number2,public_key)

        self.assertEqual(expected_encrypted_message,encrypted_message)

    #Exceptional Case #3
    def test_especial_characters_encryption(self):
    
        public_key : int= 7
        prime_number1 :int= 151
        prime_number2 :int= 59
        expected_encrypted_message = [2133, 5290, 3193, 8805, 4496, 3928, 5290, 2133, 6581, 4496]
        unencripted_message = '@%$*#&%@(#'

        encrypted_message = EncriptationEngine().encode_and_encrypt_message_with_inputs(unencripted_message,prime_number1,prime_number2,public_key)

        self.assertEqual(expected_encrypted_message,encrypted_message)

    #Exceptional Case #4
    def test_decryption_of_numbers(self):

        public_key : int= 5
        prime_number1 :int= 157
        prime_number2 :int= 79
        expected_unencrypted_message = '123385848546'
        encrypted_message = [9327, 6415, 11000, 11000, 1367, 3542, 1367, 2470, 1367, 3542, 2470, 5964]

        encrypted_message = EncriptationEngine().decode_and_decrypt_message(encrypted_message,public_key,prime_number1,prime_number2)

        self.assertEqual(expected_unencrypted_message,encrypted_message)

    #Exceptional Case #5
    def test_decryp_single_letter(self):

        public_key : int= 5
        prime_number1 :int= 37
        prime_number2 :int= 3
        expected_unencrypted_message = 'a'
        encrypted_message = [82]

        encrypted_message = EncriptationEngine().decode_and_decrypt_message(encrypted_message,public_key,prime_number1,prime_number2)

        self.assertEqual(expected_unencrypted_message,encrypted_message)

    #Exceptional Case #6
    def test_especial_characters_decryption(self):

        public_key : int= 7
        prime_number1 :int= 151
        prime_number2 :int= 59
        encrypted_message = [2133, 5290, 3193, 8805, 4496, 3928, 5290, 2133, 6581, 4496]
        expected_unencrypted_message = '@%$*#&%@(#'

        encrypted_message = EncriptationEngine().decode_and_decrypt_message(encrypted_message,public_key,prime_number1,prime_number2)

        self.assertEqual(expected_unencrypted_message,encrypted_message)

if __name__ == '__main__':
    unittest.main()