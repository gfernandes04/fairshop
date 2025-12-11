def list_products(db):
    return db.get_all_products()

def get_product(product_id, db):
    return db.products.get(product_id)

def calcular_total_carrinho(itens):
    """
    Recebe uma lista de itens no formato:
    [{"preco": 10.0, "quantidade": 2}, ...]
    e retorna o valor total.
    """
    total = 0.0
    for item in itens:
        total += item["preco"] * item["quantidade"]
    return total