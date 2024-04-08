import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth


cred = credentials.Certificate("key.json")
# app = firebase_admin.initialize_app(cred)

def authenticate_user(email, password):
    try:
        user = auth.get_user_by_email(email)
        return user.uid
    except auth.AuthError as e:
        return None
    
def create_user(email, password):
    try:
        user = auth.create_user(email=email, password=password)
        return user.uid
    except auth.AuthError as e:
        return None