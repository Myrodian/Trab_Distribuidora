from fake_data import *
from Models import *
from tabulate import tabulate

def adicionar_pessoas():
    # Solicita os dados da pessoa
    nome = input("Digite o nome da pessoa (ou digite 0 para voltar ao menu): ").strip()
    if nome == "0":
        return menu_pessoas()
    
    email = input("Digite o email: ").strip()

    while True:
        cpf = input("Digite o CPF: ").strip()
        if len(cpf) == 11 and cpf.isdigit():
            break
        print("CPF deve conter exatamente 11 dígitos numéricos. Tente novamente.")

    while True:
        data_nascimento = input("Digite a data de nascimento (YYYY-MM-DD): ").strip()
        if len(data_nascimento) == 10:
            partes = data_nascimento.split('-')
            if len(partes) == 3 and all(p.isdigit() for p in partes):
                ano, mes, dia = partes
                if len(ano) == 4 and len(mes) == 2 and len(dia) == 2:
                    break
        print("Data de nascimento deve estar no formato YYYY-MM-DD. Tente novamente.")

    observacoes = input("Alguma observação? (opcional): ").strip()
    
    pessoa = Pessoa(
        nome=nome,
        email=email,
        cpf=cpf,
        data_nascimento=data_nascimento,
        observacoes=observacoes  # Adicionando observações como atributo opcional
    )
    sucesso, retorno = pessoa.salvar()
    print(retorno)
    if not sucesso:
        return adicionar_pessoas()
    return menu_pessoas()
  
def editar_pessoas():
    print("\n--- Lista de Pessoas Cadastradas ---")
    pessoas = Pessoa.listar_todas(imprimir=True)
    # Solicita o ID da pessoa a ser editada
    id_pessoa = input("Digite o ID da pessoa que deseja editar: ").strip()
    if not id_pessoa.isdigit():
        print("ID inválido. Operação cancelada.")
        return
    # Verifica se a pessoa existe no banco
    pessoa_existente = read_data("SELECT id FROM pessoa WHERE id = %s", (id_pessoa,))
    if not pessoa_existente:
        print(f"Pessoa com ID {id_pessoa} não encontrada.")
        return menu_pessoas()
    # Exibe os dados atuais da pessoa
    pessoa_dados = read_data("SELECT nome, email, cpf, data_nascimento, observacoes FROM pessoa WHERE id = %s", (id_pessoa,))[0]

    print("\nDados atuais da pessoa:")
    print(f"1. Nome: {pessoa_dados[0]}")
    print(f"2. Email: {pessoa_dados[1]}")
    print(f"3. CPF: {pessoa_dados[2]}")
    print(f"4. Data de Nascimento: {pessoa_dados[3]}")
    print(f"5. Observações: {pessoa_dados[4]}")

    # Solicita as novas informações
    nome = input("Novo nome ou pressione ENTER para manter: ").strip() or pessoa_dados[0]
    email = input("Novo E-mail ou pressione ENTER para manter: ").strip() or pessoa_dados[1]
    while True:
        cpf_input = input("Novo CPF ou pressione ENTER para manter: ").strip()
        if not cpf_input:
            cpf = pessoa_dados[2]
            break
        if len(cpf_input) == 11 and cpf_input.isdigit():
            cpf = cpf_input
            break
        print("CPF deve conter exatamente 11 dígitos numéricos. Tente novamente.")

    while True:
        data_nascimento_input = input("Digite a nova data de nascimento (YYYY-MM-DD) ou pressione ENTER para manter: ").strip()
        if not data_nascimento_input:
            data_nascimento = pessoa_dados[3]
            break
        # Verifica se o formato está correto (YYYY-MM-DD)
        partes = data_nascimento_input.split('-')
        if len(partes) == 3 and all(p.isdigit() for p in partes):
            ano, mes, dia = partes
            if len(ano) == 4 and len(mes) == 2 and len(dia) == 2:
                data_nascimento = data_nascimento_input
                break
        print("Data de nascimento deve estar no formato YYYY-MM-DD. Tente novamente.")

    observacoes = input("Novas observações: ").strip() or pessoa_dados[4]
     # Atualiza os dados no banco de dados
    update_query = "UPDATE pessoa SET nome = %s, email = %s, cpf = %s, data_nascimento = %s, observacoes = %s WHERE id = %s"
    params = (nome, email, cpf, data_nascimento, observacoes, id_pessoa)
    rows_affected = write_data(update_query, params)

    if rows_affected > 0:
        print(f"Pessoa ID {id_pessoa} atualizada com sucesso!")

    elif rows_affected == 0:
        print("Nenhuma alteração foi feita nos dados da pessoa.")
        
    else:
        print(f"Falha ao atualizar a pessoa ID {id_pessoa}.")
    # Chama o menu, que deve listar pessoas atualizadas do banco
    return menu_pessoas()

