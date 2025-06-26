from fake_data import *
from Models import *

def menu_produtos():
    Produto.listar_todos()

    print("0 - Sair")
    print("1 - Adicionar produto")
    print("2 - Editar produto")
    print("3 - Excluir produto")
    op = input("Digite uma opção: ")



def menu():
    print("0 - Sair")
    print("1 - Gerar dados")
    print("2 - Listar todos os produtos")
    print("3 - Listar todos os clientes")
    print("4 - Listar todas as vendas")
    op = input("Digite uma opção: ")
    if op == "0":
        return 0
    elif op == "1":
        print("\nGerar dados")
    elif op == "2":
        menu_produtos()



if __name__ == '__main__':
    generate_data()
    menu()
    close_connection()
