from website.database import execute_sql

def buscar_compras(id_cliente):
    """
    Busca todas as compras do cliente informado, ordenadas pela data (mais recentes primeiro).
    Retorna uma lista de dicionários com os dados das compras.
    """
    query = """
        SELECT c.ID_Compra, c.Data_Compra, c.Valor, c.Estabelecimento
        FROM Compras c
        JOIN Cartao ca ON c.ID_CardNumber = ca.ID_CardNumber
        JOIN Conta co ON ca.ID_Numero = co.ID_Numero
        WHERE co.ID_Cliente = %s
        ORDER BY c.Data_Compra DESC
    """
    return execute_sql(query, (id_cliente,), fetch=True)

# Exemplo de uso:
# compras = buscar_compras(1234)
# for compra in compras:

if __name__ == "__main__":
    id_cliente_teste = 1234  # Troque para um ID_Cliente que exista no seu banco
    compras = buscar_compras(id_cliente_teste)
    print(compras)