from fake_data import *
from codes_crud import *

def menu():
    # """Display the main menu."""
    print("Menu:")
    print("1. Generate Data")
    print("2. Execute Command")
    print("3. Read Data")
    print("4. Exit")

if __name__ == '__main__':
    generate_data()

    pessoa1 = Pessoa() # cria um objeto Pessoa
    #exibindo a pessoa de id 1
    pessoa1.carregar(1) #chama o metodo carregar para carregar os dados da pessoa com ID 1
    print(pessoa1.nome)
    print(pessoa1.email)
    print(pessoa1.cpf)
    print(pessoa1.data_nascimento)

    # Atualizando os dados da pessoa de id 1
    pessoa1.nome = "João Silva"
    pessoa1.email = "joaozinho@gmail.com"
    pessoa1.cpf = "12345699912"
    pessoa1.data_nascimento = "1990-01-01"
    pessoa1.salvar() # chama o metodo salvar para atualizar os dados no BANCO DE DADOS da pessoa com ID 1

    # Exibindo os dados atualizados da pessoa de id 1
    print(pessoa1.nome)
    print(pessoa1.email)
    print(pessoa1.cpf)
    print(pessoa1.data_nascimento)

    # # Deletando a pessoa de id 1
    pessoa1.deletar() # chama o metodo deletar para deletar os dados da pessoa com ID 1