from mysql_codes import *

def generate_data():
    """Generate data for the database."""
    if not read_data('SELECT id FROM pessoa'):
        print('No data found in the database. Generating fake data...')
        command = (
            'INSERT INTO pessoa (nome, email, cpf, data_nascimento) VALUES '
            '("luis", "luis@gmail.com", "98765432101", "2000-01-01"), '
            '("ana", "ana.souza@gmail.com", "12345678901", "1995-04-15"), '
            '("bruno", "bruno.costa@gmail.com", "23456789012", "1990-08-22"), '
            '("carla", "carla.mendes@gmail.com", "34567890123", "1988-12-05"), '
            '("daniel", "daniel.rocha@gmail.com", "45678901234", "1992-06-18"), '
            '("eduarda", "eduarda.lima@gmail.com", "56789012345", "1998-10-30"), '
            '("felipe", "felipe.alves@gmail.com", "67890123456", "1991-03-11"), '
            '("gabriela", "gabriela.santos@gmail.com", "78901234567", "1994-07-25"), '
            '("henrique", "henrique.barbosa@gmail.com", "89012345678", "1987-11-08"), '
            '("isabela", "isabela.ferreira@gmail.com", "90123456789", "1993-05-19"), '
            '("joão", "joao.pereira@gmail.com", "01234567890", "1985-09-27"), '
            '("mariana", "mariana.silva@gmail.com", "13579246801", "1999-01-09"), '
            '("otavio", "otavio.moreira@gmail.com", "24680135792", "1996-04-04"), '
            '("priscila", "priscila.campos@gmail.com", "35791357913", "1986-02-20"), '
            '("ricardo", "ricardo.teixeira@gmail.com", "46802468024", "1989-08-16"), '
            '("sara", "sara.dias@gmail.com", "57913579135", "1997-12-12"), '
            '("tiago", "tiago.ramos@gmail.com", "68024680246", "1992-02-28"), '
            '("vanessa", "vanessa.moraes@gmail.com", "79135791357", "1990-06-06"), '
            '("wagner", "wagner.souza@gmail.com", "80246802468", "1984-11-23"), '
            '("yasmin", "yasmin.nunes@gmail.com", "91357913579", "1996-03-14"), '
            '("zeca", "zeca.machado@gmail.com", "02468024680", "1989-07-01"), '
            '("aline", "aline.carvalho@gmail.com", "13579135791", "1993-10-10"), '
            '("beto", "beto.silveira@gmail.com", "24680246802", "1991-09-09"), '
            '("cintia", "cintia.paz@gmail.com", "35791357914", "1994-04-04"), '
            '("darlan", "darlan.oliveira@gmail.com", "46802468025", "1987-01-30")'
        )
        execute_command(command)

    if not read_data('SELECT id FROM cargo'):
        command = (
            'INSERT INTO cargo (nome, salario_categoria, descricao, nivel_hierarquia) VALUES '
            '("Gerente Geral", "R$ 10.000", "Responsável por toda a operação da distribuidora", 1), '
            '("Supervisor de Logística", "R$ 6.500", "Supervisiona as atividades de transporte e estoque", 2), '
            '("Analista de Compras", "R$ 5.000", "Analisa fornecedores e realiza negociações", 3), '
            '("Vendedor Externo", "R$ 4.200", "Realiza visitas a clientes e fechamento de pedidos", 4), '
            '("Assistente Administrativo", "R$ 3.500", "Apoia tarefas administrativas e financeiras", 5), '
            '("Motorista", "R$ 3.000", "Realiza entregas de produtos aos clientes", 6), '
            '("Auxiliar de Estoque", "R$ 2.800", "Organiza e controla o estoque no armazém", 7), '
            '("Estagiário de Logística", "R$ 1.200", "Apoia a equipe de logística nas rotinas diárias", 8), '
            '("Técnico de Qualidade", "R$ 4.700", "Verifica padrões e normas dos produtos distribuídos", 4), '
            '("Coordenador Comercial", "R$ 6.800", "Coordena a equipe de vendas e estratégias comerciais", 2)'
        )
        execute_command(command)
    if not read_data('SELECT id FROM funcionario'):
        command = (
            'INSERT INTO funcionario (data_admissao, matricula, Pessoa_id, Cargo_id) VALUES '
            '("2020-01-15", "MAT001", 1, 1), '
            '("2021-03-10", "MAT002", 2, 2), '
            '("2019-11-20", "MAT003", 3, 3), '
            '("2022-06-05", "MAT004", 4, 4), '
            '("2021-08-17", "MAT005", 5, 5), '
            '("2023-02-01", "MAT006", 6, 6), '
            '("2018-07-12", "MAT007", 7, 7), '
            '("2020-09-30", "MAT008", 8, 8), '
            '("2021-12-11", "MAT009", 9, 9), '
            '("2019-04-03", "MAT010", 10, 10), '
            '("2020-05-27", "MAT011", 11, 4), '
            '("2022-01-22", "MAT012", 12, 5), '
            '("2023-04-14", "MAT013", 13, 6), '
            '("2021-10-19", "MAT014", 14, 7), '
            '("2020-12-01", "MAT015", 15, 8) '
        )
        execute_command(command)
    if not read_data('SELECT id FROM fornecedor'):
        command = (
            'INSERT INTO fornecedor (cnpj, nome_fantasia, email_contato, Pessoa_id) VALUES '
            '("12.345.678/0001-01", "Queijos Minas Ltda", "contato@queijosminas.com", 16), '
            '("98.765.432/0001-02", "Delícias do Campo", "vendas@deliciasdocampo.com", 17), '
            '("45.678.912/0001-03", "Sabor da Serra", "comercial@sabordaserra.com", 18), '
            '("23.456.789/0001-04", "Laticínios Brasil", "atendimento@laticiniosbrasil.com", 19), '
            '("67.890.123/0001-05", "Produtos Naturais Vale", "suporte@pvale.com", 20), '
            '("34.567.890/0001-06", "Artesanal Sul", "faleconosco@artesanalsul.com", 21), '
            '("56.789.012/0001-07", "Empório Serrano", "contato@emporioserrano.com", 22), '
            '("78.901.234/0001-08", "Fazenda Bela Vista", "comercial@belavista.com", 23), '
            '("89.012.345/0001-09", "Sabores do Interior", "vendas@saboresinterior.com", 24), '
            '("90.123.456/0001-10", "Raízes Gourmet", "raizes@gourmet.com", 25)'
        )
        execute_command(command)
    if not read_data('SELECT id FROM telefone'):
        command = (
            'INSERT INTO telefone (tipo, ddd, numero, Pessoa_id) VALUES '
            '("celular", "11", "987654321", 1), '
            '("residencial", "21", "345678901", 2), '
            '("comercial", "31", "912345678", 3), '
            '("celular", "41", "998877665", 4), '
            '("residencial", "51", "934567890", 5), '
            '("comercial", "61", "956789012", 6), '
            '("celular", "71", "976543210", 7), '
            '("residencial", "81", "967890123", 8), '
            '("comercial", "91", "945612378", 9), '
            '("celular", "31", "923456789", 10), '
            '("residencial", "41", "934561278", 11), '
            '("comercial", "51", "987612345", 12), '
            '("celular", "61", "998123456", 13), '
            '("residencial", "71", "976534128", 14), '
            '("comercial", "81", "934786512", 15), '
            '("comercial", "11", "343212345", 16), '
            '("celular", "11", "987123456", 16), '
            '("comercial", "21", "322456789", 17), '
            '("celular", "21", "988765432", 17), '
            '("comercial", "31", "301234567", 18), '
            '("celular", "31", "976543219", 18), '
            '("comercial", "41", "344567890", 19), '
            '("celular", "41", "997123456", 19), '
            '("comercial", "51", "366789012", 20), '
            '("celular", "51", "985432198", 20), '
            '("comercial", "61", "388123456", 21), '
            '("celular", "61", "992345678", 21), '
            '("comercial", "71", "399456123", 22), '
            '("celular", "71", "989876543", 22), '
            '("comercial", "81", "377765432", 23), '
            '("celular", "81", "991234567", 23), '
            '("comercial", "91", "388976543", 24), '
            '("celular", "91", "987654320", 24), '
            '("comercial", "31", "344556677", 25), '
            '("celular", "31", "988123456", 25)'
        )
        execute_command(command)

    print('Data generated successfully.')


