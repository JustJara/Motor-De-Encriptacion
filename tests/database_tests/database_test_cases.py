import unittest
import sys
import psycopg2
from psycopg2.errors import *
sys.path.append('src')

from encriptation_algorithm.encriptation_algorithm import *
import secret_config
import database_controller
'''
This class contains the test cases for
'''

class DataBaseTestCases(unittest.TestCase):

    def setUpClass():
        DatabaseController().delete_table()
        DatabaseController().create_table()


    def get_cursor(self):
        """
        Create the database connection and returns the cursor, and execute the instructions
        """

        DATABASE = secret_config.PGDATABASE
        USER = secret_config.PGUSER
        PASSWORD = secret_config.PGPASSWORD
        HOST = secret_config.PGHOST
        PORT = secret_config.PGPORT

        connection =  psycopg2.connect(database = DATABASE, user = USER, password = PASSWORD, host = HOST, port = PORT)

        return connection.cursor()
    
    def test_check_existing_table(self):
        '''
        Valida que la tabla de usuarios exista

        Validates that the users table exists
        '''
        
        #Se almacena la respuesta del método que verifica si la tabla de usuarios existe
        response = DatabaseController().table_users_exists()
        self.assertEqual(response, True)

    def test_create_existing_table(self):
        '''
        Valida que no se pueda crear una tabla que ya existe

        Validates that a table that already exists cannot be created
        '''

        #Se valida que el método de crear la tabla devuelva el erorr de tabla duplicada.
        self.assertRaises(psycopg2.errors.DuplicateTable,DatabaseController().create_table)

    def test_register_user(self):
        ''''
        Valida que se pueda registrar un usuario en la base de datos
        
        Validates that a user can be registered in the database
        '''
        
        username = 'testusername'
        passcode = 'test_passcode123'

        user = User(username,passcode)

        expected_output : bool = DatabaseController().register_user_db(user) 

        self.assertEqual(expected_output,True)
    
    def test_register_existing_user(self):
        ''''
        Valida que no se pueda crear un usuario con el mismo nombre de usuario que otro ya registrado

        Validates that a user cannot be created with the same username as another already registered
        '''
        
        username1 = 'test1username'
        passcode1 = 'test_passcode'

        username2 = 'test1username'
        passcode2 = 'test_passcode'

        user1 = User(username1,passcode1)
        user2 = User(username2,passcode2)
        
        DatabaseController().register_user_db(user1)

        self.assertRaises(IntegrityError,DatabaseController().register_user_db,user2)
        
    def test_login_user(self):
        ''''
        Valida que un usuario pueda inicar sesion correctamente
        
        Validates that a user can log in correctly       
        '''
        
        username = 'test_username_l'
        passcode = 'test_passcode_l'

        test_user = User(username, passcode)

        DatabaseController().register_user_db(test_user)

        expected_output : bool = DatabaseController().login_user_db(test_user)
        
        self.assertEqual(expected_output, True)
        
        
    def test_login_user_that_doesnt_exist(self):
        '''
        Valida que no se pueda iniciar sesion con un usuario que no existe (no esté registrado)
        
        Validates that a user that doesn´t exist (isn´t registered) cannot login
        '''
        
        username = 'test_username34534'
        passcode = 'test_passcode34534'
        user = User(username, passcode)

        self.assertRaises(Exception,DatabaseController().login_user_db,user)


    def test_change_user_passcode(self):
        '''
        Valida que se pueda cambiar la contraseña de un usuario
        
        Validates that a user´s password can be changed
        '''
        
        username = 'test_usern4me'
        passcode = 'test_passcode'
        new_passcode = 'new_test_passcode'

        user = User(username, passcode)

        DatabaseController().register_user_db(user)

        expected_output = DatabaseController().change_user_passcode(username,new_passcode)

        self.assertEqual(expected_output,True)

    def test_delete_all_user_messages(self):

        '''
        Valida que se puedan eliminar todos los mensajes de un usuario
        
        Validates that all messages from a user can be deleted
        '''
        
        username = 'test_username'
        passcode = 'test_passcode'

        user = User(username, passcode)

        DatabaseController().register_user_db(user)

        DatabaseController().insert_user_messages(username,'[123,123,122]','[123,1234,123,1234,1234,124,124]','test_message')


        expected_output = DatabaseController().delete_user_messages(username)

        self.assertEqual(expected_output,True)

    def test_delete_all_user_messages_with_table_empty(self):
        '''
        Valida que se lance una exepción cuando se intente borrar mensajes y no hayan para mensajes en la tabla

        Validates that an exception is thrown when trying to delete messages and there are no messages in the table    
        '''

        username = 'username_test'
        passcode = 'passcode_test'

        user = User(username, passcode)

        DatabaseController().register_user_db(user)

        self.assertRaises(Exception,DatabaseController().delete_user_messages,username)
        
    def test_change_error_passcode(self):
        '''
        Valida que no se pueda cambiar la contraseña de un usuario que no existe
        
        Validates that the password of a user that doesn´t exist cannot be changed
        '''
        
        username = 'unexistent_username'
        passcode = 'test_passcode'
        new_passcode = 'new_test_passcode'

        self.assertRaises(UniqueViolation,DatabaseController().change_user_passcode,username,new_passcode)

    #Falta el de cambiar contraseña que de error
    


if __name__ == 'main':
    unittest.main()



        

    
    