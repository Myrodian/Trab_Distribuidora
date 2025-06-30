import mysql.connector 

# Conexão com o banco de dados MySQL (global)
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
        cursor.execute(command, params)
        connection.commit()
        last_id = cursor.lastrowid
        affected = cursor.rowcount
        return True, last_id if affected > 0 else None
    except mysql.connector.Error as err:
        print(f"Erro: {err}")
        return False, None

# Executa comandos SELECT com suporte a parâmetros
def read_data(query, params=None):
    try:
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        return cursor.fetchall()
    except mysql.connector.Error as err:
        print(f"Erro: {err}")
        return None

# Executa comandos INSERT/UPDATE/DELETE e retorna número de linhas afetadas
def write_data(query, params):
    try:
        cursor.execute(query, params)
        connection.commit()
        return cursor.rowcount
    except mysql.connector.Error as err:
        print(f"Erro: {err}")
        return 0
