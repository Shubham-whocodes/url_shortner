import firebase_admin
from firebase_admin import credentials, auth , db

cred = credentials.Certificate("key.json")
# firebase_admin.initialize_app(cred, {
#    "databaseURL":"https://urlshortner-8ea0b-default-rtdb.firebaseio.com/"
# })

ref = db.reference('/')

# cred = credentials.Certificate("key.json")
# firebase_admin.initialize_app(cred,{"databaseURL":"https://urlshortner-8ea0b-default-rtdb.firebaseio.com/"})

def authenticate_user(username, password):
    users = ref.child('users').get()
    if users:
        for user_id, user_data in users.items():
             if user_data['username'] == username and user_data['password'] == password:
                  return True
    return False
    
def create_user(username, password): 
    try:
        ref.child('users').push({
            'username': username,
            'password': password
        })
        return True
    except Exception as e :
        return False