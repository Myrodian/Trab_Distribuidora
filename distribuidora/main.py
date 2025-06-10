from mysql_codes import *
from fake_data import *

def menu():
    """Display the main menu."""
    print("Menu:")
    print("1. Generate Data")
    print("2. Execute Command")
    print("3. Read Data")
    print("4. Exit")

if __name__ == '__main__':
    generate_data()

    command = 'SELECT nome FROM funcionario JOIN cargo ON funcionario.Cargo_id = cargo.id'

    # execute_command(command) # for DELETE, UPDATE, INSERT commands
    results = read_data(command) # for READ commands
    for row in results:
        print(row)
    close_connection()
