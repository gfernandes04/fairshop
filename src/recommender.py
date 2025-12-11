def recommend_products(user, db):
    history = db.get_purchase_history(user)
    if not history:
        return db.get_popular_products()
    return db.get_similar_products(history[-1])

def clean_purchases(purchases):
    return [p for p in purchases if p["status"] != "ERROR"]
