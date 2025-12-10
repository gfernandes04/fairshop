def basic_risk_score(user):
    # Score simples baseado no número de devoluções
    return max(0, 100 - user.returns * 10)
