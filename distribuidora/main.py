from mysql_codes import *
from fake_data import *

def menu():
    # """Display the main menu."""
    print("Menu:")
    print("1. Generate Data")
    print("2. Execute Command")
    print("3. Read Data")
    print("4. Exit")

## Create // Update // Delete (Pessoa)

## CREATE PESSOA
def insert_pessoa():
    # Insert a new person into the database.
    nome = str(input("Enter name: "))
    email = str(input("Enter email: "))
    cpf = int(input("Enter cpf: "))
    data_nascimento = input("Enter data nascimento: ")
    #Check if it already exists by CPF
    check_query = f'SELECT id FROM pessoa WHERE cpf = "`{cpf}"'
    result = read_data(check_query)

    if result:
        print("Pessoa já cadastrada no sistema com esse CPF. ID:", result[0][0])
        return result[0][0]
    # If it does not exist, insert the person
    command = f'''
        INSERT INTO pessoa (nome, email, cpf, data_nascimento)
        VALUES ("{nome}", "{email}", "{cpf}", "{data_nascimento}")
    '''
    execute_command(command)
    ## Retrieve the new person's ID
    pessoa_id = read_data(f'SELECT id FROM pessoa WHERE nome = "{nome}"')[0][0]
    print("Pessoa inserted successfully.", pessoa_id)
    return pessoa_id

## UPDATE PESSOA
def update_pessoa(pessoa_id):
    # Fetch the person's current data from the database
    query = f'''SELECT nome, email, cpf, data_nascimento FROM pessoa WHERE id = {pessoa_id}'''
    result = read_data(query)
    # Check if the person was found
    if not result:
        print(f"Nenhuma pessoa encontrada com o ID {pessoa_id}.")
        return
    # Unpack existing data
    nome_atual, email_atual, cpf_atual, data_nasc_atual = result[0]

    # Show current data to user
    print("\n--- Dados atuais da pessoa ---")
    print(f"Nome: {nome_atual}")
    print(f"Email: {email_atual}")
    print(f"CPF: {cpf_atual}")
    print(f"Data de Nascimento: {data_nasc_atual}")
    print("----------------------------------")
    # Request new data (or keep current data if user presses Enter)
    nome = input(f"Digite o novo nome (ou Enter para manter '{nome_atual}'): ") or nome_atual
    email = input(f"Digite o novo email (ou Enter para manter '{email_atual}'): ") or email_atual
    
    try:
        cpf_input = input(f"Digite o novo CPF (ou Enter para manter '{cpf_atual}'): ")
        cpf = int(cpf_input) if cpf_input else cpf_atual
    except ValueError:
        print("CPF inválido. Atualização cancelada.")
        return

    data_nasc = input(f"Digite a nova data de nascimento (ou Enter para manter '{data_nasc_atual}'): ") or data_nasc_atual
    # Assemble the update SQL command
    command = f'''
        UPDATE pessoa 
        SET nome = "{nome}", email = "{email}", cpf = {cpf}, data_nascimento = "{data_nasc}"
        WHERE id = {pessoa_id}
    '''
    execute_command(command)

    print("Pessoa atualizada com sucesso!")

## DELETE PESSOA
def delete_pessoa():
    nome_pessoa = input("Digite o nome da pessoa que deseja deletar: ").strip()
    # Search for people with similar name
    query = f'''SELECT id, nome, cpf FROM pessoa WHERE nome LIKE "%{nome_pessoa}%"'''
    result = read_data(query)

    if not result:
        print(f"Nenhuma pessoa encontrada com nome parecido com '{nome_pessoa}'.")
        return
    # If more than one person found, ask to choose
    if len(result) > 1:
        print("\nPessoas encontradas:")
        for idx, (pid, nome, cpf) in enumerate(result, 1):
            print(f"{idx}. ID: {pid}, Nome: {nome}, CPF: {cpf}")
        try:
            escolha = int(input("Digite o número da pessoa que deseja deletar: "))
            pessoa_id = result[escolha - 1][0]
            nome_escolhido = result[escolha - 1][1]
        except (ValueError, IndexError):
            print("Opção inválida!")
            return
    else:
        pessoa_id = result[0][0]
        nome_escolhido = result[0][1]
    # Confirmation before deleting
    confirmar = input(f"Tem certeza que deseja deletar a pessoa '{nome_escolhido}' (ID: {pessoa_id})? (s/n): ").lower()
    if confirmar != 's':
        print("Operação cancelada.")
        return
    # Deletion
    try:
        delete_command = f'DELETE FROM pessoa WHERE id = {pessoa_id}'
        execute_command(delete_command)
        print(f"Pessoa '{nome_escolhido}' (ID: {pessoa_id}) deletada com sucesso!")
    except Exception as e:
        print("Erro ao deletar a pessoa:", e)


