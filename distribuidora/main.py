from mysql_codes import *
from fake_data import *


if __name__ == '__main__':
    generate_data()

    command = 'SELECT nome FROM funcionario INNER JOIN cargo ON funcionario.Cargo_id = cargo.id'

    # execute_command(command) # for DELETE, UPDATE, INSERT commands
    results = read_data(command) # for READ commands
    for row in results:
        print(row)
    close_connection()
