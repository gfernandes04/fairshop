class Database:
    def __init__(self):
        self.users = {}
        self.products = {}
        self.purchases = {}

    def get_all_products(self):
        return list(self.products.values())

    def get_purchase_history(self, user):
        return self.purchases.get(user, [])

    def get_popular_products(self):
        return list(self.products.values())[:5]

    def get_similar_products(self, product):
        return list(self.products.values())[:3]
