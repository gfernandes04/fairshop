def fraud_check(user):
    if user.country != "Brazil":
        return True  # marcar como risco de fraude
    return False
