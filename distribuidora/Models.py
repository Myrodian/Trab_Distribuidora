from mysql_codes import *
from datetime import datetime
from tabulate import tabulate

class Pessoa:
    def __str__(self):
        return self.nome

    def __init__(self, id=None, nome=None, email=None, cpf=None, data_nascimento=None, observacoes=None):
        self.id = id
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.observacoes = observacoes

    def carregar(self, id):
        result = read_data("SELECT id, nome, email, cpf, data_nascimento, observacoes FROM pessoa WHERE id = %s", (id,))
        if result:
            self.id, self.nome, self.email, self.cpf, self.data_nascimento, self.observacoes = result[0]
            print(f"Pessoa ID {self.id} carregada!")
            return True
        else:
            print("Pessoa não encontrada.")
            return False

    def salvar(self):
        try:
            if self.id:
                query = """UPDATE pessoa SET nome=%s, email=%s, cpf=%s, data_nascimento=%s, observacoes=%s WHERE id=%s"""
                execute_command(query, (self.nome, self.email, self.cpf, self.data_nascimento, self.observacoes, self.id))
                return f'Pessoa atualizada com sucesso!'
            else:
                query = """INSERT INTO pessoa (nome, email, cpf, data_nascimento, observacoes) VALUES (%s, %s, %s, %s, %s)"""
                execute_command(query, (self.nome, self.email, self.cpf, self.data_nascimento, self.observacoes))
                result = read_data("SELECT LAST_INSERT_ID()")
                self.id = result[0][0]
                return f'Pessoa adicionada com sucesso! Novo ID: {self.id}'
        except Exception as e:
            return f'Erro ao salvar pessoa no banco de dados: {e}'

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

    def associar_cliente(self, cliente):
        if not self.id or not cliente.id:
            print("IDs inválidos. Carregue os objetos primeiro.")
            return

        result = read_data(
            "SELECT 1 FROM Pessoa_has_Cliente WHERE Pessoa_id = %s AND Cliente_id = %s",
            (self.id, cliente.id)
        )
        if result:
            print(f"Já existe associação entre Pessoa {self.id} e Cliente {cliente.id}.")
            return

        query = "INSERT INTO Pessoa_has_Cliente (Pessoa_id, Cliente_id) VALUES (%s, %s)"
        execute_command(query, (self.id, cliente.id))
        print(f"Pessoa {self.id} associada ao Cliente {cliente.id} com sucesso!")

    @staticmethod
    def listar_todas(imprimir=True):
        result = read_data("SELECT id, nome, email, cpf, data_nascimento, observacoes FROM pessoa ORDER BY id")
        pessoas = [Pessoa(*row[:5]) for row in result]  # o método __init__ da classe Pessoa aceita só os 5 primeiros campos

        if imprimir:
            dados_tabela = []
            for row in result:
                dados_tabela.append([
                    row[0],  # id
                    row[1],  # nome
                    row[2],  # email
                    row[3],  # cpf
                    row[4],  # data_nascimento
                    row[5] if row[5] else ""  # observacoes
                ])
            cabecalhos = ["ID", "Nome", "Email", "CPF", "Data Nasc.", "Observações"]
            print(tabulate(dados_tabela, headers=cabecalhos, tablefmt="grid"))

        return pessoas
    

