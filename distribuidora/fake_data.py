from mysql_codes import *

def generate_data(connection, cursor):
    """Generate data for the database."""
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
    execute_command(connection, cursor, command)
    print('Data generated successfully.')