def deletar_pessoas():
    try:
        pessoa_id = int(input("Digite o ID da pessoa que deseja deletar: "))
    except ValueError:
        print("ID inválido.")
        return menu_pessoas()

    pessoa = Pessoa()
    if not pessoa.carregar(pessoa_id):
        print(f"Pessoa com ID {pessoa_id} não encontrada.")
        return menu_pessoas()

    print(f"\nNome: {pessoa.nome}")
    print(f"Email: {pessoa.email}")
    print(f"CPF: {pessoa.cpf}")
    print(f"Data de nascimento: {pessoa.data_nascimento}")
    print(f"Observações: {pessoa.observacoes}")

    confirm = input(f"\nTem certeza que deseja deletar a pessoa '{pessoa.nome}'? (s/n): ").strip().lower()
    if confirm == 's':
        pessoa.deletar()
    else:
        print("Operação cancelada.")
    
    return menu_pessoas()

def menu_pessoas():
    Pessoa.listar_todas(imprimir=True)

    print("<========================================> Menu Pessoas <========================================>")
    print("0 - Voltar ao menu principal")
    print("1 - Adicionar pessoa")
    print("2 - Editar pessoa")
    print("3 - Deletar pessoa")

    opcao = input("Escolha uma opção: ")

    if opcao == "0":
        return menu()
    elif opcao == "1":
        return adicionar_pessoas()
    elif opcao == "2":
        return editar_pessoas()
    elif opcao == "3":
        return deletar_pessoas()
    else:
        print("Opção inválida.")
        return menu_pessoas()

def adicionar_telefone():
    print("\n--- Adicionar Telefone ---")
    # Lista pessoas existentes para escolher
    pessoas = Pessoa.listar_todas(imprimir=True)
    if not pessoas:
        print("Nenhuma pessoa cadastrada.")
        return
    try:
        pessoa_id = int(input("Digite o ID da pessoa para associar o telefone: ").strip())
    except ValueError:
        print("ID inválido.")
        return
    # Verifica se o ID informado existe
    if not any(p[0] == pessoa_id for p in pessoas):
        print("Pessoa com o ID informado não encontrada.")
        return
    # Tipo do telefone
    tipos_validos = ['residencial', 'comercial', 'celular']
    while True:
        tipo = input("Digite o tipo de telefone (residencial, comercial, celular): ").strip().lower()
        if tipo in tipos_validos:
            break
        print("Tipo inválido. Os tipos válidos são: residencial, comercial, celular.")
    # DDD
    while True:
        ddd = input("Digite o DDD (ex: 011): ").strip()
        if len(ddd) == 3 and ddd.isdigit():
            break
        print("DDD inválido. Deve conter 3 dígitos numéricos.")
    # Número
    while True:
        numero = input("Digite o número (ex: 912345678): ").strip()
        if numero.isdigit() and 8 <= len(numero) <= 9:
            break
        print("Número inválido. Deve conter de 8 a 9 dígitos numéricos.")

    telefone = Telefone(tipo=tipo, ddd=ddd, numero=numero, pessoa_id=pessoa_id)
    sucesso, retorno = telefone.salvar()
    print(retorno)

    if sucesso:
        Telefone.listar_por_pessoa(pessoa_id)
        return menu_telefones()

