from fake_data import *
from Models import *

def adicionar_produto():
    nome = input("Qual o nome do novo produto? ")

    try:
        preco_unitario = float(input("Qual o valor unitário? "))
    except ValueError:
        print("Valor inválido. Operação cancelada.")
        return menu_produtos()

    observacoes = input("Alguma observação? (opcional): ").strip()
    if not observacoes:
        observacoes = None

    Fornecedor.listar_todos()
    try:
        fornecedor_id = int(input("Qual o ID do fornecedor que fornece esse produto? "))
    except ValueError:
        print("ID inválido. Operação cancelada.")
        return menu_produtos()

    estoque_str = input("Deseja adicionar uma quantidade ao estoque? (opcional): ").strip()
    try:
        estoque_inicial = int(estoque_str) if estoque_str else 0
    except ValueError:
        print("Quantidade inválida. Definido como 0.")
        estoque_inicial = 0

    produto = Produto(
        nome=nome,
        preco_unitario=preco_unitario,
        observacoes=observacoes,
        fornecedor_id=fornecedor_id,
        quantidade_estoque=estoque_inicial
    )
    produto.salvar()

    print("Produto inserido com sucesso!")
    return menu_produtos()

def editar_produto():
    try:
        produto_id = int(input("Qual o ID do produto que deseja alterar? "))
    except ValueError:
        print("ID inválido.")
        return menu_produtos()

    produto = Produto()
    if not produto.carregar(produto_id):
        print("Produto não encontrado!")
        return menu_produtos()

    print("\nDeixe em branco para manter os valores atuais:")
    print(produto.nome)
    nome_input = input(f"Nome atual: {produto.nome}. Novo nome: ").strip() #strip serve para remover espaços em branco no início e no final da string
    nome = nome_input if nome_input else produto.nome
    print(nome)
    preco_input = input(f"Preço atual: R$ {produto.preco_unitario:.2f}. Novo preço: ").strip()
    try:
        preco = float(preco_input) if preco_input else produto.preco_unitario
    except ValueError:
        print("Valor inválido. Mantendo o preço atual.")
        preco = produto.preco_unitario

    observacoes_input = input(f"Observações atuais: {produto.observacoes or 'Nenhuma'}. Nova observação: ").strip()
    observacoes = observacoes_input if observacoes_input else produto.observacoes

    Fornecedor.listar_todos()
    fornecedor_input = input(f"ID do fornecedor atual: {produto.fornecedor_id}. Novo ID: ").strip()
    try:
        fornecedor_id = int(fornecedor_input) if fornecedor_input else produto.fornecedor_id
    except ValueError:
        print("ID inválido. Mantendo o atual.")
        fornecedor_id = produto.fornecedor_id

    estoque_input = input(f"Estoque atual: {produto.quantidade_estoque or 0}. Novo estoque (opcional): ").strip()
    if estoque_input:
        try:
            nova_qtd_estoque = int(estoque_input)
            produto.definir_estoque(nova_qtd_estoque)
        except ValueError:
            print("Quantidade inválida. Estoque não alterado.")
    #observe que essa forma de atualizar é diferente da de adicionar. essa eu atualizo o objeto já existente, enquanto na de adicionar eu crio um novo objeto.
    # Atualiza os campos
    produto.nome = nome
    produto.preco_unitario = preco
    produto.observacoes = observacoes
    produto.fornecedor_id = fornecedor_id

    produto.salvar()
    return menu_produtos()

def deletar_produto():
    try:
        produto_id = int(input("Qual o ID do produto que deseja excluir? "))
    except ValueError:
        print("ID inválido.")
        return menu_produtos()

    produto = Produto()
    if not produto.carregar(produto_id):
        print("Produto não encontrado!")
        return menu_produtos()

    confirmacao = input(f"Tem certeza que deseja excluir o produto '{produto.nome}'? (s/n): ").strip().lower()
    if confirmacao == 's':
        produto.deletar()
        print("Produto excluído com sucesso!")
    else:
        print("Operação cancelada.")

    return menu_produtos()

def menu_produtos():
    Produto.listar_todos()

    print("<========================================> Menu Produto <========================================>")
    print("0 - Voltar ao menu principal")
    print("1 - Adicionar produto")
    print("2 - Editar produto")
    print("3 - Excluir produto")

    opcao = input("Digite uma opção: ")

    if opcao == "0":
        return menu()

    elif opcao == "1":
        return adicionar_produto()

    elif opcao == "2":
        return editar_produto()

    elif opcao == "3":
        return deletar_produto()

    #TODO elif opcao == "4": alterar estoque de tal produto (hardcoded)
    #TODO fazer a opção de alterar o estoque de um produto específico
    #TODO fazer movimentação de estoque, ou seja, adicionar ou remover quantidade de um produto específico (softcoded)

    else:
        print("Opção inválida.")
        return menu_produtos()

def menu():
    print("0 - Sair")
    print("1 - Ir para o menu de produtos")
    print("2 - Ir para o menu de fornecedores")

    op = input("Digite uma opção: ")
    if op == "0":
        return
    elif op == "1":
        menu_produtos()
    else:
        print("Opção inválida, tente novamente.")
        menu()

if __name__ == '__main__':
    generate_data()
    menu()
    close_connection()
