import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
cred = credentials.Certificate("/home/nakulan/VS Code/Project/Key.json")
firebase_admin.initialize_app(cred, {'databaseURL': 'https://fir-83250-default-rtdb.firebaseio.com/'})
ref = db.reference('/admin')

class administration:
    def reference():
        return ref
