from mysql_codes import *
from datetime import datetime

class Pessoa:
    def __str__(self):
        return self.nome

    def __init__(self, id=None, nome=None, email=None, cpf=None, data_nascimento=None):
        self.id = id
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.data_nascimento = data_nascimento

    def carregar(self, id):
        result = read_data("SELECT id, nome, email, cpf, data_nascimento FROM pessoa WHERE id = %s", (id,))
        if result:
            self.id, self.nome, self.email, self.cpf, self.data_nascimento = result[0]
            print(f"Pessoa ID {self.id} carregada!")
            return True
        else:
            print("Pessoa não encontrada.")
            return False

    def salvar(self):
        if self.id:
            query = """UPDATE pessoa SET nome=%s, email=%s, cpf=%s, data_nascimento=%s WHERE id=%s"""
            execute_command(query, (self.nome, self.email, self.cpf, self.data_nascimento, self.id))
            print("Pessoa atualizada com sucesso!")
        else:
            query = """INSERT INTO pessoa (nome, email, cpf, data_nascimento) VALUES (%s, %s, %s, %s)"""
            execute_command(query, (self.nome, self.email, self.cpf, self.data_nascimento))
            result = read_data("SELECT LAST_INSERT_ID()")
            self.id = result[0][0]
            print(f"Pessoa inserida com sucesso! Novo ID: {self.id}")

    def deletar(self):
        if not self.id:
            print("Pessoa não carregada no objeto. Não pode deletar.")
            return
        execute_command("DELETE FROM pessoa WHERE id = %s", (self.id,))
        print("Pessoa deletada!")
        self.id = None

    # MÉTODOS DE ASSOCIAÇÃO
    def associar_fornecedor(self, fornecedor):
        if not self.id or not fornecedor.id:
            print("IDs inválidos. Carregue os objetos primeiro.")
            return

        result = read_data(
            "SELECT 1 FROM PessoaFornecedor WHERE Pessoa_id = %s AND Fornecedor_id = %s",
            (self.id, fornecedor.id)
        )
        if result:
            print(f"Já existe associação entre Pessoa {self.id} e Fornecedor {fornecedor.id}.")
            return

        query = "INSERT INTO PessoaFornecedor (Pessoa_id, Fornecedor_id) VALUES (%s, %s)"
        execute_command(query, (self.id, fornecedor.id))
        print(f"Pessoa {self.id} associada ao Fornecedor {fornecedor.id} com sucesso!")

    def listar_fornecedores(self):
        if not self.id:
            print("Pessoa não carregada.")
            return []

        result = read_data("""
            SELECT f.id, f.cnpj, f.nome_fantasia, f.email_contato 
            FROM fornecedor f
            JOIN PessoaFornecedor pf ON f.id = pf.Fornecedor_id
            WHERE pf.Pessoa_id = %s
        """, (self.id,))

        fornecedores = [Fornecedor(*row) for row in result]
        return fornecedores

class Cargo:
    def __str__(self):
        return self.nome

    def __init__(self, id=None, nome=None, salario_categoria=None, descricao=None, nivel_hierarquia=None):
        self.id = id
        self.nome = nome
        self.salario_categoria = salario_categoria
        self.descricao = descricao
        self.nivel_hierarquia = nivel_hierarquia

    def carregar(self, id):
        result = read_data("SELECT id, nome, salario_categoria, descricao, nivel_hierarquia FROM cargo WHERE id = %s", (id,))
        if result:
            self.id, self.nome, self.salario_categoria, self.descricao, self.nivel_hierarquia = result[0]
            print(f"Cargo ID {self.id} carregado com sucesso!")
            return True
        else:
            print("Cargo não encontrado.")
            return False

    def salvar(self):
        if self.id:
            query = """UPDATE cargo SET nome=%s, salario_categoria=%s, descricao=%s, nivel_hierarquia=%s WHERE id=%s"""
            execute_command(query, (self.nome, self.salario_categoria, self.descricao, self.nivel_hierarquia, self.id))
            print("Cargo atualizado com sucesso!")
        else:
            query = """INSERT INTO cargo (nome, salario_categoria, descricao, nivel_hierarquia) VALUES (%s, %s, %s, %s)"""
            execute_command(query, (self.nome, self.salario_categoria, self.descricao, self.nivel_hierarquia))
            result = read_data("SELECT LAST_INSERT_ID()")
            self.id = result[0][0]
            print(f"Cargo inserido com sucesso! Novo ID: {self.id}")

    def deletar(self):
        if not self.id:
            print("Cargo não carregado. Não é possível deletar.")
            return
        execute_command("DELETE FROM cargo WHERE id = %s", (self.id,))
        print("Cargo deletado com sucesso!")
        self.id = None

