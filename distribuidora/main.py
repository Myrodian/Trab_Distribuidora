from mysql_codes import *
from fake_data import *

def menu():
    """Display the main menu."""
    print("Menu:")
    print("1. Generate Data")
    print("2. Execute Command")
    print("3. Read Data")
    print("4. Exit")



def insert_pessoa():
    """Insert a new person into the database."""
    nome = str(input("Enter name: "))
    email = str(input("Enter email: "))
    cpf = int(input("Enter cpf: "))
    data_nascimento = input("Enter data nascimento: ")
    command = f'INSERT INTO pessoa (nome, email, cpf, data_nascimento) VALUES ("{nome}", "{email}", {cpf}, "{data_nascimento}")'
    execute_command(command)
    pessoa_id = read_data(f'SELECT id FROM pessoa WHERE nome = "{nome}"')[0][0]
    print("Pessoa inserted successfully.", pessoa_id)
    return pessoa_id

## CREATE
def insert_funcionario(cargo_id):
    pessoa_id = insert_pessoa()
    data_atual = "a"
    matricula = str(input("Enter matricula: "))
    command = f'INSERT INTO funcionario (data_admissao, matricula, Pessoa_id, Cargo_id) VALUES("{data_atual}", "{matricula}", {pessoa_id}, {cargo_id})'
    execute_command(command)

## UPDATE
def update_pessoa(pessoa_id):
    nome = str(input("Enter new name: "))
    email = str(input("Enter new email: "))
    cpf = int(input("Enter new cpf: "))
    data_nascimento = input("Enter new data nascimento: ")
    command = f'UPDATE pessoa SET nome="{nome}", email="{email}", cpf={cpf}, data_nascimento="{data_nascimento}" WHERE id={pessoa_id}'
    execute_command(command)

if __name__ == '__main__':
    generate_data()
    # insert_funcionario(4)
    # command = 'SELECT nome FROM funcionario JOIN cargo ON funcionario.Cargo_id = cargo.id'
    command = 'DELETE FROM pessoa where nome="Nasser"'
    execute_command(command) # for DELETE, UPDATE, INSERT commands
    # results = read_data(command) # for READ commands
    # for row in results:
    #     print(row)
    close_connection()