class Cargo:
    def __str__(self):
        return self.nome

    def __init__(self, id=None, nome=None, salario_categoria=None, nivel_hierarquia=None, observacoes=None):
        self.id = id
        self.nome = nome
        self.salario_categoria = salario_categoria
        self.nivel_hierarquia = nivel_hierarquia
        self.observacoes = observacoes

    def carregar(self, id):
        result = read_data("SELECT id, nome, salario_categoria, nivel_hierarquia, observacoes FROM cargo WHERE id = %s", (id,))
        if result:
            self.id, self.nome, self.salario_categoria, self.nivel_hierarquia, self.observacoes = result[0]
            print(f"Cargo ID {self.id} carregado com sucesso!")
            return True
        else:
            print("Cargo não encontrado.")
            return False

    def salvar(self):
        if self.id:
            query = """UPDATE cargo SET nome=%s, salario_categoria=%s, nivel_hierarquia=%s, observacoes=%s WHERE id=%s"""
            execute_command(query, (self.nome, self.salario_categoria, self.nivel_hierarquia, self.observacoes, self.id))
            print("Cargo atualizado com sucesso!")
        else:
            query = """INSERT INTO cargo (nome, salario_categoria, nivel_hierarquia, observacoes) VALUES (%s, %s, %s, %s)"""
            execute_command(query, (self.nome, self.salario_categoria, self.nivel_hierarquia, self.observacoes))
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

    def listar_pessoas(self, imprimir=True):
        if not self.id:
            print("Fornecedor não carregado.")
            return []

        result = read_data("""
            SELECT p.id, p.nome, p.email, p.cpf, p.data_nascimento 
            FROM pessoa p
            JOIN PessoaFornecedor pf ON p.id = pf.Pessoa_id
            WHERE pf.Fornecedor_id = %s
        """, (self.id,))

        pessoas = []
        dados_tabela = []
        for row in result:
            pessoa = Pessoa(*row)
            pessoas.append(pessoa)

            dados_tabela.append([
                pessoa.id,
                pessoa.nome,
                pessoa.email,
                pessoa.cpf,
                pessoa.data_nascimento
            ])

        if imprimir:
            cabecalhos = ["ID", "Nome", "Email", "CPF", "Data Nasc."]
            print(tabulate(dados_tabela, headers=cabecalhos, tablefmt="grid"))

        return pessoas

    @staticmethod
    def listar_todos(imprimir=True):
        result = read_data("""
            SELECT id, cnpj, nome_fantasia, email_contato
            FROM fornecedor
            ORDER BY id
        """)
        fornecedores = []
        dados_tabela = []
        for row in result:
            fornecedor = Fornecedor(
                id=row[0],
                cnpj=row[1],
                nome_fantasia=row[2],
                email_contato=row[3]
            )
            fornecedores.append(fornecedor)

            dados_tabela.append([
                fornecedor.id,
                fornecedor.nome_fantasia or "",
                fornecedor.cnpj,
                fornecedor.email_contato or ""
            ])

        if imprimir:
            cabecalhos = ["ID", "Nome Fantasia", "CNPJ", "Email Contato"]
            print(tabulate(dados_tabela, headers=cabecalhos, tablefmt="grid"))

        return fornecedores

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

    @staticmethod
    def listar_todos(imprimir=True):
        result = read_data("""
            SELECT f.id, f.data_admissao, f.matricula, f.data_demissao,
                   f.Pessoa_id, f.Cargo_id,
                   p.nome AS nome_pessoa,
                   c.nome AS nome_cargo
            FROM funcionario f
            INNER JOIN pessoa p ON f.Pessoa_id = p.id
            INNER JOIN cargo c ON f.Cargo_id = c.id
            WHERE f.data_demissao IS NULL
            ORDER BY f.id
        """)

        funcionarios = []
        dados_tabela = []
        for row in result:
            funcionario = Funcionario(
                id=row[0],
                data_admissao=row[1],
                matricula=row[2],
                data_demissao=row[3],
                pessoa_id=row[4],
                cargo_id=row[5]
            )
            funcionarios.append(funcionario)
            dados_tabela.append([
                row[0],  # id
                row[6],  # nome da pessoa
                row[2],  # matrícula
                row[1],  # data de admissão
                row[7],  # nome do cargo
            ])

        if imprimir:
            cabecalhos = ["ID", "Nome", "Matrícula", "Admissão", "Cargo"]
            print(tabulate(dados_tabela, headers=cabecalhos, tablefmt="grid"))

        return funcionarios


