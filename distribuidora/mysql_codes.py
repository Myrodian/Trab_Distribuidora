import mysql.connector

def create_connection():
    """Create a connection to the MySQL database."""
    connection = mysql.connector.connect(
        host='localhost',
        user = 'root',
        password = 'root',
        database = 'distribuidora'
    )
    cursor = connection.cursor()
    return connection, cursor

def close_connection(connection, cursor):
    cursor.close()
    connection.close()

def execute_command(connection, cursor , command):
    """Execute a command on the MySQL database."""
    try:
        cursor.execute(command)
        connection.commit()
        return True
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return False

def read_data(cursor, command):
    """Read data from the MySQL database."""
    try:
        cursor.execute(command)
        return cursor.fetchall()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

