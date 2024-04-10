import firebase_admin
from firebase_admin import credentials, auth , db
import pandas as pd

cred = credentials.Certificate("key.json")
# firebase_admin.initialize_app(cred, {
#    "databaseURL":"https://urlshortner-8ea0b-default-rtdb.firebaseio.com/"
# })

ref = db.reference('/')

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
    except Exception as e :
        print(e)
    
def push_new_url_entry(username,url,shorturl):
    try:
        ref.child('url_logs').push({
            'username': username,
            'url': url,
            'shorturl':shorturl
        })
    except Exception as e :
        print(e)

def get_user_history(username):
    url_logs = ref.child('url_logs').get()
    output = pd.DataFrame()
    if url_logs:
        for user_id, user_data in url_logs.items():
             if user_data['username'] == username:
                temp = {
                    'Original Url' : [user_data['url']],
                    'Short Url' : [user_data['shorturl']]
                }
                t = pd.DataFrame.from_dict(temp)
                output = output._append(t)
        return output
            