class Produto:
    def __str__(self):
        return self.nome

    def __init__(self, id=None, nome=None, preco_unitario=None, observacoes=None, fornecedor_id=None, quantidade_estoque=None):
        self.id = id
        self.nome = nome
        self.preco_unitario = preco_unitario
        self.observacoes = observacoes
        self.fornecedor_id = fornecedor_id
        self.quantidade_estoque = quantidade_estoque

    def carregar(self, id):
        result = read_data("""
            SELECT p.id, p.nome, p.preco_unitario, p.observacoes, p.Fornecedor_id,
                   e.quantidade_atual
            FROM produto p
            LEFT JOIN estoque e ON p.id = e.Produto_id
            WHERE p.id = %s
        """, (id,))
        if result:
            (self.id, self.nome, self.preco_unitario, self.observacoes,
             self.fornecedor_id, self.quantidade_estoque) = result[0]
            print(f"Produto ID {self.id} carregado com sucesso!")
            return True
        else:
            print("Produto não encontrado.")
            return False

    def salvar(self, estoque_inicial=None):
        if self.id:
            query = """UPDATE produto SET nome=%s, preco_unitario=%s, observacoes=%s, Fornecedor_id=%s WHERE id=%s"""
            execute_command(query, (self.nome, self.preco_unitario, self.observacoes, self.fornecedor_id, self.id))
            print("Produto atualizado com sucesso!")
        else:
            query = """INSERT INTO produto (nome, preco_unitario, observacoes, Fornecedor_id) VALUES (%s, %s, %s, %s)"""
            execute_command(query, (self.nome, self.preco_unitario, self.observacoes, self.fornecedor_id))
            result = read_data("SELECT LAST_INSERT_ID()")
            self.id = result[0][0]
            print(f"Produto inserido com sucesso! Novo ID: {self.id}")
            self._criar_estoque_inicial(estoque_inicial if estoque_inicial is not None else (self.quantidade_estoque or 0))

    def deletar(self):
        if not self.id:
            print("Produto não carregado. Não é possível deletar.")
            return
        execute_command("DELETE FROM estoque WHERE Produto_id = %s", (self.id,))
        execute_command("DELETE FROM produto WHERE id = %s", (self.id,))
        print("Produto e estoque deletados com sucesso!")
        self.id = None

    # ---------------------------
    # MÉTODOS RELACIONADOS AO ESTOQUE
    # ---------------------------

    def _criar_estoque_inicial(self, quantidade=0):
        query = "INSERT INTO estoque (Produto_id, quantidade_atual) VALUES (%s, %s)"
        execute_command(query, (self.id, quantidade))
        self.quantidade_estoque = quantidade

    def carregar_estoque(self):
        result = read_data("SELECT quantidade_atual FROM estoque WHERE Produto_id = %s", (self.id,))
        if result:
            self.quantidade_estoque = result[0][0]
        else:
            print("Estoque não encontrado para o produto.")
        return self.quantidade_estoque

    def ajustar_estoque(self, delta):
        result = read_data("SELECT id, quantidade_atual FROM estoque WHERE Produto_id = %s", (self.id,))
        if result:
            estoque_id, quantidade = result[0]
            nova_qtd = quantidade + delta
            execute_command("UPDATE estoque SET quantidade_atual = %s WHERE id = %s", (nova_qtd, estoque_id))
            self.quantidade_estoque = nova_qtd
            print(f"Estoque ajustado. Nova quantidade: {nova_qtd}")
        else:
            # cria estoque, se não existir
            self._criar_estoque_inicial(delta)

    def definir_estoque(self, nova_quantidade):
        result = read_data("SELECT id FROM estoque WHERE Produto_id = %s", (self.id,))
        if result:
            estoque_id = result[0][0]
            execute_command("UPDATE estoque SET quantidade_atual = %s WHERE id = %s", (nova_quantidade, estoque_id))
        else:
            self._criar_estoque_inicial(nova_quantidade)
        self.quantidade_estoque = nova_quantidade
        print(f"Quantidade em estoque definida para {nova_quantidade}")

    @staticmethod
    def listar_todos(imprimir=True):
        result = read_data("""
            SELECT p.id, p.nome, p.preco_unitario, p.observacoes, p.Fornecedor_id,
                   e.quantidade_atual
            FROM produto p
            LEFT JOIN estoque e ON p.id = e.Produto_id
            ORDER BY p.id
        """)
        produtos = []
        dados_tabela = []
        for row in result:
            produto = Produto(
                id=row[0],
                nome=row[1],
                preco_unitario=row[2],
                observacoes=row[3],
                fornecedor_id=row[4],
                quantidade_estoque=row[5]
            )
            produtos.append(produto)
            # Linha para a tabela
            dados_tabela.append([
                produto.id,
                produto.nome,
                f"R$ {produto.preco_unitario:.2f}" if produto.preco_unitario is not None else "",
                produto.quantidade_estoque if produto.quantidade_estoque is not None else 0,
                produto.observacoes or ""
            ])

        if imprimir:
            cabecalhos = ["ID", "Nome", "Preço Unit.", "Estoque", "Observações"]
            print(tabulate(dados_tabela, headers=cabecalhos, tablefmt="grid"))

        return produtos  # ainda retorna a lista, caso queira usar depois

    @staticmethod
    def listar_todos_com_fornecedores(imprimir=True):
        result = read_data("""
            SELECT p.id, p.nome, p.preco_unitario, p.observacoes, 
                   e.quantidade_atual,
                   f.nome_fantasia, f.cnpj
            FROM produto p
            LEFT JOIN estoque e ON p.id = e.Produto_id
            INNER JOIN fornecedor f ON p.Fornecedor_id = f.id
            ORDER BY p.id
        """)
        produtos = []
        dados_tabela = []
        for row in result:
            produto = Produto(
                id=row[0],
                nome=row[1],
                preco_unitario=row[2],
                observacoes=row[3],
                fornecedor_id=None,  # opcional aqui
                quantidade_estoque=row[4]
            )
            produtos.append(produto)
            dados_tabela.append([
                row[0],  # id
                row[1],  # nome
                f"R$ {row[2]:.2f}" if row[2] is not None else "",
                row[4] if row[4] is not None else 0,  # estoque
                row[5],  # nome_fantasia
                row[6],  # cnpj
                row[3] or ""  # observações
            ])

        if imprimir:
            cabecalhos = ["ID", "Nome", "Preço Unit.", "Estoque", "Fornecedor", "CNPJ", "Observações"]
            print(tabulate(dados_tabela, headers=cabecalhos, tablefmt="grid"))

        return

