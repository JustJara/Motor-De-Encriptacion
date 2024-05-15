'''
Module for handling database operations
'''
import sys
import psycopg2
sys.path.append('src/controller/')
import secret_config

from psycopg2.errors import *


class DatabaseController:

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

    def table_users_exists(self) -> bool:
        """
        Checks if the table named 'Users' exists in the database

        Verifica si la tabla llamada 'Users' existe en la base de datos

        Returns:
        --------    
        bool
            True if the table exists, False otherwise
            Verdadero si la tabla existe, Falso en caso contrario
        """
        cursor = self.get_cursor()
        sql_sentence = ''

        with open('sql_sentences/check_users_table_existence.sql', 'r') as file:
            sql_sentence = file.read() 


        cursor.execute(sql_sentence)
        response = cursor.fetchone()
        table_exists = response[0]
        if table_exists:
            return table_exists
        else:
            return False

    def table_users_messages_exists(self) -> bool:
        """
        Checks if the table named 'Users_messages' exists in the database

        Verifica si la tabla llamada 'Users_messages' existe en la base de datos

        Returns:
        --------    
        bool
            True if the table exists, False otherwise
            Verdadero si la tabla existe, Falso en caso contrario
        """
        cursor = self.get_cursor()
        sql_sentence = ''

        with open('sql_sentences/check_users_messages_table_existence.sql', 'r') as file:
            sql_sentence = file.read() 


        cursor.execute(sql_sentence)
        response = cursor.fetchone()
        table_exists = response[0]
        if table_exists:
            return table_exists
        else:
            return False

        
    def create_table(self):
        """
        Creates user table in case it does not exist
        """


        sql_sentence = ''
        with open('sql_sentences/create_table.sql', 'r') as file:
            sql_sentence = file.read()

        cursor = self.get_cursor()
        cursor.execute(sql_sentence)
        cursor.connection.commit()

    def delete_table(self):
        """
        Deletes the table named 'users' and 'users_messages' in the database

        """
        cursor = self.get_cursor()
        sql_sentence = ''
        with open('sql_sentences/delete_table.sql', 'r') as file:
            sql_sentence = file.read()

        cursor.execute(sql_sentence)
        cursor.connection.commit()

        

    def register_user_db(self,user):
        """
        Inserts a new user in the database

        """

        """
        Parameters:

        -----------
        username : str
            Username to be inserted in the database /
            Nombre de usuario a ingresar en la base de datos

        password : str
            Password to be inserted in the database /
            Contraseña a ingresar en la base de datos


        """


        cursor = self.get_cursor()
                
        sql_sentence = ''
        with open('sql_sentences/insert_user.sql', 'r') as file:
            sql_sentence = file.read()
        cursor.execute(sql_sentence, (user.username, user.password))
        response = cursor.connection.commit()
        print(response)
        return True




    def insert_user_messages(self,username: str, secret_key: str, encrypted_message: str, original_message: str):
        """
        Inserts a new secret message in the database


        Parameters:

        -----------

        username: str
            Username to be inserted in the database /
            Nombre de usuario a ingresar en la base de datos

        secret_key: str
            Secret key to be inserted in the database /
            Clave secreta a ingresar en la base de datos
        
        encrypted_message: str
            Encrypted message to be inserted in the database /
            Mensaje encriptado a ingresar en la base de datos

        original_message: str
            Original message to be inserted in the database /
            Mensaje original a ingresar en la base de datos

        """
        cursor = self.get_cursor()
        sql_sentence = ''
        with open('sql_sentences/insert_users_messages.sql', 'r') as file:
            sql_sentence = file.read()
        
        cursor.execute(sql_sentence, (username, secret_key, encrypted_message, original_message))
        cursor.connection.commit()
        return True


    def find_user_in_database(self,username : str):
        """
        Searches for a user by username

        Parameters:

        -----------

        username: str
            Username to be searched in the database /
            Nombre de usuario a buscar en la base de datos

        """
        cursor = self.get_cursor()
        sql_sentence = ''
        with open('sql_sentences/search_user.sql', 'r') as file:
            sql_sentence = file.read()

        cursor.execute(sql_sentence, (username,))
        response = cursor.fetchone()
        return response

    def check_username_existence(self, username : str):
        """
        Checks if username already exists in the database

        Verifica si el nombre de usuario ya existe en la base de datos

        Parameters:

        -----------

        username: str
            Username to be checked in the database /
            Nombre de usuario a verificar en la base de datos

        """
        
        cursor = self.get_cursor()
        sql_sentence = ''
        with open('sql_sentences/check_username_existence.sql', 'r') as file:
            sql_sentence = file.read()

        cursor.execute(sql_sentence, (username,))
        response = cursor.fetchone()
        if response != None:
            return response[0]
        return response

    def get_user_messages(self, username: str):
        """
        Gets all the messages of a user

        Obtiene todos los mensajes de un usuario

        Parameters:

        -----------

        username: str
            Username to be searched in the database /
            Nombre de usuario a buscar en la base de datos

        """
        cursor = self.get_cursor()
        sql_sentence = ''
        with open('sql_sentences/get_users_messages.sql', 'r') as file:
            sql_sentence = file.read()

        cursor.execute(sql_sentence, (username,))
        response = cursor.fetchall()
        return response

    def change_user_passcode(self,username:str,new_passcode:str) -> bool:
        """
        Changes the passcode of a user

        Cambia el passcode de un usuario

        Parameters:

        -----------

        new_passcode: str
            New passcode to be updated in the database /
            Nuevo passcode a actualizar en la base de datos

        """
        user_existence = self.check_username_existence(username)
        if user_existence == None:
            raise UniqueViolation('El nombre de usuario NO existe')
        cursor = self.get_cursor()
        sql_sentence = ''
        with open('sql_sentences/change_user_passcode.sql', 'r') as file:
            sql_sentence = file.read()

        cursor.execute(sql_sentence, (new_passcode,username))
        cursor.connection.commit()
        return True
    
    def login_user_db(self,user) -> bool:
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

        bool
            True if the user logs in successfully, False otherwise /
            Verdadero si el usuario inicia sesión correctamente, Falso en caso contrario
        '''

        user_finded = self.check_username_existence(user.username)
        if user_finded == None:
            raise Exception('El nombre de usuario no está registrado. Intente nuevamente o regístrese.')
        else:
            user_in_db = self.find_user_in_database(user.username)

            if user_in_db[0] == user.username and user_in_db[1] == user.password:
                print('Inicio de sesión exitoso')
                return True
            return False

    def delete_user_messages(self,username:str) -> bool:
        """
        Deletes all the messages of a user

        Elimina todos los mensajes de un usuario

        Parameters:

        -----------

        username: str
            Username to be deleted in the database /
            Nombre de usuario a eliminar en la base de datos

        """
        if self.get_user_messages(username) == []:
            raise Exception('El usuario no tiene mensajes para eliminar')
        cursor = self.get_cursor()
        sql_sentence = ''
        with open('sql_sentences/delete_user_messages.sql', 'r') as file:
            sql_sentence = file.read()

        cursor.execute(sql_sentence, (username,))
        cursor.connection.commit()
        return True

