def risk_by_zip(user):
    if user.zip.startswith("11"):
        return 80
    return 20
