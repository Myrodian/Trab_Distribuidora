from mysql_codes import *
from datetime import datetime

class Pessoa:
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


class Cargo:
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


class Telefone:
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