def editar_telefone():
    print("\n--- Lista de Telefones Cadastrados ---")
    telefones = Telefone.listar_todos(imprimir=True)
    if not telefones:
        print("Nenhum telefone cadastrado.")
        return menu_telefones()

    id_telefone = input("Digite o ID do telefone que deseja editar: ").strip()
    if not id_telefone.isdigit():
        print("ID inválido. Operação cancelada.")
        return menu_telefones()

    telefone_obj = Telefone()
    if not telefone_obj.carregar(int(id_telefone)):
        print("Telefone não encontrado.")
        return menu_telefones()

    print("\nDados atuais do telefone:")
    print(f"1. Tipo: {telefone_obj.tipo}")
    print(f"2. DDD: {telefone_obj.ddd}")
    print(f"3. Número: {telefone_obj.numero}")
    print(f"4. Pessoa ID: {telefone_obj.pessoa_id}")
    tipos_validos = ['residencial', 'comercial', 'celular']
    # Flag para controlar se houve alteração
    alterado = False
    # Editar tipo
    while True:
        tipo = input("Novo tipo (residencial, comercial, celular) ou ENTER para manter: ").strip().lower()
        if tipo == "":
            tipo = telefone_obj.tipo
            break
        if tipo in tipos_validos:
            alterado = alterado or (tipo != telefone_obj.tipo)
            break
        print(f"Tipo inválido. Os tipos válidos são: {', '.join(tipos_validos)}.")
    # Editar DDD
    while True:
        ddd = input("Novo DDD (3 dígitos) ou ENTER para manter: ").strip()
        if ddd == "":
            ddd = telefone_obj.ddd
            break
        if len(ddd) == 3 and ddd.isdigit():
            alterado = alterado or (ddd != telefone_obj.ddd)
            break
        print("DDD inválido. Deve conter 3 dígitos numéricos.")
    # Editar número
    while True:
        numero = input("Novo número (8 a 9 dígitos) ou ENTER para manter: ").strip()
        if numero == "":
            numero = telefone_obj.numero
            break
        if numero.isdigit() and 8 <= len(numero) <= 9:
            alterado = alterado or (numero != telefone_obj.numero)
            break
        print("Número inválido. Deve conter de 8 a 9 dígitos numéricos.")
    # Editar pessoa_id
    pessoas = Pessoa.listar_todas(imprimir=True)
    if not pessoas:
        print("Nenhuma pessoa cadastrada para associar ao telefone.")
        return
    while True:
        pessoa_id_input = input("Novo ID da pessoa para associar ou ENTER para manter: ").strip()
        if pessoa_id_input == "":
            pessoa_id = telefone_obj.pessoa_id
            break
        if pessoa_id_input.isdigit() and any(p[0] == int(pessoa_id_input) for p in pessoas):
            pessoa_id = int(pessoa_id_input)
            alterado = alterado or (pessoa_id != telefone_obj.pessoa_id)
            break
        print("ID de pessoa inválido ou não encontrado. Tente novamente.")
    if not alterado:
        print("Nenhuma alteração foi feita no telefone.")
        return menu_telefones()
    # Atualiza objeto telefone com novos valores
    telefone_obj.tipo = tipo
    telefone_obj.ddd = ddd
    telefone_obj.numero = numero
    telefone_obj.pessoa_id = pessoa_id

    sucesso, retorno = telefone_obj.salvar()
    print(retorno)
    return menu_telefones()

def deletar_telefone():

    print("\n--- Lista de Telefones Cadastrados ---")
    telefones = Telefone.listar_todos(imprimir=True)
    if not telefones:
        print("Nenhum telefone cadastrado.")
        return menu_telefones()
    try:
        telefone_id = int(input("Digite o ID do telefone que deseja deletar: ").strip())
    except ValueError:
        print("ID inválido.")
        return menu_telefones()

    telefone = Telefone()
    if not telefone.carregar(telefone_id):
        print(f"Telefone com ID {telefone_id} não encontrado.")
        return menu_telefones()

    print(f"\nTelefone: ({telefone.ddd}) {telefone.numero} - {telefone.tipo}")
    print(f"Associado à Pessoa ID: {telefone.pessoa_id}")
    confirm = input(f"\nTem certeza que deseja deletar este telefone? (s/n): ").strip().lower()
    if confirm == 's':
        telefone.deletar()
    else:
        print("Operação cancelada.")

    return menu_telefones()
    
