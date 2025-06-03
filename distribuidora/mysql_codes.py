import mysql.connector

# This code is used to connect to a MySQL database and execute commands on it.
connection = mysql.connector.connect(
        host='localhost',
        user = 'root',
        password = 'root',
        database = 'distribuidora'
    )
cursor = connection.cursor()

# This function is used to close the connection to the database
def close_connection():
    cursor.close()
    connection.close()

# This function is used to execute INSERT, UPDATE, DELETE commands
def execute_command(command):
    """Execute a command on the MySQL database."""
    try:
        cursor.execute(command)
        connection.commit()
        return True
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return False

# This function is used to execute READ commands
def read_data(command):
    """Read data from the MySQL database."""
    try:
        cursor.execute(command)
        return cursor.fetchall()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None