## Create // Update // Delete (Funcionario)

## CREATE FUNCIONARIO
def insert_funcionario(cargo_id):
    pessoa_id = insert_pessoa()
    data_atual = "a"
    matricula = str(input("Enter matricula: "))
    # Insert funcionario
    command = f'INSERT INTO funcionario (data_admissao, matricula, Pessoa_id, Cargo_id) VALUES("{data_atual}", "{matricula}", {pessoa_id}, {cargo_id})'
    execute_command(command)
    # Check if was inserted successfully
    # Cria uma consulta para verificar se o funcionário foi inserido com sucesso
    # Procura pelo funcionário com a mesma matrícula, Pessoa_id e Cargo_id
    # Ordena pelo ID em ordem decrescente e pega apenas o mais recente (LIMIT 1)
    query = f'''SELECT id FROM funcionario WHERE matricula = "{matricula}" AND Pessoa_id = {pessoa_id} AND Cargo_id = {cargo_id}  ORDER BY id DESC LIMIT 1'''
    result = read_data(query)

    if result and len(result) > 0:
        funcionario_id = result[0][0]
        print(f"Funcionario inserido com sucesso!!! ID: {funcionario_id}")
        return funcionario_id
    else:
        print("Erro: Funcionário não foi inserido.")
        return None

## UPDATE FUNCIONARIO
def update_funcionario(funcionario_id):
    # Check if employee exists
    check_query = f'SELECT matricula, Cargo_id, data_admissao FROM funcionario WHERE id = {funcionario_id}'
    result = read_data(check_query)

    if not result:
        print(f"Nenhum funcionário encontrado com o ID {funcionario_id}.")
        return
    matricula_atual, cargo_id_atual, data_admissao_atual = result[0]

    print("\n--- Dados atuais do funcionário ---")
    print(f"Matrícula: {matricula_atual}")
    print(f"Cargo ID: {cargo_id_atual}")
    print(f"Data de admissão: {data_admissao_atual}")
    print("------------------------------------")
    # Request new data or keep current data
    nova_matricula = input(f"Digite a nova matrícula (ou Enter para manter '{matricula_atual}'): ") or matricula_atual
    novo_cargo_id = input(f"Digite o novo Cargo ID (ou Enter para manter '{cargo_id_atual}'): ") or cargo_id_atual
    nova_data = input(f"Digite a nova data de admissão (ou Enter para manter '{data_admissao_atual}'): ") or data_admissao_atual
    # Update SQL command
    command = f'''
    UPDATE funcionario SET matricula = "{nova_matricula}", Cargo_id = {novo_cargo_id}, data_admissao = "{nova_data}" WHERE id = {funcionario_id}'''
    execute_command(command)
    # Check if it has been updated
    verify_query = f'SELECT id FROM funcionario WHERE id = {funcionario_id}'
    verify_result = read_data(verify_query)

    if verify_result:
        print(f"Funcionário (ID: {funcionario_id}) atualizado com sucesso!")
    else:
        print("Erro ao atualizar o funcionário.")

## DELETE FUNCIONARIO
def delete_funcionario():
    nome_pessoa = input("Digite o nome da pessoa associada ao funcionário que deseja deletar: ").strip()
    # Search for employees linked to this name
    query = f'''SELECT f.id, f.matricula, p.nome FROM funcionario f JOIN pessoa p ON f.Pessoa_id = p.id WHERE p.nome LIKE "%{nome_pessoa}%"'''
    result = read_data(query)

    if not result:
        print(f"Nenhum funcionário encontrado com nome parecido com '{nome_pessoa}'.")
        return
    # If more than one result, ask to choose
    if len(result) > 1:
        print("\nFuncionários encontrados:")
        # Percorre a lista de resultados da consulta SQL, enumerando a partir de 1
        for idx, (fid, matricula, nome) in enumerate(result, 1):
            # Exibe o número do item (idx), ID, matrícula e nome do funcionário
            # Isso facilita a escolha do usuário se houver mais de um resultado
            print(f"{idx}. ID: {fid}, Matrícula: {matricula}, Nome: {nome}")
        try:
            escolha = int(input("Digite o número do funcionário que deseja deletar: "))
            funcionario_id = result[escolha - 1][0] # Get the ID of the chosen employee
            matricula = result[escolha - 1][1] # Get the corresponding license plate
        except (ValueError, IndexError):
            print("Opção inválida!")
            return
    else:
        # If only one employee was found, take the ID and registration number directly
        funcionario_id = result[0][0]
        matricula = result[0][1]
    # Confirmation
    confirmar = input(f"Tem certeza que deseja deletar o funcionário com matrícula '{matricula}'? (s/n): ").lower()
    if confirmar != 's':
        print("Operação cancelada.")
        return
    # Delete
    try:
        delete_command = f'DELETE FROM funcionario WHERE id = {funcionario_id}'
        execute_command(delete_command)
        print(f"Funcionário com matrícula '{matricula}' (ID: {funcionario_id}) deletado com sucesso!")
    except Exception as e:
        print("Erro ao deletar o funcionário:", e)

