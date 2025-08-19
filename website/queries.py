from website.database import execute_sql

def get_investimentos_por_usuario_ordenado_tipo(id_cliente):
    """
    Retorna os investimentos de um usuário ordenados por tipo.
    """
    query = """
        SELECT i.ID_Pag, i.Tipo_Invest, i.Rentabilidade
        FROM Investimento i
        JOIN Deposito d ON i.ID_Pag = d.ID_Pag
        JOIN Conta c ON c.ID_Cliente = %s
        WHERE d.ID_Pag = i.ID_Pag
        ORDER BY i.Tipo_Invest ASC
    """
    return execute_sql(query, params=(id_cliente,), fetch=True)
from website.database import execute_sql

def get_investimentos_por_usuario(id_cliente):
    """
    Retorna os investimentos de um usuário ordenados por rentabilidade crescente.
    """
    query = """
        SELECT i.ID_Pag, i.Tipo_Invest, i.Rentabilidade
        FROM Investimento i
        JOIN Deposito d ON i.ID_Pag = d.ID_Pag
        JOIN Conta c ON d.ID_Pag = c.ID_Cliente
        WHERE c.ID_Cliente = %s
        ORDER BY i.Rentabilidade ASC
    """
    return execute_sql(query, params=(id_cliente,), fetch=True)

def get_historico_depositos_usuario(id_cliente, ordem='ASC'):
    """
    Retorna o histórico de depósitos de um usuário ordenado por data.
    ordem: 'ASC' para crescente, 'DESC' para decrescente.
    """
    query = f'''
        SELECT d.ID_Pag, d.Valor_Pag, d.Status_Pag, d.Data_Pag
        FROM Deposito d
        JOIN Conta c ON c.ID_Cliente = %s
        WHERE d.ID_Pag IN (
            SELECT i.ID_Pag FROM Investimento i WHERE i.ID_Pag = d.ID_Pag
            UNION
            SELECT b.ID_Pag FROM Boleto b WHERE b.ID_Pag = d.ID_Pag
            UNION
            SELECT f.ID_Pag FROM Fatura f WHERE f.ID_Pag = d.ID_Pag
        )
        ORDER BY d.Data_Pag {ordem}
    '''
    return execute_sql(query, params=(id_cliente,), fetch=True)

def get_historico_depositos_usuario_crescente(id_cliente):
    return get_historico_depositos_usuario(id_cliente, ordem='ASC')

def get_historico_depositos_usuario_decrescente(id_cliente):
    return get_historico_depositos_usuario(id_cliente, ordem='DESC')

def get_faturas_compras_por_data_e_usuario(data_compra, id_cliente):
    """
    Retorna as faturas das compras realizadas em uma determinada data por um usuário específico.
    """
    query = """
        SELECT f.ID_Pag, c.ID_Compra, c.Data_Compra, c.Valor, c.Estabelecimento
        FROM Fatura f
        JOIN Compras c ON f.ID_Pag = c.ID_Pag
        JOIN Cartao ca ON ca.ID_CardNumber = c.ID_CardNumber
        JOIN Conta ct ON ct.ID_Numero = ca.ID_Numero
        WHERE c.Data_Compra = %s AND ct.ID_Cliente = %s
    """
    return execute_sql(query, params=(data_compra, id_cliente), fetch=True)

def get_historico_faturas_usuario_decrescente(id_cliente):
    """
    Retorna o histórico de faturas da mais recente para a mais antiga de um usuário.
    """
    query = '''
        SELECT f.ID_Pag, d.Valor_Pag, d.Status_Pag, d.Data_Pag
        FROM Fatura f
        JOIN Deposito d ON f.ID_Pag = d.ID_Pag
        JOIN Conta c ON c.ID_Cliente = %s
        WHERE d.ID_Pag = f.ID_Pag
        ORDER BY d.Data_Pag DESC
    '''
    return execute_sql(query, params=(id_cliente,), fetch=True)

def get_contas_usuario_com_saldo(id_cliente):
    """
    Retorna todas as contas vinculadas ao usuário mostrando o saldo disponível em cada conta (corrente, poupança, salário).
    """
    query = '''
        SELECT c.ID_Numero,
               c.Saldo,
               CASE
                   WHEN co.ID_Numero IS NOT NULL THEN 'Corrente'
                   WHEN p.ID_Numero IS NOT NULL THEN 'Poupanca'
                   WHEN s.ID_Numero IS NOT NULL THEN 'Salario'
                   ELSE 'Desconhecido'
               END AS tipo_conta
        FROM Conta c
        LEFT JOIN Corrente co ON c.ID_Numero = co.ID_Numero
        LEFT JOIN Poupanca p ON c.ID_Numero = p.ID_Numero
        LEFT JOIN Salario s ON c.ID_Numero = s.ID_Numero
        WHERE c.ID_Cliente = %s
    '''
    return execute_sql(query, params=(id_cliente,), fetch=True)


