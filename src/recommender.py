def recommend_products(user, db):
    history = db.get_purchase_history(user)
    if not history:
        return db.get_popular_products()
    return db.get_similar_products(history[-1])

class Recommender:
    def fit(self, data):
        pass

def train_recommender(data):
    model = Recommender()
    model.fit(data)
    return model

# recomendar pelo pais se for brazil, por exemplo
def recommend_by_country(user, db):
    country = db.get_user_country(user)
    if country == 'Brazil':
        return db.get_brazilian_products()
    return []