## Create // Update // Delete (Cargo)

## CREATE CARGO
def insert_cargo():
    nome = input("Digite o nome do cargo: ")
    salario_categoria = input("Digite o salário da categoria: ")
    descricao = input("Digite a descrição do cargo: ")
    nivel_hierarquia = input("Digite o nível de hierarquia (número inteiro): ")
    # Check if a position with the same name already exists
    check_query = f'SELECT id FROM cargo WHERE nome = "{nome}"'
    result = read_data(check_query)
    if result:
        print(f"Cargo já cadastrado no sistema. ID: {result[0][0]}")
        return result[0][0]
    # Insert into the database
    command = f'''INSERT INTO cargo (nome, salario_categoria, descricao, nivel_hierarquia)VALUES ("{nome}", "{salario_categoria}", "{descricao}", {nivel_hierarquia})'''
    execute_command(command)
    # Retrieves the ID of the newly created role
    query = f'SELECT id FROM cargo WHERE nome = "{nome}" ORDER BY id DESC LIMIT 1'
    result = read_data(query)

    if result and len(result) > 0:
        cargo_id = result[0][0]
        print(f"Cargo inserido com sucesso! ID: {cargo_id}")
        return cargo_id
    else:
        print("Erro: Cargo não foi inserido.")
        return None

## UPDATE CARGO
def update_cargo(cargo_id):
    # Check if the position exists
    check_query = f'SELECT nome, salario_categoria, descricao, nivel_hierarquia FROM cargo WHERE id = {cargo_id}'
    result = read_data(check_query)

    if not result:
        print(f"Nenhum cargo encontrado com o ID {cargo_id}.")
        return

    nome_atual, salario_atual, descricao_atual, nivel_atual = result[0]

    print("\n--- Dados atuais do cargo ---")
    print(f"Nome: {nome_atual}")
    print(f"Salário da categoria: {salario_atual}")
    print(f"Descrição: {descricao_atual}")
    print(f"Nível hierárquico: {nivel_atual}")
    print("------------------------------------")
    # Request new data or keep current data
    novo_nome = input(f"Digite o novo nome (ou Enter para manter '{nome_atual}'): ") or nome_atual
    novo_salario = input(f"Digite o novo salário da categoria (ou Enter para manter '{salario_atual}'): ") or salario_atual
    nova_descricao = input(f"Digite a nova descrição (ou Enter para manter '{descricao_atual}'): ") or descricao_atual
    novo_nivel = input(f"Digite o novo nível hierárquico (ou Enter para manter '{nivel_atual}'): ") or nivel_atual
    # Comando SQL de atualização
    command = f'''
    UPDATE cargo SET nome = "{novo_nome}", salario_categoria = "{novo_salario}", descricao = "{nova_descricao}", nivel_hierarquia = {novo_nivel}WHERE id = {cargo_id}'''

    execute_command(command)

    print(f"Cargo (ID: {cargo_id}) atualizado com sucesso!")

