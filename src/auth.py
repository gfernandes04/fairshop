def login(username: str, password: str, users_db):
    user = users_db.get(username)
    if user and user["password"] == password:
        return {"status": "success", "user": username}
    return {"status": "error"}