class Fornecedor:
    def __str__(self):
        return self.nome_fantasia if self.nome_fantasia else self.cnpj

    def __init__(self, id=None, cnpj=None, nome_fantasia=None, email_contato=None):
        self.id = id
        self.cnpj = cnpj
        self.nome_fantasia = nome_fantasia
        self.email_contato = email_contato

    def carregar(self, id):
        result = read_data("SELECT id, cnpj, nome_fantasia, email_contato FROM fornecedor WHERE id = %s", (id,))
        if result:
            self.id, self.cnpj, self.nome_fantasia, self.email_contato = result[0]
            print(f"Fornecedor ID {self.id} carregado com sucesso!")
            return True
        else:
            print("Fornecedor não encontrado.")
            return False

    def salvar(self):
        if self.id:
            query = """UPDATE fornecedor SET cnpj=%s, nome_fantasia=%s, email_contato=%s WHERE id=%s"""
            execute_command(query, (self.cnpj, self.nome_fantasia, self.email_contato, self.id))
            print("Fornecedor atualizado com sucesso!")
        else:
            query = """INSERT INTO fornecedor (cnpj, nome_fantasia, email_contato) VALUES (%s, %s, %s)"""
            execute_command(query, (self.cnpj, self.nome_fantasia, self.email_contato))
            result = read_data("SELECT LAST_INSERT_ID()")
            self.id = result[0][0]
            print(f"Fornecedor inserido com sucesso! Novo ID: {self.id}")

    def deletar(self):
        if not self.id:
            print("Fornecedor não carregado. Não é possível deletar.")
            return
        execute_command("DELETE FROM fornecedor WHERE id = %s", (self.id,))
        print("Fornecedor deletado com sucesso!")
        self.id = None

    # MÉTODOS DE ASSOCIAÇÃO
    def associar_pessoa(self, pessoa):
        if not self.id or not pessoa.id:
            print("IDs inválidos. Carregue os objetos primeiro.")
            return

        result = read_data(
            "SELECT 1 FROM PessoaFornecedor WHERE Pessoa_id = %s AND Fornecedor_id = %s",
            (pessoa.id, self.id)
        )
        if result:
            print(f"Já existe associação entre Fornecedor {self.id} e Pessoa {pessoa.id}.")
            return

        query = "INSERT INTO PessoaFornecedor (Pessoa_id, Fornecedor_id) VALUES (%s, %s)"
        execute_command(query, (pessoa.id, self.id))
        print(f"Fornecedor {self.id} associado à Pessoa {pessoa.id} com sucesso!")

    def listar_pessoas(self):
        if not self.id:
            print("Fornecedor não carregado.")
            return []

        result = read_data("""
            SELECT p.id, p.nome, p.email, p.cpf, p.data_nascimento 
            FROM pessoa p
            JOIN PessoaFornecedor pf ON p.id = pf.Pessoa_id
            WHERE pf.Fornecedor_id = %s
        """, (self.id,))

        pessoas = [Pessoa(*row) for row in result]
        return pessoas