## DELETE CARGO
def delete_cargo():
    # Prompts the user for the name of the position they want to delete
    nome_cargo = input("Digite o nome do cargo que deseja deletar: ").strip()
    # Search the database for positions with similar names
    query = f'SELECT id, nome FROM cargo WHERE nome LIKE "%{nome_cargo}%"'
    result = read_data(query)
    # If no position is found, display a message and close the function
    if not result:
        print(f"Nenhum cargo encontrado com nome parecido com '{nome_cargo}'.")
        return
    # If more than one position is found, display them all for the user to choose from
    if len(result) > 1:
        print("\nCargos encontrados:")
        # Percorre os resultados da consulta SQL de cargos encontrados, começando em 1
        for idx, (cid, nome) in enumerate(result, 1):
            # Exibe o número (idx), o ID do cargo e o nome do cargo
            # Útil para o usuário escolher o cargo certo caso existam duplicidades
            print(f"{idx}. ID: {cid}, Nome: {nome}")
        try:
            # Ask the user to choose which position they want to delete
            escolha = int(input("Digite o número do cargo que deseja deletar: "))
            cargo_id = result[escolha - 1][0]  # Get the ID of the selected role
            nome = result[escolha - 1][1]      # Get the name of the selected position
        except (ValueError, IndexError):
            # If the input is invalid or out of the list
            print("Opção inválida!")
            return
    else:
        # If only one position was found
        cargo_id = result[0][0]
        nome = result[0][1]
    # Ask for confirmation before performing the delete
    confirmar = input(f"Tem certeza que deseja deletar o cargo '{nome}'? (s/n): ").lower()
    if confirmar != 's':
        print("Operação cancelada.")
        return
    # Try to execute the delete command on the database
    try:
        delete_command = f'DELETE FROM cargo WHERE id = {cargo_id}'
        execute_command(delete_command)
        print(f"Cargo '{nome}' (ID: {cargo_id}) deletado com sucesso!")
    except Exception as e:
        # Display error message if operation fails
        print("Erro ao deletar o cargo:", e)

## Create // Update // Delete (Telefone)

## CREATE TELEFONE
def insert_telefone(pessoa_id):
    tipo = input("Digite o tipo (ex: celular, fixo): ")
    ddd = input("Digite o DDD (ex: 21): ")
    numero = input("Digite o número (ex: 912345678)")

    command = f'''INSERT INTO telefone (tipo, ddd, numero, Pessoa_id) VALUES ("{tipo}, "{ddd}", "{numero}", {pessoa_id})'''
    execute_command(command)

    # Insert confirmation
    result = read_data('''SELECT id FROM telefone WHERE tipo = "{tipo}" AND ddd = "{ddd}" AND numero = "{numero}" AND Pessoa_id = {pesssoa_id} ORDER BY id DESC LIMIT 1''')

    if result:
        print(f"Telefone inserido com sucesso! ID: {result[0][0]}")
        return result[0][0]
    else:
        print("Erro ao inserir telefone.")
        return None

## UPDATE TELEFONE
def update_telefone(telefone_id):
    # Search current data
    query = f'SELECT tipo, ddd, numero FROM telefone WHERE id = {telefone_id}'
    result = read_data(query)

    if not result:
        print("Telefone não encontrado.")
        return

    tipo_atual, ddd_atual, numero_atual = result[0]

    print("\n--- Dados atuais ---")
    print(f"Tipo: {tipo_atual}, DDD: {ddd_atual}, Número: {numero_atual}")

    tipo = input(f"Novo tipo (ou Enter para manter '{tipo_atual}'): ") or tipo_atual
    ddd = input(f"Novo DDD (ou Enter para manter '{ddd_atual}'): ") or ddd_atual
    numero = input(f"Novo número (ou Enter para manter '{numero_atual}'): ") or numero_atual

    command = f'''UPDATE telefone SET tipo = "{tipo}", ddd = "{ddd}", numero = "{numero}" WHERE id = {telefone_id}'''
    execute_command(command)
    print("Telefone atualizado com sucesso!")

## DELETE TELEFONE
def delete_telefone():
    # Asks for the person's name
    nome_pessoa = input("Digite o nome da pessoa associada ao telefone: ").strip()
    # Check the phones linked to this person
    query = f'''SELECT t.id, t.tipo, t.ddd, t.numero, p.nome FROM telefone t JOIN pessoa p ON t.Pessoa_id = p.id WHERE p.nome LIKE "%{nome_pessoa}%"'''
    resultados = read_data(query)

    if not resultados:
        print(f"Nenhum telefone encontrado para pessoas com nome parecido com '{nome_pessoa}'.")
        return
    # Displays the phones found
    print("\nTelefones encontrados:")
    for (tid, tipo, ddd, numero, nome) in resultados:
        print(f"ID: {tid} | Tipo: {tipo} | DDD: {ddd} | Número: {numero} | Pessoa: {nome}")
    # Asks for the ID of the phone the user wants to delete
    try:
        telefone_id = int(input("\nDigite o ID do telefone que deseja deletar: "))
    except ValueError:
        print("ID inválido!")
        return
    # Checks if the given ID is in the results list
    telefone_info = next((t for t in resultados if t[0] == telefone_id), None)
    if not telefone_info:
        print(f"Nenhum telefone com ID {telefone_id} encontrado na lista.")
        return

    tipo, ddd, numero = telefone_info[1], telefone_info[2], telefone_info[3]
    # Confirmation
    confirmar = input(f"Tem certeza que deseja deletar o telefone ({tipo} - ({ddd}) {numero})? (s/n): ").lower()
    if confirmar != 's':
        print("Operação cancelada.")
        return
    # Perform the deletion
    try:
        execute_command(f'DELETE FROM telefone WHERE id = {telefone_id}')
        print(f"Telefone ({tipo} - ({ddd}) {numero}) deletado com sucesso!")
    except Exception as e:
        print("Erro ao deletar telefone:", e)