class EntregaProduto:
    def __init__(self, entrega_id=None, produto_id=None, quantidade=None, preco_unitario=None):
        self.entrega_id = entrega_id
        self.produto_id = produto_id
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario

    def carregar(self, entrega_id, produto_id):
        result = read_data("""
            SELECT quantidade, preco_unitario
            FROM EntregaProduto
            WHERE Entrega_id = %s AND Produto_id = %s
        """, (entrega_id, produto_id))
        if result:
            self.entrega_id = entrega_id
            self.produto_id = produto_id
            self.quantidade, self.preco_unitario = result[0]
            print("EntregaProduto carregado com sucesso!")
            return True
        print("Relação EntregaProduto não encontrada.")
        return False

    def salvar(self):
        existente = read_data("""
            SELECT 1 FROM EntregaProduto WHERE Entrega_id = %s AND Produto_id = %s
        """, (self.entrega_id, self.produto_id))

        if existente:
            execute_command("""
                UPDATE EntregaProduto
                SET quantidade = %s, preco_unitario = %s
                WHERE Entrega_id = %s AND Produto_id = %s
            """, (self.quantidade, self.preco_unitario, self.entrega_id, self.produto_id))
            print("EntregaProduto atualizado com sucesso!")
        else:
            execute_command("""
                INSERT INTO EntregaProduto (Entrega_id, Produto_id, quantidade, preco_unitario)
                VALUES (%s, %s, %s, %s)
            """, (self.entrega_id, self.produto_id, self.quantidade, self.preco_unitario))
            print("EntregaProduto inserido com sucesso!")

    def deletar(self):
        execute_command("""
            DELETE FROM EntregaProduto
            WHERE Entrega_id = %s AND Produto_id = %s
        """, (self.entrega_id, self.produto_id))
        print("EntregaProduto deletado com sucesso!")

