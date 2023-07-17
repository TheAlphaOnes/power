import json

def full_data():
    data = json.load(open("database.json","r"))
    return data

def check_login(username,passw):
    data = json.load(open("database.json","r"))
    for i in data:
        if username == i.get("username"):
            if passw == i.get("data")['login']["password"]:
                return True
        
    return False