## Create // Update // Delete (Fornecedor)

## CREATE FORNECEDOR
def insert_fornecedor():
    cnpj = input("Digite o CNPJ do fornecedor: ")
    nome_fantasia = input("Digite o nome fantasia do fornecedor: ")
    email_contato = input("Digite o e-mail de contato do fornecedor: ")
    # Check if it already exists
    check_query = f'SELECT id FROM fornecedor WHERE cnpj = "{cnpj}"'
    result = read_data(check_query)

    if result:
        print(f"Fornecedor já cadastrado. ID: {result[0][0]}")
        return result[0][0]
    # Insert
    command = f'''INSERT INTO fornecedor (cnpj, nome_fantasia, email_contato) VALUES ("{cnpj}", "{nome_fantasia}", "{email_contato}")'''
    execute_command(command)
    # Retrieve ID
    query = f'SELECT id FROM fornecedor WHERE cnpj = "{cnpj}" ORDER BY id DESC LIMIT 1'
    result = read_data(query)

    if result:
        fornecedor_id = result[0][0]
        print(f"Fornecedor inserido com sucesso! ID: {fornecedor_id}")
        return fornecedor_id
    else:
        print("Erro ao inserir fornecedor.")
        return None

##UPDATE FORNECEDOR
def update_fornecedor(fornecedor_id):
    # Check if it exists
    query = f'''SELECT cnpj, nome_fantasia, email_contato FROM fornecedor WHERE id = {fornecedor_id}'''
    result = read_data(query)

    if not result:
        print("Fornecedor não encontrado.")
        return

    cnpj_atual, nome_atual, email_atual = result[0]

    print("\n--- Dados atuais ---")
    print(f"CNPJ: {cnpj_atual}")
    print(f"Nome Fantasia: {nome_atual}")
    print(f"E-mail de Contato: {email_atual}")

    cnpj = input(f"Novo CNPJ (ou Enter para manter '{cnpj_atual}'): ") or cnpj_atual
    nome = input(f"Novo nome fantasia (ou Enter para manter '{nome_atual}'): ") or nome_atual
    email = input(f"Novo e-mail de contato (ou Enter para manter '{email_atual}'): ") or email_atual

    command = f'''UPDATE fornecedor SET cnpj = "{cnpj}", nome_fantasia = "{nome}", email_contato = "{email}" WHERE id = {fornecedor_id}'''
    execute_command(command)
    print("Fornecedor atualizado com sucesso!")

##DELETE FORNECEDOR
def delete_fornecedor():
    nome_fantasia = input("Digite (parte do) nome fantasia do fornecedor: ").strip()
    # Search for all suppliers whose trade name contains the term entered
    query = f'''SELECT id, nome_fantasia FROM fornecedor WHERE nome_fantasia LIKE "%{nome_fantasia}%"'''
    resultados = read_data(query)

    if not resultados:
        print(f"Nenhum fornecedor encontrado com nome parecido com '{nome_fantasia}'.")
        return
    # Displays the suppliers found
    print("\nFornecedores encontrados:")
    for fid, nome in resultados:
        print(f"ID: {fid} | Nome Fantasia: {nome}")
    # Request the vendor ID to be deleted
    try:
        fornecedor_id = int(input("\nDigite o ID do fornecedor que deseja deletar: "))
    except ValueError:
        print("ID inválido!")
        return
    # Check if the given ID is in the list
    fornecedor_info = next((f for f in resultados if f[0] == fornecedor_id), None)
    if not fornecedor_info:
        print(f"Nenhum fornecedor com ID {fornecedor_id} encontrado.")
        return

    nome_confirmar = fornecedor_info[1]
    # Confirmation
    confirmar = input(f"Tem certeza que deseja deletar o fornecedor '{nome_confirmar}'? (s/n): ").lower()
    if confirmar != 's':
        print("Operação cancelada.")
        return
    # Perform the deletion
    try:
        execute_command(f'DELETE FROM fornecedor WHERE id = {fornecedor_id}')
        print(f"Fornecedor '{nome_confirmar}' (ID: {fornecedor_id}) deletado com sucesso!")
    except Exception as e:
        print("Erro ao deletar fornecedor:", e)

if __name__ == '__main__':
    generate_data()
    close_connection()
