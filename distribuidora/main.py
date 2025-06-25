from fake_data import *
from codes_crud import *

def cadastrarpessoa():
    # cadastrar pessoa CREATE
    pessoa = Pessoa()  # cria um objeto Pessoa
    pessoa.nome = input("Digite o nome da pessoa: ")
    pessoa.email = input("Digite o email da pessoa: ")
    pessoa.cpf = input("Digite o CPF da pessoa: ")
    pessoa.data_nascimento = input("Digite a data de nascimento da pessoa ( YYYY-MM-DD ): ") # DD/MM/YYYY
    pessoa.salvar()  # chama o metodo salvar para inserir os dados no BANCO DE DADOS
    print(pessoa)
    print (f"Nome:{pessoa.nome}\nEmail:{pessoa.email}\nCPF:{pessoa.cpf}\nData de Nascimento:{pessoa.data_nascimento}")


if __name__ == '__main__':
    generate_data()
    # cadastrarpessoa()
    # pessoa = Pessoa() # cria um objeto Pessoa
    # #exibindo a pessoa de id 1
    # pessoa.carregar(1) #chama o metodo carregar para carregar os dados da pessoa com ID 1
    # print(pessoa.nome)
    # print(pessoa.email)
    # print(pessoa.cpf)
    # print(pessoa.data_nascimento)
    #
    # # Atualizando os dados da pessoa de id 1
    # pessoa.nome = "João Silva"
    # pessoa.salvar() # chama o metodo salvar para atualizar os dados no BANCO DE DADOS da pessoa com ID 1
    #
    # # Exibindo os dados atualizados da pessoa de id 1
    # print(pessoa.nome)
    # print(pessoa.email)
    # print(pessoa.cpf)
    # print(pessoa.data_nascimento)

    pessoa = Pessoa() # cria um objeto Pessoa
    #
    # pessoa.nome = "nasser"
    # pessoa.email = "nasser@gmail.com"
    # pessoa.cpf = "12328910371"
    # pessoa.data_nascimento = "1999-01-01"
    # pessoa.salvar()
    # pessoa.carregar(1)
    # print(pessoa)
    # # Deletando a pessoa de id 1
    # pessoa.deletar() # chama o metodo deletar para deletar os dados da pessoa com ID 1

    # fornecedor = Fornecedor()  # cria um objeto Fornecedor
    # fornecedor.carregar(1) # carrega os dados do fornecedor com ID 1
    # pessoa.associar_fornecedor(fornecedor)



    fornecedor = Fornecedor()  # cria um objeto Fornecedor
    opcao = 1
    fornecedor.carregar(opcao)

    donos = fornecedor.listar_pessoas()
    for dono in donos:
        print(dono)

    # fornecedor.email_contato = "emailnovodofornecedor4@gmail.com"
    # fornecedor.salvar()

    close_connection()
