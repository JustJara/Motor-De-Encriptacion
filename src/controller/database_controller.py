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

def insert_user(username: str, password : str):
    """
    Inserts a new user in the database

    """

    """
    
    cursor = get_cursor()

    #Check if user already exists in data

    """

def insert_user_messages(username: str, secret_key: str, encrypted_message: str, original_message: str):
    """
    Inserts a new secret message in the database


    Parameters:

    -----------

    """


def search_by_username(username : str):
    """
    Searches for a user by username
    """

