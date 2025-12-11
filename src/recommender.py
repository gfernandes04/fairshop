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
