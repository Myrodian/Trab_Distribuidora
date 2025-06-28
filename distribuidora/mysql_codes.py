import mysql.connector

# Conexão com o banco de dados MySQL
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='distribuidora'
)

cursor = connection.cursor()

# Fecha a conexão com o banco de dados
def close_connection():
    cursor.close()
    connection.close()

# Executa comandos INSERT, UPDATE, DELETE com suporte a parâmetros
def execute_command(command, params=None):
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='distribuidora'
        )
        cursor = conn.cursor()
        if params:
            cursor.execute(command, params)
        else:
            cursor.execute(command)
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return False


# Executa comandos SELECT com suporte a parâmetros
def read_data(query, params=None):
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='distribuidora'
        )
        cursor = conn.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    
def write_data(query, params):
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='distribuidora'
    )
    cursor = conn.cursor()
    cursor.execute(query, params)
    conn.commit()
    linhas_afetadas = cursor.rowcount
    cursor.close()
    conn.close()
    return linhas_afetadas