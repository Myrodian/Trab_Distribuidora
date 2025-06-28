from fake_data import *
from Models import *

def adicionar_pessoa():
    nome = input("Digite o nome da pessoa: ").strip()
    email = input("Digite o email: ").strip()
    cpf = input("Digite o CPF: ").strip()
    data_nascimento = input("Digite a data de nascimento (YYYY-MM-DD): ").strip()
    observacoes = input("Alguma observação? (opcional): ").strip()
    
    pessoa = Pessoa(
        nome=nome,
        email=email,
        cpf=cpf,
        data_nascimento=data_nascimento,
        observacoes=observacoes  # Adicionando observações como atributo opcional
    )
    pessoa.salvar()

    
def editar_pessoa():
    try:
        pessoa_id = int(input("Digite o ID da pessoa que deseja editar: "))
    except ValueError:
        print("ID inválido.")
        return menu_pessoas()

    pessoa = Pessoa() 

    print("Deixe em branco para manter o valor atual.")
    nome = input(f"Nome atual: {pessoa.nome}. Novo nome: ").strip() or pessoa.nome
    email = input(f"Email atual: {pessoa.email}. Novo email: ").strip() or pessoa.email
    cpf = input(f"CPF atual: {pessoa.cpf}. Novo CPF: ").strip() or pessoa.cpf
    data_nascimento = input(f"Data de nascimento atual: {pessoa.data_nascimento}. Nova data: ").strip() or pessoa.data_nascimento

    pessoa.nome = nome
    pessoa.email = email
    pessoa.cpf = cpf
    pessoa.data_nascimento = data_nascimento

    pessoa.salvar()
    print("Pessoa atualizada com sucesso!")
    return menu_pessoas()

def deletar_pessoa():
    try:
        pessoa_id = int(input("Digite o ID da pessoa que deseja deletar: "))
    except ValueError:
        print("ID inválido.")
        return menu_pessoas()

    pessoa = Pessoa()
    if not pessoa.carregar(pessoa_id):
        return menu_pessoas()

    confirm = input(f"Tem certeza que deseja deletar a pessoa '{pessoa.nome}'? (s/n): ").strip().lower()
    if confirm == 's':
        pessoa.deletar()
    else:
        print("Operação cancelada.")
    return menu_pessoas()

def menu_pessoas():
    Pessoa.listar_todas()

    print("<========================================> Menu Pessoas <========================================>")
    print("0 - Voltar ao menu principal")
    print("1 - Adicionar pessoa")
    print("2 - Editar pessoa")
    print("3 - Deletar pessoa")

    opcao = input("Escolha uma opção: ")

    if opcao == "0":
        return menu()
    elif opcao == "1":
        return adicionar_pessoa()
    elif opcao == "2":
        return editar_pessoa()
    elif opcao == "3":
        return deletar_pessoa()
    else:
        print("Opção inválida.")
        return menu_pessoas()


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

def menu_juncoes():
    print("<========================================> Menu Junções <========================================>")
    print("0 - Voltar")
    print("1 - Exibir produtos com os seus estoques")
    print("2 - Exibir todos os produtos com seus fornecedores")
    print("3 - Exibir todos os funcionarios com seus nomes e cargos")
    print("4 - exibir todos os clientes")
    opcao = input("Digite uma opção: ")
    if opcao == "0":
        return menu_trabalho()
    elif opcao == "1":
        Produto.listar_todos()
        print("Exibindo todos os produtos com seus estoques.")
        return menu_juncoes()

    elif opcao == "2":
        Produto.listar_todos_com_fornecedores()
        print("Exibindo todos os produtos com seus fornecedores.")
        return menu_juncoes()

    elif opcao == "3":
        Funcionario.listar_todos()
        print("Exibindo todos os funcionários com seus nomes e cargos.")
        return menu_juncoes()

    elif opcao == "4":
        Cliente.listar_todos()
        print("Essa consulta está retornando todos os clientes. Para exibir foi usado função de junção e função aninhada.")
        print("para que serve? Exibir todos os clientes com seus endereços")
        return menu_juncoes()

    else:
        print("Opção inválida.")
        return menu_juncoes()


def menu_group_by_having():
    print("<========================================> Menu Group By e Having <========================================>")
    print("0 - Voltar")
    print("1 - Exibir produtos com os seus estoques")
    print("2 - Exibir todos os produtos com seus fornecedores")
    print("3 - Exibir todos os funcionarios com seus nomes e cargos")
    print("4 - exibir todas as entregas para um determinado cliente")
    opcao = input("Digite uma opção: ")
    if opcao == "0":
        return menu_trabalho()

def menu_funcoes_datas():
    print("<========================================> Menu Funções de Datas <========================================>")
    print("0 - Voltar")
    print("1 - Exibir produtos com os seus estoques")
    print("2 - Exibir todos os produtos com seus fornecedores")
    print("3 - Exibir todos os funcionarios com seus nomes e cargos")
    print("4 - exibir todas as entregas para um determinado cliente")
    opcao = input("Digite uma opção: ")
    if opcao == "0":
        return menu_trabalho()

def menu_consultas_aninhadas():
    print("<========================================> Menu Consultas Aninhadas <========================================>")
    print("0 - Voltar")
    print("1 - Exibir produtos com os seus estoques")
    print("2 - Exibir todos os produtos com seus fornecedores")
    print("3 - Exibir todos os funcionarios com seus nomes e cargos")
    print("4 - exibir todas as entregas para um determinado cliente")
    opcao = input("Digite uma opção: ")
    if opcao == "0":
        return menu_trabalho()

def menu_trabalho():
    print("<========================================> Menu Trabalho <========================================>")
    print("0 - Voltar ao menu principal")
    print("1 - consultas com junção")
    print("2 - consultas com group by e funções agregadas e/ou having")
    print("3 - consultas com funções de datas")
    print("4 - consultas aninhadas")

    opcao = input("Digite uma opção: ")

    if opcao == "0":
        return menu()

    elif opcao == "1":
        menu_juncoes()

    elif opcao == "2":
        menu_group_by_having()

    elif opcao == "3":
        menu_funcoes_datas()

    elif opcao == "4":
        menu_consultas_aninhadas()

    else:
        print("Opção inválida.")
        return menu_trabalho()

def menu():
    print("0 - Sair")
    print("1 - Ir para o menu de produtos")
    print("2 - Ir para o menu de fornecedores")
    print("9 - Pesquisas Importantes para o trabalho")
    op = input("Digite uma opção: ")
    if op == "0":
        return
    elif op == "1":
        menu_produtos()
    elif op == "9":
        menu_trabalho()
    else:
        print("Opção inválida, tente novamente.")
        menu()

if __name__ == '__main__':
    generate_data()
    menu_pessoas()
    close_connection()