class Entrega:
    def __str__(self):
        return f"Entrega ID: {self.id}, Status: {self.status}"

    def __init__(self, id=None, numero_endereco=None, previsao_entrega=None, data_entregue=None,
                 status=None, observacoes=None, funcionario_id=None, cliente_id=None):
        self.id = id
        self.numero_endereco = numero_endereco
        self.previsao_entrega = previsao_entrega
        self.data_entregue = data_entregue
        self.status = status
        self.observacoes = observacoes
        self.funcionario_id = funcionario_id
        self.cliente_id = cliente_id

    def carregar(self, id):
        result = read_data("""
            SELECT id, numero_endereco, previsao_entrega, data_entregue,
                   status, observacoes, Funcionario_id, Cliente_id
            FROM entrega WHERE id = %s
        """, (id,))
        if result:
            (self.id, self.numero_endereco, self.previsao_entrega, self.data_entregue,
             self.status, self.observacoes, self.funcionario_id, self.cliente_id) = result[0]
            print(f"Entrega ID {self.id} carregada com sucesso!")
            return True
        else:
            print("Entrega não encontrada.")
            return False

    def salvar(self):
        if self.id:
            query = """UPDATE entrega SET numero_endereco=%s, previsao_entrega=%s, data_entregue=%s,
                       status=%s, observacoes=%s, Funcionario_id=%s, Cliente_id=%s WHERE id=%s"""
            execute_command(query, (self.numero_endereco, self.previsao_entrega, self.data_entregue,
                                    self.status, self.observacoes, self.funcionario_id, self.cliente_id, self.id))
            print("Entrega atualizada com sucesso!")
        else:
            query = """INSERT INTO entrega (numero_endereco, previsao_entrega, data_entregue,
                                             status, observacoes, Funcionario_id, Cliente_id)
                       VALUES (%s, %s, %s, %s, %s, %s, %s)"""
            execute_command(query, (self.numero_endereco, self.previsao_entrega, self.data_entregue,
                                    self.status, self.observacoes, self.funcionario_id, self.cliente_id))
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

    def listar_produtos(self):
        result = read_data("""
            SELECT p.id, p.nome, ep.quantidade, ep.preco_unitario
            FROM produto p
            JOIN EntregaProduto ep ON p.id = ep.Produto_id
            WHERE ep.Entrega_id = %s
        """, (self.id,))
        return result

class Cliente:
    def __str__(self):
        return self.nome_fantasia if self.nome_fantasia else str(self.id)

    def __init__(self, id=None, nome_fantasia=None, cnpj=None, numero_endereco=None, rua_id=None):
        self.id = id
        self.nome_fantasia = nome_fantasia
        self.cnpj = cnpj
        self.numero_endereco = numero_endereco
        self.rua_id = rua_id

    def carregar(self, id):
        result = read_data("SELECT id, nome_fantasia, cnpj, numero_endereco, Rua_id FROM cliente WHERE id = %s", (id,))
        if result:
            self.id, self.nome_fantasia, self.cnpj, self.numero_endereco, self.rua_id = result[0]
            print(f"Cliente ID {self.id} carregado com sucesso!")
            return True
        else:
            print("Cliente não encontrado.")
            return False

    def salvar(self):
        if self.id:
            query = """UPDATE cliente SET nome_fantasia=%s, cnpj=%s, numero_endereco=%s, Rua_id=%s WHERE id=%s"""
            execute_command(query, (self.nome_fantasia, self.cnpj, self.numero_endereco, self.rua_id, self.id))
            print("Cliente atualizado com sucesso!")
        else:
            query = """INSERT INTO cliente (nome_fantasia, cnpj, numero_endereco, Rua_id) VALUES (%s, %s, %s, %s)"""
            execute_command(query, (self.nome_fantasia, self.cnpj, self.numero_endereco, self.rua_id))
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

    def listar_pessoas(self):
        if not self.id:
            print("Cliente não carregado.")
            return []

        result = read_data("""
            SELECT p.id, p.nome, p.email, p.cpf, p.data_nascimento
            FROM pessoa p
            JOIN Pessoa_has_Cliente pc ON p.id = pc.Pessoa_id
            WHERE pc.Cliente_id = %s
        """, (self.id,))

        pessoas = [Pessoa(*row) for row in result]
        return pessoas

    @staticmethod
    def listar_todos(imprimir=True):
        query = """
            SELECT 
                c.id,
                c.nome_fantasia,
                c.cnpj,
                c.numero_endereco,
                r.Nome AS rua,
                ci.Nome AS cidade,
                es.Nome AS estado,
                p.nome AS nome_pessoa,
                p.cpf AS cpf_pessoa
            FROM cliente c
            JOIN rua r ON c.Rua_id = r.id
            JOIN cidade ci ON r.Cidade_id = ci.id
            JOIN estado es ON ci.Estado_id = es.id
            LEFT JOIN (
                SELECT phc.Cliente_id, p.nome, p.cpf
                FROM pessoa_has_cliente phc
                JOIN pessoa p ON phc.Pessoa_id = p.id
                WHERE phc.Pessoa_id = (
                    SELECT MIN(phc2.Pessoa_id)
                    FROM pessoa_has_cliente phc2
                    WHERE phc2.Cliente_id = phc.Cliente_id
                )
            ) AS p ON p.Cliente_id = c.id
            ORDER BY c.id
        """
        result = read_data(query)

        clientes = []
        dados_tabela = []

        for row in result:
            cliente = Cliente(
                id=row[0],
                nome_fantasia=row[1],
                cnpj=row[2],
                numero_endereco=row[3],
                rua_id=None
            )
            clientes.append(cliente)

            nome_exibido = row[1] if row[2] else (row[7] or "Desconhecido")
            documento = row[2] if row[2] else (row[8] or "Não informado")
            endereco = f"{row[6]} / {row[5]} / {row[4]}, {row[3]}"

            dados_tabela.append([
                cliente.id,
                nome_exibido,
                documento,
                endereco
            ])

        if imprimir:
            cabecalhos = ["ID", "Nome/Razão Social", "CPF/CNPJ", "Endereço"]
            print(tabulate(dados_tabela, headers=cabecalhos, tablefmt="grid"))

        return clientes