def menu_telefones():
    print("<========================================> Menu Telefones <========================================>")
    print("0 - Voltar ao menu principal")
    print("1 - Adicionar telefone")
    print("2 - Editar telefone")
    print("3 - Deletar telefone")

    opcao = input("Escolha uma opção: ")

    if opcao == "0":
        return menu()
    elif opcao == "1":
        return adicionar_telefone()
    elif opcao == "2":
        return editar_telefone()
    elif opcao == "3":
        return deletar_telefone()
    else:
        print("Opção inválida.")
        return menu_telefones()

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

def adicionar_cargo():
    print("\n--- Lista Atual de Cargos ---")
    Cargo.listar_todos(imprimir=True)  # mostra tabela de cargos antes de inserir
    print("\n--- Adicionar Cargo ---")

    nome = input("Digite o nome do cargo ou ENTER para cancelar: ").strip()
    if not nome:
        print("Operação cancelada.")
        return menu_cargos()
    # Verifica se já existe um cargo com esse nome
    while True:
        cargos_existentes = Cargo.listar_todos()
        if any(c[1].lower() == nome.lower() for c in cargos_existentes):
            print("Já existe um cargo com esse nome. Digite outro nome ou pressione ENTER para cancelar.")
            nome = input("Digite o nome do cargo ou ENTER para cancelar: ").strip()
            if not nome:
                print("Operação cancelada.")
                return menu_cargos()
        else:
            break
    while True:
        salario_input = input("Digite o salário para o cargo (somente números, ex: 3500.00): ").strip().replace(",", ".")
        try:
            salario_valor = float(salario_input)
            if salario_valor < 0:
                print("Salário não pode ser negativo.")
                continue
            break
        except ValueError:
            print("Valor inválido. Digite apenas números (use ponto ou vírgula para casas decimais).")
    # Prefixa aqui com "R$ " e formata para duas casas decimais
    salario_categoria = f"R$ {salario_valor:.2f}"
    while True:
        try:
            nivel_hierarquia = int(input("Digite o nível hierárquico (ex: 1 = base): ").strip())
            if nivel_hierarquia >= 0:
                break
            print("Nível deve ser um número inteiro positivo.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

    observacoes = input("Alguma observação? (opcional): ").strip()

    cargo = Cargo(nome=nome, salario_categoria=salario_categoria, nivel_hierarquia=nivel_hierarquia, observacoes=observacoes)
    sucesso, msg = cargo.salvar()
    print(msg)
    return menu_cargos()

def editar_cargo():
    print("\n--- Cargos Cadastrados ---")
    cargos = Cargo.listar_todos(imprimir=True)
    if not cargos:
        print("Nenhum cargo encontrado.")
        return menu_cargos()
    try:
        id_editar = int(input("Digite o ID do cargo que deseja editar: ").strip())
    except ValueError:
        print("ID inválido.")
        return menu_cargos()
    cargo_existente = next((c for c in cargos if c[0] == id_editar), None)
    if not cargo_existente:
        print("Cargo com ID informado não encontrado.")
        return menu_cargos()

    print("\nPressione ENTER para manter o valor atual.")
    # Verifica nome duplicado
    while True:
        nome = input(f"Novo nome do cargo [Atual: {cargo_existente[1]}]: ").strip()
        if not nome:
            nome = cargo_existente[1]
            break
        elif any(c[1].lower() == nome.lower() and c[0] != id_editar for c in cargos):
            print("Já existe um cargo com esse nome. Digite outro nome ou pressione ENTER para manter o atual.")
        else:
            break

    salario_categoria = input(f"Novo salário (formato: R$ XXXX.XX) [Atual: {cargo_existente[2]}]: ").strip() or cargo_existente[2]
    while True:
        nivel_input = input(f"Nível hierárquico (número inteiro) [Atual: {cargo_existente[3]}]: ").strip()
        if not nivel_input:
            nivel_hierarquia = cargo_existente[3]
            break
        try:
            nivel_hierarquia = int(nivel_input)
            break
        except ValueError:
            print("Entrada inválida. Digite um número inteiro para o nível.")

    observacoes = input(f"Observações [Atual: {cargo_existente[4] or 'Nenhuma'}]: ").strip() or cargo_existente[4]
    # Verifica se algo foi alterado
    if (nome == cargo_existente[1] and
        salario_categoria == cargo_existente[2] and
        nivel_hierarquia == cargo_existente[3] and
        observacoes == cargo_existente[4]):
        print("Nenhuma alteração foi feita.")
        return menu_cargos()

    cargo = Cargo(
        id=id_editar,
        nome=nome,
        salario_categoria=salario_categoria,
        nivel_hierarquia=nivel_hierarquia,
        observacoes=observacoes
    )
    sucesso, msg = cargo.salvar()
    print(msg)
    return menu_cargos()

def deletar_cargo():
    cargo = Cargo.listar_todos()
    if not cargo:
        print("Nenhum cargo encontrado.")
        return

    Cargo.listar_todos(imprimir=True)  # Mostra os cargos na tela

    try:
        id_deletar = int(input("Digite o ID do cargo que deseja deletar: ").strip())
    except ValueError:
        print("ID inválido.")
        return menu_cargos()

    cargo_existente = next((c for c in cargo if c[0] == id_deletar), None)
    if not cargo_existente:
        print("Cargo não encontrado.")
        return menu_cargos()

    confirmacao = input(f"Tem certeza que deseja deletar o cargo '{cargo_existente[1]}'? (s/n): ").strip().lower()
    if confirmacao != 's':
        print("Operação cancelada.")
        return menu_cargos()

    linhas_afetadas = write_data("DELETE FROM cargo WHERE id = %s", (id_deletar,))
    if linhas_afetadas > 0:
        print(f"Cargo ID {id_deletar} deletado com sucesso.")
    else:
        print("Falha ao deletar o cargo.")

    return menu_cargos()

def menu_cargos():
    print("<========================================> Menu Cargos <========================================>")
    print("0 - Voltar ao menu principal")
    print("1 - Adicionar cargo")
    print("2 - Editar cargo")
    print("3 - Excluir cargo")

    opcao = input("Digite uma opção: ")

    if opcao == "0":
        return menu()

    elif opcao == "1":
        return adicionar_cargo()

    elif opcao == "2":
        return editar_cargo()

    elif opcao == "3":
        return deletar_cargo()

    else:
        print("Opção inválida.")
        return menu_cargos()
    
def inserir_funcionario():
    print("\n--- Inserir Novo Funcionário ---")

    # Mostra lista de pessoas cadastradas
    print("\n--- Pessoas Cadastradas ---")
    pessoas = Pessoa.listar_todas(imprimir=True)
    try:
        pessoa_id = int(input("Digite o ID da pessoa que será o funcionário: ").strip())
    except ValueError:
        print("ID inválido.")
        return
    # Verifica se a pessoa existe
    if not any(p.id == pessoa_id for p in pessoas):
        print("Pessoa com ID informado não encontrada.")
        return
    # 🔒 Verifica se a pessoa já está empregada (sem data de demissão)
    vinculo_ativo = read_data(
        "SELECT id FROM funcionario WHERE Pessoa_id = %s AND data_demissao IS NULL",
        (pessoa_id,)
    )
    if vinculo_ativo:
        print("Esta pessoa já está vinculada à empresa como funcionário ativo.")
        print("Não é possível cadastrar novamente sem registrar uma data de demissão.")
        return menu_funcionario()
    # Mostra lista de cargos
    print("\n--- Cargos Cadastrados ---")
    cargos = Cargo.listar_todos(imprimir=True)
    try:
        cargo_id = int(input("Digite o ID do cargo: ").strip())
    except ValueError:
        print("ID inválido.")
        return

    if not any(c[0] == cargo_id for c in cargos):
        print("Cargo com ID informado não encontrado.")
        return menu_funcionario()
    # Data de admissão
    while True:
        data_admissao = input("Digite a data de admissão (YYYY-MM-DD): ").strip()
        if not data_admissao:
            print("Data obrigatória.")
            continue
        partes = data_admissao.split("-")
        if len(partes) == 3 and all(p.isdigit() for p in partes) and len(partes[0]) == 4:
            break
        print("Formato inválido. Use YYYY-MM-DD.")
    # Matrícula com prefixo "MAT"
    while True:
        matricula = input("Digite a matrícula iniciando com 'MAT' (máx. 20 caracteres): ").strip()
        
        if not matricula:
            print("Matrícula obrigatória.")
            continue
        if not matricula.upper().startswith("MAT"):
            print("A matrícula deve começar com 'MAT'.")
            continue
        if len(matricula) > 20:
            print("Matrícula muito longa.")
            continue
        # Verifica se já existe essa matrícula no banco (ativa ou não)
        duplicada = read_data("SELECT id FROM funcionario WHERE matricula = %s", (matricula,))
        if duplicada:
            print("Esta matrícula já está registrada no sistema. Digite uma matrícula diferente.")
            continue
        break  # Matrícula válida e única
    # Data de demissão (opcional)
    while True:
        data_demissao = input("Digite a data de demissão (YYYY-MM-DD) ou pressione ENTER para deixar em aberto: ").strip()
        if not data_demissao:
            data_demissao = None
            break
        partes = data_demissao.split("-")
        if len(partes) == 3 and all(p.isdigit() for p in partes) and len(partes[0]) == 4:
            break
        print("Formato inválido. Use YYYY-MM-DD.")
    # Observações (opcional)
    observacoes = input("Digite observações (opcional): ").strip() or None
    # Criação do objeto e salvamento
    funcionario = Funcionario(
        data_admissao=data_admissao,
        matricula=matricula,
        data_demissao=data_demissao,
        pessoa_id=pessoa_id,
        cargo_id=cargo_id,
        observacoes=observacoes
    )

    funcionario.salvar()
    return menu_funcionario()

def editar_funcionario():
    print("\n--- Funcionários Cadastrados ---")
    funcionarios = Funcionario.listar_todos(imprimir=True)
    
    try:
        id_editar = int(input("Digite o ID do funcionário que deseja editar: ").strip())
    except ValueError:
        print("ID inválido.")
        return

    funcionario = Funcionario()
    if not funcionario.carregar(id_editar):
        return menu_funcionario()
    
    print("\nPressione ENTER para manter o valor atual.")

    # Data de admissão
    while True:
        nova_data = input(f"Data de admissão [Atual: {funcionario.data_admissao}]: ").strip()
        if not nova_data:
            break
        partes = nova_data.split("-")
        if len(partes) == 3 and all(p.isdigit() for p in partes) and len(partes[0]) == 4:
            funcionario.data_admissao = nova_data
            break
        print("Formato inválido. Use YYYY-MM-DD.")

    # Matrícula
    while True:
        nova_matricula = input(f"Matrícula [Atual: {funcionario.matricula}]: ").strip()
        if not nova_matricula:
            break  # manter atual
        if not nova_matricula.upper().startswith("MAT"):
            print("A matrícula deve começar com 'MAT'.")
            continue
        if len(nova_matricula) > 20:
            print("Matrícula muito longa.")
            continue
        # Verifica se outra pessoa já usa essa matrícula
        duplicada = read_data(
            "SELECT id FROM funcionario WHERE matricula = %s AND id != %s",
            (nova_matricula, funcionario.id)
        )
        if duplicada:
            print("Matrícula já está em uso por outro funcionário.")
            continue
        funcionario.matricula = nova_matricula
        break
    # Data de demissão
    while True:
        nova_demissao = input(f"Data de demissão [Atual: {funcionario.data_demissao or '---'}] ou ENTER para manter: ").strip()
        if not nova_demissao:
            break
        partes = nova_demissao.split("-")
        if len(partes) == 3 and all(p.isdigit() for p in partes) and len(partes[0]) == 4:
            funcionario.data_demissao = nova_demissao
            break
        print("Formato inválido. Use YYYY-MM-DD.")
    # Observações
    nova_obs = input(f"Observações [Atual: {funcionario.observacoes or 'Nenhuma'}]: ").strip()
    if nova_obs:
        funcionario.observacoes = nova_obs

    funcionario.salvar()
    return menu_funcionario()

def deletar_funcionario():
    print("\n--- Funcionários Ativos ---")
    funcionarios = Funcionario.listar_todos(imprimir=True)
    if not funcionarios:
        print("Nenhum funcionário ativo encontrado.")
        return

    try:
        id_escolhido = int(input("Digite o ID do funcionário que deseja desligar: ").strip())
    except ValueError:
        print("ID inválido.")
        return

    query = """
        SELECT f.id, f.data_admissao, f.matricula, f.data_demissao,
               p.nome, p.email, p.cpf,
               c.nome AS nome_cargo, c.salario_categoria,
               f.observacoes
        FROM funcionario f
        INNER JOIN pessoa p ON f.Pessoa_id = p.id
        INNER JOIN cargo c ON f.Cargo_id = c.id
        WHERE f.id = %s
    """
    result = read_data(query, (id_escolhido,))
    if not result:
        print("Funcionário não encontrado.")
        return

    row = result[0]
    if row[3] is not None:
        print(f"\nFuncionário já desligado em {row[3]}.")
        return

    print("\n--- Confirmação de Desligamento ---")
    print(f"ID: {row[0]}")
    print(f"Nome: {row[4]}")
    print(f"Email: {row[5]}")
    print(f"CPF: {row[6]}")
    print(f"Matrícula: {row[2]}")
    print(f"Admissão: {row[1]}")
    print(f"Cargo: {row[7]}")
    print(f"Salário: R$ {row[8]}")
    print(f"Observações: {row[9] or 'Nenhuma'}")

    confirmar = input("\nDeseja realmente desligar este funcionário? (s/n): ").strip().lower()
    if confirmar != 's':
        print("Operação cancelada.")
        return menu_funcionario()
    data_hoje = datetime.now().strftime('%Y-%m-%d')
    sucesso = execute_command("UPDATE funcionario SET data_demissao = %s WHERE id = %s", (data_hoje, id_escolhido))
    if sucesso:
        print(f"Funcionário desligado com sucesso em {data_hoje}.")
    else:
        print("Erro ao desligar o funcionário.")

def menu_funcionario():
    Funcionario.listar_todos(imprimir=True)

    print("<========================================> Menu Funcionário <========================================>")
    print("0 - Voltar ao menu principal")
    print("1 - Adicionar funcionário")
    print("2 - Editar funcionário")
    print("3 - Excluir funcionário")

    opcao = input("Digite uma opção: ")

    if opcao == "0":
        return menu()

    elif opcao == "1":
        return inserir_funcionario()

    elif opcao == "2":
        return editar_funcionario()

    elif opcao == "3":
        return deletar_funcionario()

    else:
        print("Opção inválida.")
        return menu_funcionario()

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
    print("2 - Ir para o menu de pessoas")
    print("3 - Ir para o menu de telefones")
    print("4 - Ir para o menu de cargos")
    print("5 - Ir para o menu de funcionários")
    print("9 - Pesquisas Importantes para o trabalho")
    op = input("Digite uma opção: ")
    if op == "0":
        return
    elif op == "1":
        menu_produtos()
    elif op == "2":
        menu_pessoas()
    elif op == "3":
        menu_telefones()
    elif op == "4":
        menu_cargos()
    elif op == "5":
        menu_funcionario()
    elif op == "9":
        menu_trabalho()
    else:
        print("Opção inválida, tente novamente.")
        menu()

if __name__ == '__main__':
    generate_data()
    menu_funcionario()
    close_connection()