class Telefone:
    def __str__(self):
        return self.numero

    def __init__(self, id=None, tipo=None, ddd=None, numero=None, pessoa_id=None):
        self.id = id
        self.tipo = tipo
        self.ddd = ddd
        self.numero = numero
        self.pessoa_id = pessoa_id

    def carregar(self, id):
        result = read_data("SELECT id, tipo, ddd, numero, Pessoa_id FROM telefone WHERE id = %s", (id,))
        if result:
            self.id, self.tipo, self.ddd, self.numero, self.pessoa_id = result[0]
            print(f"Telefone ID {self.id} carregado com sucesso!")
            return True
        else:
            print("Telefone não encontrado.")
            return False

    def salvar(self):
        if self.id:
            query = """UPDATE telefone SET tipo=%s, ddd=%s, numero=%s WHERE id=%s"""
            execute_command(query, (self.tipo, self.ddd, self.numero, self.id))
            print("Telefone atualizado com sucesso!")
        else:
            query = """INSERT INTO telefone (tipo, ddd, numero, Pessoa_id) VALUES (%s, %s, %s, %s)"""
            execute_command(query, (self.tipo, self.ddd, self.numero, self.pessoa_id))
            result = read_data("SELECT LAST_INSERT_ID()")
            self.id = result[0][0]
            print(f"Telefone inserido com sucesso! Novo ID: {self.id}")

    def deletar(self):
        if not self.id:
            print("Telefone não carregado. Não é possível deletar.")
            return
        execute_command("DELETE FROM telefone WHERE id = %s", (self.id,))
        print("Telefone deletado com sucesso!")
        self.id = None

class Funcionario:
    def __str__(self):
        pessoa = Pessoa()
        if self.pessoa_id:
            pessoa.carregar(self.pessoa_id)
            nome = pessoa.nome
        else:
            nome = "Desconhecido"
        return nome

    def __init__(self, id=None, data_admissao=None, matricula=None, data_demissao=None, pessoa_id=None, cargo_id=None):
        self.id = id
        self.data_admissao = data_admissao
        self.matricula = matricula
        self.data_demissao = data_demissao
        self.pessoa_id = pessoa_id
        self.cargo_id = cargo_id

    def carregar(self, id):
        result = read_data("SELECT id, data_admissao, matricula, data_demissao, Pessoa_id, Cargo_id FROM funcionario WHERE id = %s", (id,))
        if result:
            self.id, self.data_admissao, self.matricula, self.data_demissao, self.pessoa_id, self.cargo_id = result[0]
            print(f"Funcionário ID {self.id} carregado com sucesso!")
            return True
        else:
            print("Funcionário não encontrado.")
            return False

    def salvar(self):
        if self.id:
            query = """UPDATE funcionario SET data_admissao=%s, matricula=%s, data_demissao=%s WHERE id=%s"""
            execute_command(query, (self.data_admissao, self.matricula, self.data_demissao, self.id))
            print("Funcionário atualizado com sucesso!")
        else:
            query = """INSERT INTO funcionario (data_admissao, matricula, data_demissao, Pessoa_id, Cargo_id) VALUES (%s, %s, %s, %s)"""
            execute_command(query, (self.data_admissao, self.matricula, self.data_demissao, self.pessoa_id, self.cargo_id))
            result = read_data("SELECT LAST_INSERT_ID()")
            self.id = result[0][0]
            print(f"Funcionário inserido com sucesso! Novo ID: {self.id}")

    def deletar(self):
        if not self.id:
            print("Funcionário não carregado. Não é possível deletar.")
            return
        self.data_demissao = datetime.now().strftime('%Y-%m-%d')
        execute_command("UPDATE funcionario SET data_demissao = %s WHERE id = %s", (self.data_demissao, self.id))
        print(f"Funcionário marcado como desligado em {self.data_demissao}.")