class Estado:
    def __init__(self, id=None, nome=None):
        self.id = id
        self.nome = nome

    def carregar(self, id):
        result = read_data("SELECT id, Nome FROM estado WHERE id = %s", (id,))
        if result:
            self.id, self.nome = result[0]
            print(f"Estado ID {self.id} carregado com sucesso!")
            return True
        print("Estado não encontrado.")
        return False

    def salvar(self):
        if self.id:
            execute_command("UPDATE estado SET Nome = %s WHERE id = %s", (self.nome, self.id))
            print("Estado atualizado com sucesso!")
        else:
            execute_command("INSERT INTO estado (Nome) VALUES (%s)", (self.nome,))
            self.id = read_data("SELECT LAST_INSERT_ID()")[0][0]
            print(f"Estado inserido com sucesso! Novo ID: {self.id}")

    def deletar(self):
        execute_command("DELETE FROM estado WHERE id = %s", (self.id,))
        print("Estado deletado com sucesso!")
        self.id = None

class Cidade:
    def __init__(self, id=None, nome=None, estado_id=None):
        self.id = id
        self.nome = nome
        self.estado_id = estado_id

    def carregar(self, id):
        result = read_data("SELECT id, Nome, Estado_id FROM cidade WHERE id = %s", (id,))
        if result:
            self.id, self.nome, self.estado_id = result[0]
            print(f"Cidade ID {self.id} carregada com sucesso!")
            return True
        print("Cidade não encontrada.")
        return False

    def salvar(self):
        if self.id:
            execute_command("UPDATE cidade SET Nome = %s, Estado_id = %s WHERE id = %s", (self.nome, self.estado_id, self.id))
            print("Cidade atualizada com sucesso!")
        else:
            execute_command("INSERT INTO cidade (Nome, Estado_id) VALUES (%s, %s)", (self.nome, self.estado_id))
            self.id = read_data("SELECT LAST_INSERT_ID()")[0][0]
            print(f"Cidade inserida com sucesso! Novo ID: {self.id}")

    def deletar(self):
        execute_command("DELETE FROM cidade WHERE id = %s", (self.id,))
        print("Cidade deletada com sucesso!")
        self.id = None

class Rua:
    def __init__(self, id=None, nome=None, cep=None, cidade_id=None):
        self.id = id
        self.nome = nome
        self.cep = cep
        self.cidade_id = cidade_id

    def carregar(self, id):
        result = read_data("SELECT id, Nome, cep, Cidade_id FROM rua WHERE id = %s", (id,))
        if result:
            self.id, self.nome, self.cep, self.cidade_id = result[0]
            print(f"Rua ID {self.id} carregada com sucesso!")
            return True
        print("Rua não encontrada.")
        return False

    def salvar(self):
        if self.id:
            execute_command("UPDATE rua SET Nome = %s, cep = %s, Cidade_id = %s WHERE id = %s", (self.nome, self.cep, self.cidade_id, self.id))
            print("Rua atualizada com sucesso!")
        else:
            execute_command("INSERT INTO rua (Nome, cep, Cidade_id) VALUES (%s, %s, %s)", (self.nome, self.cep, self.cidade_id))
            self.id = read_data("SELECT LAST_INSERT_ID()")[0][0]
            print(f"Rua inserida com sucesso! Novo ID: {self.id}")

    def deletar(self):
        execute_command("DELETE FROM rua WHERE id = %s", (self.id,))
        print("Rua deletada com sucesso!")
        self.id = None
