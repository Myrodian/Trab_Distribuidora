import mysql.connector

# Conexão com o banco de dados MySQL
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='distribuidora'
)

cursor = connection.cursor(dictionary=True)

# Fecha a conexão com o banco de dados
def close_connection():
    cursor.close()
    connection.close()

# Executa comandos INSERT, UPDATE, DELETE com suporte a parâmetros
def execute_command(command, params=None):
    try:
        if params:
            cursor.execute(command, params)
        else:
            cursor.execute(command)
        connection.commit()
        return True
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return False

# Executa comandos SELECT com suporte a parâmetros
def read_data(command, params=None):
    try:
        if params:

            cursor.execute(command, params)
        else:
            cursor.execute(command)
        return cursor.fetchall()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
