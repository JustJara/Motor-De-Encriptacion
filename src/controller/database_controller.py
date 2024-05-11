'''
Module for handling database operations
'''
import sys
import psycopg2
import secret_config

sys.path.append('encryption_engine/src')


def get_cursor():
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

def create_table():
    """
    Creates user table in case it does not exist
    """

    sql = ''
    with open('src/controller/create_table.sql', 'r') as file:
        sql = file.read()

    cursor = get_cursor()

    try:
        cursor.execute(sql)
        cursor.connection.commit()
    except:
        cursor.connection.rollback()
    

def insert_user(username: str, password : str):
    """
    Inserts a new user in the database

    """

    """
    
    cursor = get_cursor()

    #Check if user already exists in data

    Parameters:

    -----------
    username : str
        Username to be inserted in the database /
        Nombre de usuario a ingresar en la base de datos

    password : str
        Password to be inserted in the database /
        Contraseña a ingresar en la base de datos

    """

def insert_user_messages(username: str, secret_key: str, encrypted_message: str, original_message: str):
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


def search_by_username(username : str):
    """
    Searches for a user by username

    Parameters:

    -----------

    username: str
        Username to be searched in the database /
        Nombre de usuario a buscar en la base de datos

    """

