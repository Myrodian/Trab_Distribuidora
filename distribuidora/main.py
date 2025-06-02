from mysql_codes import *
from fake_data import *



if __name__ == '__main__':
    connection, cursor = create_connection()
    generate_data(connection, cursor)

    command = 'SELECT * FROM pessoa'
    results = read_data(cursor, command)
    print(type(results))
    print(results)
    close_connection(connection, cursor)