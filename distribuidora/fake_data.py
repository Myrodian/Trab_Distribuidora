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
            
            '("darlan", "darlan.oliveira@gmail.com", "46802468025", "1987-01-30"), '
            '("eduardo", "eduardo.silva@gmail.com", "12312312312", "1990-02-10"), '
            '("fernanda", "fernanda.oliveira@gmail.com", "45645645645", "1991-05-20"), '
            '("gustavo", "gustavo.martins@gmail.com", "78978978978", "1989-08-15"), '
            '("helena", "helena.almeida@gmail.com", "32132132132", "1993-11-25"), '
            '("igor", "igor.cardoso@gmail.com", "65465465465", "1995-03-30"), '
            '("julia", "julia.pereira@gmail.com", "98798798798", "1994-07-12"), '
            '("leonardo", "leonardo.mendes@gmail.com", "15915915915", "1988-12-01"), '
            '("marcela", "marcela.ferraz@gmail.com", "75375375375", "1992-09-18"), '
            '("nicolas", "nicolas.souza@gmail.com", "25825825825", "1996-06-06"), '
            '("olivia", "olivia.ramos@gmail.com", "36936936936", "1990-04-04"), '
            '("paulo", "paulo.vieira@gmail.com", "11122233344", "1990-01-15"), '
            '("renata", "renata.souza@gmail.com", "22233344455", "1987-05-23"), '
            '("samuel", "samuel.lima@gmail.com", "33344455566", "1992-09-30"), '
            '("talita", "talita.alves@gmail.com", "44455566677", "1995-12-12"), '
            '("vinicius", "vinicius.martins@gmail.com", "55566677788", "1991-03-03")'
        )
        execute_command(command)
    if not read_data('SELECT id FROM cargo'):
        command = (
            'INSERT INTO cargo (nome, salario_categoria, nivel_hierarquia, observacoes) VALUES '
            '("Gerente Geral", "R$ 10.000", 1, "Responsável por toda a operação da distribuidora"), '
            '("Supervisor de Logística", "R$ 6.500", 2, "Supervisiona as atividades de transporte e estoque"), '
            '("Analista de Compras", "R$ 5.000", 3, "Analisa fornecedores e realiza negociações"), '
            '("Vendedor Externo", "R$ 4.200", 4, "Realiza visitas a clientes e fechamento de pedidos"), '
            '("Assistente Administrativo", "R$ 3.500", 5, "Apoia tarefas administrativas e financeiras"), '
            '("Motorista", "R$ 3.000", 6, "Realiza entregas de produtos aos clientes"), '
            '("Auxiliar de Estoque", "R$ 2.800", 7, "Organiza e controla o estoque no armazém"), '
            '("Estagiário de Logística", "R$ 1.200", 8, "Apoia a equipe de logística nas rotinas diárias"), '
            '("Técnico de Qualidade", "R$ 4.700", 4, "Verifica padrões e normas dos produtos distribuídos"), '
            '("Coordenador Comercial", "R$ 6.800", 2, "Coordena a equipe de vendas e estratégias comerciais")'
        )
        execute_command(command)
    if not read_data('SELECT id FROM funcionario'):
        command = (
            'INSERT INTO funcionario (data_admissao, matricula, Pessoa_id, Cargo_id, observacoes, data_demissao) VALUES '
            '("2020-01-15", "MAT001", 1, 1, NULL, NULL), '
            '("2021-03-10", "MAT002", 2, 6, NULL, NULL), '
            '("2019-11-20", "MAT003", 3, 3, NULL, NULL), '
            '("2022-06-05", "MAT004", 4, 6, NULL, NULL), '
            '("2021-08-17", "MAT005", 5, 5, NULL, NULL), '
            '("2023-02-01", "MAT006", 6, 6, NULL, NULL), '
            '("2018-07-12", "MAT007", 7, 7, NULL, NULL), '
            '("2020-09-30", "MAT008", 8, 8, NULL, NULL), '
            '("2021-12-11", "MAT009", 9, 9, NULL, NULL), '
            '("2019-04-03", "MAT010", 10, 10, NULL, "2020-05-10"), '
            '("2020-05-27", "MAT011", 11, 4, NULL, NULL), '
            '("2022-01-22", "MAT012", 12, 5, NULL, NULL), '
            '("2023-04-14", "MAT013", 13, 6, NULL, "2025-03-27"), '
            '("2021-10-19", "MAT014", 14, 7, NULL, NULL), '
            '("2020-12-01", "MAT015", 15, 8, NULL, NULL)'
        )
        execute_command(command)
    if not read_data('SELECT id FROM fornecedor'):
        command = (
            'INSERT INTO fornecedor (cnpj, nome_fantasia, email_contato, observacoes) VALUES '
            '("12.345.678/0001-01", "Queijos Minas Ltda", "contato@queijosminas.com", NULL), '
            '("98.765.432/0001-02", "Delícias do Campo", "vendas@deliciasdocampo.com", NULL), '
            '("45.678.912/0001-03", "Sabor da Serra", "comercial@sabordaserra.com", NULL), '
            '("23.456.789/0001-04", "Laticínios Brasil", "atendimento@laticiniosbrasil.com", NULL), '
            '("67.890.123/0001-05", "Produtos Naturais Vale", "suporte@pvale.com", NULL), '
            '("34.567.890/0001-06", "Artesanal Sul", "faleconosco@artesanalsul.com", NULL), '
            '("56.789.012/0001-07", "Empório Serrano", "contato@emporioserrano.com", NULL), '
            '("78.901.234/0001-08", "Fazenda Bela Vista", "comercial@belavista.com", NULL), '
            '("89.012.345/0001-09", "Sabores do Interior", "vendas@saboresinterior.com", NULL), '
            '("90.123.456/0001-10", "Raízes Gourmet", "raizes@gourmet.com", NULL)'
        )
        execute_command(command)
    if not read_data('SELECT * FROM pessoafornecedor'):
        command = (
            'INSERT INTO pessoafornecedor (Pessoa_id, Fornecedor_id) VALUES '
            '(16, 1), (17, 2), (18, 3), (19, 4), (20, 5), '
            '(21, 6), (22, 7), (23, 8), (24, 9), (25, 10)'
        )
        execute_command(command)
    if not read_data('SELECT id FROM telefone'):
        command = (
            'INSERT INTO telefone (tipo, ddd, numero, Pessoa_id) VALUES '
            '("celular", "011", "987654321", 1), '
            '("residencial", "021", "345678901", 2), '
            '("comercial", "031", "912345678", 3), '
            '("celular", "041", "998877665", 4), '
            '("residencial", "051", "934567890", 5), '
            '("comercial", "061", "956789012", 6), '
            '("celular", "071", "976543210", 7), '
            '("residencial", "081", "967890123", 8), '
            '("comercial", "091", "945612378", 9), '
            '("celular", "031", "923456789", 10), '
            '("residencial", "041", "934561278", 11), '
            '("comercial", "051", "987612345", 12), '
            '("celular", "061", "998123456", 13), '
            '("residencial", "071", "976534128", 14), '
            '("comercial", "081", "934786512", 15), '
            '("comercial", "011", "343212345", 16), '
            '("celular", "011", "987123456", 16), '
            '("comercial", "021", "322456789", 17), '
            '("celular", "021", "988765432", 17), '
            '("comercial", "031", "301234567", 18), '
            '("celular", "031", "976543219", 18), '
            '("comercial", "041", "344567890", 19), '
            '("celular", "041", "997123456", 19), '
            '("comercial", "051", "366789012", 20), '
            '("celular", "051", "985432198", 20), '
            '("comercial", "061", "388123456", 21), '
            '("celular", "061", "992345678", 21), '
            '("comercial", "071", "399456123", 22), '
            '("celular", "071", "989876543", 22), '
            '("comercial", "081", "377765432", 23), '
            '("celular", "081", "991234567", 23), '
            '("comercial", "091", "388976543", 24), '
            '("celular", "091", "987654320", 24), '
            '("comercial", "031", "344556677", 25), '
            '("celular", "031", "988123456", 25)'
        )
        execute_command(command)
    if not read_data('SELECT id FROM estado'):
        command = (
            'INSERT INTO estado (nome) VALUES '
            '("São Paulo"), '
            '("Minas Gerais"), '
            '("Rio de Janeiro"), '
            '("Bahia"), '
            '("Paraná")'
        )
        execute_command(command)
    if not read_data('SELECT id FROM cidade'):
        command = (
            'INSERT INTO cidade (nome, Estado_id) VALUES '
            '("Campinas", 1), '
            '("Uberlândia", 2), '
            '("Niterói", 3), '
            '("Salvador", 4), '
            '("Curitiba", 5), '
            '("São Paulo", 1), '
            '("Belo Horizonte", 2), '
            '("Rio de Janeiro", 3), '
            '("Feira de Santana", 4), '
            '("Londrina", 5)'
        )
        execute_command(command)
    if not read_data('SELECT id FROM rua'):
        command = (
            'INSERT INTO rua (nome, cep, Cidade_id) VALUES '
            '("Rua das Laranjeiras", 13010000, 1), '
            '("Avenida Floriano", 38400000, 2), '
            '("Rua das Acácias", 24210000, 3), '
            '("Avenida Sete", 40000000, 4), '
            '("Rua XV de Novembro", 80000000, 5), '
            '("Avenida Paulista", 13020000, 6), '
            '("Rua da Bahia", 30100000, 7), '
            '("Rua Voluntários", 22000000, 8), '
            '("Rua Conselheiro", 44000000, 9), '
            '("Rua Souza Naves", 86000000, 10)'
        )
        execute_command(command)
    if not read_data('SELECT id FROM produto'):
        command = (
            'INSERT INTO produto (nome, observacoes, preco_unitario, Fornecedor_id) VALUES '
            '("Queijo Minas Frescal", "Queijo fresco tradicional de Minas", 25.50, 1), '
            '("Doce de Leite", "Doce cremoso feito com leite e açúcar", 15.00, 2), '
            '("Requeijão Cremoso", "Produto pastoso para pães e torradas", 12.00, 3), '
            '("Iogurte Natural", "Iogurte sem açúcar, ideal para dietas", 8.50, 4), '
            '("Leite Integral", "Leite pasteurizado integral", 5.70, 5), '
            '("Manteiga Artesanal", "Feita com creme de leite fresco", 18.20, 6), '
            '("Queijo Prato", "Queijo amarelo ideal para lanches", 22.00, 7), '
            '("Ricota Fresca", "Leve e com baixo teor de gordura", 10.30, 8), '
            '("Bebida Láctea", "Com sabor de morango", 6.50, 9), '
            '("Iogurte Grego", "Mais cremoso e proteico", 9.90, 10), '
            '("Queijo Coalho", "Ideal para churrascos", 19.75, 1), '
            '("Mussarela de Búfala", "Queijo nobre, ótimo para saladas", 28.00, 2), '
            '("Queijo Parmesão", "Ideal para massas", 35.00, 3), '
            '("Achocolatado", "Bebida láctea sabor chocolate", 6.75, 4), '
            '("Creme de Leite", "Para receitas doces e salgadas", 7.80, 5), '
            '("Iogurte com Granola", "Lanche saudável", 11.50, 6), '
            '("Bebida Vegetal", "Feita com castanhas", 14.90, 7), '
            '("Leite Desnatado", "Menos gordura", 5.40, 8), '
            '("Bebida Proteica", "Enriquecida com whey", 12.90, 9), '
            '("Queijo Azul", "Sabor marcante e maturado", 33.00, 10)'
        )
        execute_command(command)
    if not read_data('SELECT id FROM cliente'):
        command = (
            'INSERT INTO Cliente (nome_fantasia, cnpj, numero_endereco, Rua_id) VALUES '
            '(NULL, NULL, 738, 1), '
            '("Eduardo ME", "12.312.312/0001-12", 512, 2), '
            '(NULL, NULL, 264, 3), '
            '(NULL, NULL, 883, 4), '
            '("Helena Distribuidora", "32.132.132/0001-32", 199, 5), '
            '(NULL, NULL, 411, 6), '
            '(NULL, NULL, 620, 7), '
            '(NULL, NULL, 347, 8), '
            '("Marcela Atacadista", "75.375.375/0001-75", 185, 9), '
            '(NULL, NULL, 921, 10)'
        )
        execute_command(command)
    if not read_data('SELECT id FROM entrega'):
        command = (
            'INSERT INTO Entrega (numero_endereco, previsao_entrega, data_entregue, status, observacoes, Funcionario_id, Cliente_id) VALUES '
            '(738, "2023-02-15", "2023-02-15 09:12:00", "entregue", "Entrega sem problemas", 2, 1), '
            '(512, "2024-04-03", NULL, "pendente", NULL, 4, 2), '
            '(264, "2025-01-20", NULL, "em trânsito", NULL, 6, 3), '
            '(883, "2023-06-10", "2023-06-10 18:50:00", "entregue", "Cliente não encontrado na primeira tentativa", 13, 4), '
            '(199, "2025-03-12", "2025-03-12 07:40:00", "entregue", NULL, 2, 5), '
            '(411, "2023-11-09", NULL, "pendente", NULL, 4, 6), '
            '(620, "2024-08-21", "2024-08-21 10:10:00", "entregue", "Produto parcialmente avariado", 6, 7), '
            '(347, "2025-05-25", "2025-05-25 20:15:00", "entregue", NULL, 13, 8), '
            '(185, "2023-09-17", NULL, "pendente", NULL, 2, 9), '
            '(921, "2024-10-01", "2024-10-01 14:30:00", "entregue", NULL, 4, 10), '
            '(578, "2025-06-05", "2025-06-05 09:45:00", "entregue", NULL, 6, 1), '
            '(337, "2024-07-18", NULL, "em trânsito", NULL, 13, 2), '
            '(404, "2023-03-23", "2023-03-23 16:05:00", "entregue", NULL, 2, 3), '
            '(810, "2025-01-09", NULL, "pendente", "Clima severo na região", 4, 4), '
            '(690, "2024-05-02", "2024-05-02 18:40:00", "entregue", NULL, 6, 5), '
            '(205, "2023-12-14", "2023-12-14 13:55:00", "entregue", NULL, 13, 6), '
            '(754, "2024-09-06", NULL, "pendente", NULL, 2, 7), '
            '(146, "2025-02-20", "2025-02-20 11:50:00", "entregue", NULL, 4, 8), '
            '(829, "2023-07-29", NULL, "em trânsito", NULL, 6, 9), '
            '(312, "2024-11-11", "2024-11-11 08:22:00", "entregue", NULL, 13, 10)'
        )
        execute_command(command)
    if not read_data('SELECT * FROM EntregaProduto'):
        command = (
            'INSERT INTO EntregaProduto (Entrega_id, Produto_id, quantidade, preco_unitario) VALUES '
            '(1, 1, 10, 25.50), '
            '(1, 5, 5, 5.70), '
            '(2, 2, 8, 15.00), '
            '(3, 4, 12, 8.50), '
            '(4, 3, 6, 12.00), '
            '(5, 7, 3, 22.00), '
            '(6, 6, 7, 18.20), '
            '(7, 9, 9, 6.50), '
            '(8, 10, 4, 9.90), '
            '(9, 8, 2, 10.30), '
            '(10, 11, 5, 19.75), '
            '(11, 12, 6, 28.00), '
            '(12, 13, 7, 35.00), '
            '(13, 14, 10, 6.75), '
            '(14, 15, 8, 7.80), '
            '(15, 16, 9, 11.50), '
            '(16, 17, 3, 14.90), '
            '(17, 18, 4, 5.40), '
            '(18, 19, 2, 12.90), '
            '(19, 20, 1, 33.00), '
            '(20, 1, 5, 25.50)'
        )
        execute_command(command)
    if not read_data('SELECT id FROM estoque'):
        command = (
            'INSERT INTO Estoque (quantidade_atual, Produto_id) VALUES '
            '(100, 1), '
            '(80, 2), '
            '(60, 3), '
            '(90, 4), '
            '(150, 5), '
            '(70, 6), '
            '(120, 7), '
            '(85, 8), '
            '(110, 9), '
            '(95, 10), '
            '(75, 11), '
            '(65, 12), '
            '(55, 13), '
            '(130, 14), '
            '(140, 15), '
            '(50, 16), '
            '(115, 17), '
            '(125, 18), '
            '(135, 19), '
            '(105, 20)'
        )
        execute_command(command)
    if not read_data('SELECT * FROM pessoa_has_cliente'):
        command = (
            'INSERT INTO Pessoa_has_Cliente (Pessoa_id, Cliente_id) VALUES '
            '(26, 1), '
            '(27, 2), '
            '(28, 2), '
            '(29, 2), '
            '(30, 3), '
            '(31, 4), '
            '(32, 5), '
            '(33, 5), '
            '(34, 5), '
            '(35, 5), '
            '(36, 6), '
            '(37, 7), '
            '(38, 8), '
            '(39, 9), '
            '(40, 9), '
            '(26, 9)'
            '(27, 10)'
            '(28, 10)'

        )
        execute_command(command)

    print('Data generated successfully.')


