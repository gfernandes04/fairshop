def list_products(db):
    return db.get_all_products()

def get_product(product_id, db):
    return db.products.get(product_id)
