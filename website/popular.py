from faker import Faker
import random
from database import execute_sql

fake = Faker('pt_BR')

def sanitize_utf8(text):
    if isinstance(text, str):
        return text.encode('utf-8', errors='ignore').decode('utf-8', errors='ignore')
    return text

def inserir_usuario():
    """Insere um novo usuário e retorna seu ID."""
    id_cliente = random.randint(1000, 9999)
    cpf = fake.cpf().replace('.', '').replace('-', '')
    nome = sanitize_utf8(fake.name())
    telefone = fake.msisdn()[:11]
    execute_sql(
        "INSERT INTO Usuario (ID_Cliente, CPF, Nome, Telefone) VALUES (%s, %s, %s, %s)",
        (id_cliente, cpf, nome, telefone)
    )
    return id_cliente

def inserir_dados_secundarios(id_cliente):
    """Insere dados de Conta, Cartão, Depósito, etc., para um cliente existente."""

    # 1. Conta
    while True:
        id_numero = random.randint(10000, 99999)
        existe = execute_sql("SELECT 1 FROM Conta WHERE ID_Numero = %s", (id_numero,), fetch_one=True)
        if not existe:
            break
    saldo = random.randint(100, 10000)
    execute_sql("INSERT INTO Conta (ID_Numero, Saldo, ID_Cliente) VALUES (%s, %s, %s)", (id_numero, saldo, id_cliente))

    tipo_conta = random.choice(['corrente', 'poupanca', 'salario'])
    if tipo_conta == 'corrente':
        execute_sql("INSERT INTO Corrente (ID_Numero) VALUES (%s)", (id_numero,))
    elif tipo_conta == 'poupanca':
        rentabilidade = random.randint(1, 10)
        execute_sql("INSERT INTO Poupanca (ID_Numero, Rentabilidade) VALUES (%s, %s)", (id_numero, rentabilidade))
    else:
        contratante = sanitize_utf8(fake.company())
        execute_sql("INSERT INTO Salario (ID_Numero, Contratante) VALUES (%s, %s)", (id_numero, contratante))

    # 2. Cartão
    while True:
        id_card = random.randint(100000, 999999)
        existe = execute_sql("SELECT 1 FROM Cartao WHERE ID_CardNumber = %s", (id_card,), fetch_one=True)
        if not existe:
            break
    execute_sql("INSERT INTO Cartao (ID_CardNumber, ID_Numero) VALUES (%s, %s)", (id_card, id_numero))

    if random.choice([True, False]):
        execute_sql("INSERT INTO Debito (ID_CardNumber) VALUES (%s)", (id_card,))
    else:
        vencimento = fake.date_this_year()
        limite = round(random.uniform(500, 5000), 2)
        execute_sql("INSERT INTO Credito (ID_CardNumber, Vencimento_Cartao, Limite) VALUES (%s, %s, %s)", (id_card, vencimento, limite))

    # 3. Depósito
    while True:
        id_pag = random.randint(1000000, 9999999)
        existe = execute_sql("SELECT 1 FROM Deposito WHERE ID_Pag = %s", (id_pag,), fetch_one=True)
        if not existe:
            break
    valor_pag = random.randint(50, 5000)
    status_pag = random.choice([True, False])
    data_pag = fake.date_this_year()
    execute_sql("INSERT INTO Deposito (ID_Pag, Valor_Pag, Status_Pag, Data_Pag) VALUES (%s, %s, %s, %s)", (id_pag, valor_pag, status_pag, data_pag))

    # 4. Fatura, Compra, etc.
    if random.choice([True, False]):
        execute_sql("INSERT INTO Fatura (ID_Pag) VALUES (%s)", (id_pag,))
        if random.choice([True, False]):
            while True:
                id_compra = random.randint(100000, 999999)
                existe = execute_sql("SELECT 1 FROM Compras WHERE ID_Compra = %s", (id_compra,), fetch_one=True)
                if not existe:
                    break
            data_compra = fake.date_this_year()
            valor = round(random.uniform(10, 1000), 2)
            estabelecimento = sanitize_utf8(fake.company())
            execute_sql("INSERT INTO Compras (ID_Compra, ID_CardNumber, ID_Pag, Data_Compra, Valor, Estabelecimento) VALUES (%s, %s, %s, %s, %s, %s)", (id_compra, id_card, id_pag, data_compra, valor, estabelecimento))
            if random.choice([True, False]):
                execute_sql("INSERT INTO A_Prazo (ID_Compra) VALUES (%s)", (id_compra,))
            else:
                execute_sql("INSERT INTO A_Vista (ID_Compra) VALUES (%s)", (id_compra,))

    # 5. Investimento
    if random.choice([True, False]):
        tipo_invest = random.choice(['CDB', 'LCI', 'LCA', 'Tesouro'])
        rentabilidade = random.randint(1, 10)
        execute_sql("INSERT INTO Investimento (ID_Pag, Tipo_Invest, Rentabilidade) VALUES (%s, %s, %s)", (id_pag, tipo_invest, rentabilidade))

    # 6. Boleto
    if random.choice([True, False]):
        vencimento_boleto = fake.date_this_year()
        codigo = random.randint(10000000, 99999999)
        favorecido = sanitize_utf8(fake.name())
        valor_boleto = round(random.uniform(50, 2000), 2)
        pagador = sanitize_utf8(fake.name())
        execute_sql("INSERT INTO Boleto (ID_Pag, Vencimento_Boleto, Codigo, Favorecido, Valor_Boleto, Pagador) VALUES (%s, %s, %s, %s, %s, %s)", (id_pag, vencimento_boleto, codigo, favorecido, valor_boleto, pagador))


def popular_todas_tabelas(qtd_usuarios=10):
    for _ in range(qtd_usuarios):
        id_cliente = inserir_usuario()
        inserir_dados_secundarios(id_cliente)

def popular_dados_para_usuarios_existentes(qtd_por_usuario=3):
    usuarios = execute_sql("SELECT ID_Cliente FROM Usuario", fetch=True)
    for usuario in usuarios:
        id_cliente = usuario['id_cliente'] if 'id_cliente' in usuario else usuario['ID_Cliente']
        for _ in range(qtd_por_usuario):
            inserir_dados_secundarios(id_cliente)

if __name__ == "__main__":
    popular_todas_tabelas(qtd_usuarios=10)
    print("Todas as tabelas populadas com dados aleatórios!")