class Produto:
    def __str__(self):
        return self.nome

    def __init__(self, id=None, nome=None, descricao=None, preco=None, fornecedor_id=None):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.fornecedor_id = fornecedor_id

    def carregar(self, id):
        result = read_data("SELECT id, nome, descricao, preco, Fornecedor_id FROM produto WHERE id = %s", (id,))
        if result:
            self.id, self.nome, self.descricao, self.preco, self.fornecedor_id = result[0]
            print(f"Produto ID {self.id} carregado com sucesso!")
            return True
        else:
            print("Produto não encontrado.")
            return False

    def salvar(self):
        if self.id:
            query = """UPDATE produto SET nome=%s, descricao=%s, preco=%s WHERE id=%s"""
            execute_command(query, (self.nome, self.descricao, self.preco, self.id))
            print("Produto atualizado com sucesso!")
        else:
            query = """INSERT INTO produto (nome, descricao, preco, Fornecedor_id) VALUES (%s, %s, %s, %s)"""
            execute_command(query, (self.nome, self.descricao, self.preco, self.fornecedor_id))
            result = read_data("SELECT LAST_INSERT_ID()")
            self.id = result[0][0]
            print(f"Produto inserido com sucesso! Novo ID: {self.id}")

    def deletar(self):
        if not self.id:
            print("Produto não carregado. Não é possível deletar.")
            return
        execute_command("DELETE FROM produto WHERE id = %s", (self.id,))
        print("Produto deletado com sucesso!")
        self.id = None

class Entrega:
    def __str__(self):
        return f"Entrega ID: {self.id}, Data: {self.data_entrega}"

    def __init__(self, id=None, data_entrega=None, produto_id=None, quantidade=None):
        self.id = id
        self.data_entrega = data_entrega
        self.produto_id = produto_id
        self.quantidade = quantidade

    def carregar(self, id):
        result = read_data("SELECT id, data_entrega, Produto_id, quantidade FROM entrega WHERE id = %s", (id,))
        if result:
            self.id, self.data_entrega, self.produto_id, self.quantidade = result[0]
            print(f"Entrega ID {self.id} carregada com sucesso!")
            return True
        else:
            print("Entrega não encontrada.")
            return False

    def salvar(self):
        if self.id:
            query = """UPDATE entrega SET data_entrega=%s, Produto_id=%s, quantidade=%s WHERE id=%s"""
            execute_command(query, (self.data_entrega, self.produto_id, self.quantidade, self.id))
            print("Entrega atualizada com sucesso!")
        else:
            query = """INSERT INTO entrega (data_entrega, Produto_id, quantidade) VALUES (%s, %s, %s)"""
            execute_command(query, (self.data_entrega, self.produto_id, self.quantidade))
            result = read_data("SELECT LAST_INSERT_ID()")
            self.id = result[0][0]
            print(f"Entrega inserida com sucesso! Novo ID: {self.id}")

    def deletar(self):
        if not self.id:
            print("Entrega não carregada. Não é possível deletar.")
            return
        execute_command("DELETE FROM entrega WHERE id = %s", (self.id,))
        print("Entrega deletada com sucesso!")
        self.id = None

class Cliente:
    def __str__(self):
        return self.nome

    def __init__(self, id=None, nome=None, email=None, telefone=None):
        self.id = id
        self.nome = nome
        self.email = email
        self.telefone = telefone

    def carregar(self, id):
        result = read_data("SELECT id, nome, email, telefone FROM cliente WHERE id = %s", (id,))
        if result:
            self.id, self.nome, self.email, self.telefone = result[0]
            print(f"Cliente ID {self.id} carregado com sucesso!")
            return True
        else:
            print("Cliente não encontrado.")
            return False

    def salvar(self):
        if self.id:
            query = """UPDATE cliente SET nome=%s, email=%s, telefone=%s WHERE id=%s"""
            execute_command(query, (self.nome, self.email, self.telefone, self.id))
            print("Cliente atualizado com sucesso!")
        else:
            query = """INSERT INTO cliente (nome, email, telefone) VALUES (%s, %s, %s)"""
            execute_command(query, (self.nome, self.email, self.telefone))
            result = read_data("SELECT LAST_INSERT_ID()")
            self.id = result[0][0]
            print(f"Cliente inserido com sucesso! Novo ID: {self.id}")

    def deletar(self):
        if not self.id:
            print("Cliente não carregado. Não é possível deletar.")
            return
        execute_command("DELETE FROM cliente WHERE id = %s", (self.id,))
        print("Cliente deletado com sucesso!")
        self.id = None
