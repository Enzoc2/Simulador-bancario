from datetime import datetime
from website.database import execute_sql

def gasto_mes(id_cliente):
    """
    Soma o valor das compras do mês atual para o cliente informado.
    """
    # Obtém o mês e ano atual
    hoje = datetime.now()
    mes = hoje.month
    ano = hoje.year

    # Busca todas as compras do cliente no mês atual
    query = """
        SELECT SUM(Valor) as total
        FROM Compras c
        JOIN Cartao ca ON c.ID_CardNumber = ca.ID_CardNumber
        JOIN Conta co ON ca.ID_Numero = co.ID_Numero
        WHERE co.ID_Cliente = %s
        AND EXTRACT(MONTH FROM c.Data_Compra) = %s
        AND EXTRACT(YEAR FROM c.Data_Compra) = %s
    """
    result = execute_sql(query, (id_cliente, mes, ano), fetch_one=True)
    return result['total'] if result and result['total'] else 0.0

# Exemplo de