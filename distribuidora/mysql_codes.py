import mysql.connector

connection = mysql.connector.connect(
        host='localhost',
        user = 'root',
        password = 'root',
        database = 'distribuidora'
    )
cursor = connection.cursor()

def close_connection():
    cursor.close()
    connection.close()

def execute_command(command):
    """Execute a command on the MySQL database."""
    try:
        cursor.execute(command)
        connection.commit()
        return True
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return False

def read_data(command):
    """Read data from the MySQL database."""
    try:
        cursor.execute(command)
        return cursor.fetchall()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

