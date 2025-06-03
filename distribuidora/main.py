from mysql_codes import *
from fake_data import *



if __name__ == '__main__':
    generate_data()

    command = 'SELECT * FROM pessoa'
    results = read_data(command)
    print(type(results))
    print(results)
    close_connection()